from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0.0',
    description='Code small program',
    url='https://github.com/EfimenkoAlexey/homework_06/tree/main/clean_folder',
    author='Alexey Efimenko',
    packages=find_namespace_packages(),
    install_requires=["sys", "os", "shutil"],
    entry_points={'console_scripts': ['clean_folder = clean_folder.clean_folder:main']}
)