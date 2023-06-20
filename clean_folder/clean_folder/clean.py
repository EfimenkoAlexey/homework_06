
import shutil, os, sys

# Список расширений для каждой категории
CATEGORIES = {
    "images" : ("jpeg", "png", "jpg", "svg", "bmp"),
    "documents":("doc", "docx", "txt", "pdf", "xls", "xlsx", "pptx"),
    "video": ("avi", "mp4", "mov", "mkv"),
    "audio":("mp3", "ogg", "wav", "amr"),
    "archives":('zip', 'gz', 'tar')   
} 

# Папки, которые нужно игнорировать
IGNORE_FOLDERS = ['archives', 'video', 'audio', 'documents', 'images']

# Функция для транслитерации и нормализации имени файла
def normalize(name):
    
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    TRANS = {}
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION): 
        TRANS[ord(c)] = l 
        TRANS[ord(c.upper())] = l.upper()
    
    normalized_name = ''
    for char in name:
        if char.isalpha() and ord(char) in TRANS:
            normalized_name += TRANS[ord(char)]
        elif char.isdigit() or char.isalpha() and ord(char) not in TRANS:
            normalized_name += char
        else:
            normalized_name += "_"
    
    return normalized_name

# Функция для сортировки и обработки папки
def process_folder(folder_path):
    known_extensions = set()
    unknown_extensions = set()

    files = os.listdir(folder_path)

    for file in files:
        file_path = os.path.join(folder_path,file)

        if os.path.isdir(file_path):
            if file not in IGNORE_FOLDERS:
                process_folder(file_path)
        else:
            file_extension = file.split('.')[-1].lower()

            def file_in_folder():
                normalized_name = normalize(file.split('.')[0])
                new_name = f'{normalized_name}.{file_extension}'
                target_folder = os.path.join(folder_path, category)
                os.makedirs(target_folder, exist_ok=True)
                res = shutil.move(file_path, target_folder+"/"+new_name)
                return res

            if file_extension in CATEGORIES["images"]:
                category = "images"
                file_in_folder()
                known_extensions.add(file_extension)

            elif file_extension in CATEGORIES["documents"]:
                category = "documents"
                file_in_folder()
                known_extensions.add(file_extension)

            elif file_extension in CATEGORIES["video"]:
                category = "video"
                file_in_folder()
                known_extensions.add(file_extension)

            elif file_extension in CATEGORIES["audio"]:
                category = "audio"
                file_in_folder()
                known_extensions.add(file_extension)

            elif file_extension in CATEGORIES["archives"]:
                category = "archives"
                target_folder = os.path.join(folder_path, category)
                os.makedirs(target_folder, exist_ok=True)
                shutil.copy(file_path, target_folder+"/"+file)
                normalized_name = normalize(file.split('.')[0])
                new_name = f'{normalized_name}.{file_extension}'
                os.replace(target_folder+"/"+file,target_folder+"/"+new_name)
                shutil.unpack_archive(target_folder + "/" + new_name, target_folder+"/" + normalized_name)
                os.remove(target_folder + "/" + new_name)
                known_extensions.add(file_extension)
            else:
                category = None
                unknown_extensions.add(file_extension)
      
    # Удаление пустых папок
    if len(os.listdir(folder_path)) == 0:
        os.rmdir(folder_path)

    for category, extensions in CATEGORIES.items():
        if file_extension in extensions:
            print(f'Файл {file} принадлежит категории "{category}"')
            break
    
    print("Список файлов в каждой категории:")
    for category in CATEGORIES:
        if os.path.exists(folder_path+"/"+category):
            category_path = os.path.join(folder_path, category)
            files = os.listdir(category_path)
            print(f"Категория: {category}")
            for file in files:
                print(f"- {file}")
            print()   
        
    print("Известные расширение:", ", ".join(known_extensions))
    print("Неизвестные расширения:", ", ".join(unknown_extensions))

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Правильно использовать: python clean.py <folder_path>")
    else:
        folder_path = sys.argv[1]
        process_folder(folder_path)