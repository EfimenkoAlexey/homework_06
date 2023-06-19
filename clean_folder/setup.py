from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/EfimenkoAlexey/homework_06/tree/main/clean_folder',
    author='Alexey Efimenko',
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.script:main'
        ]
    },
    install_requires=["shutil", "os", "sys"
    ],
)