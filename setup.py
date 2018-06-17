# coding: utf-8

from cx_Freeze import setup, Executable

executables = [Executable('Main.py',
                          targetName='Extracting_keywords.exe',
                          base='Win32GUI',
                          )]

zip_include_packages = ['collections', 'encodings', 'importlib', 'PyQt5']

include_files = ['Аlgorithms',
                 'Thematic_dictionary',
                 'GUI',
                 'TextIO.py',
                 'README.txt',
                 ]

options = {
    'build_exe': {
        'zip_include_packages': zip_include_packages,
        'build_exe': 'Extracting_keywords',
        'include_files': include_files,
    }
}

setup(name='Extracting_keywords',
      version='0.0.1',
      description='Extract keywords from txt files.',
      executables=executables,
      options=options
      )