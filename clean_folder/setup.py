from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='1.0.0',
    packages=find_packages(),
    url='http://github.com/dummy_user/useful',
    author='Alexey Efimenko',
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.script:main'
        ]
    },
    install_requires=["shutil", "os", "sys"
    ],
)