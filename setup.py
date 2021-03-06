# coding: utf-8

from cx_Freeze import setup, Executable

executables = [Executable('Main.py',
                          targetName='Extracting_keywords.exe',
                          base='Win32GUI',
                          )]

zip_include_packages = ['collections', 'encodings', 'importlib', 'PyQt5']

include_files = ['README.txt',
                 'MainForm.py',
                 'Postprocessing.py',
                 'TextIO.py',
                 'AddSubjectAreaForm.py',
                 'AddToDictionaryForm.py',
                 'AlgorithmsEstimationForm.py',
                 'DefinitionCharacteristics.py',
                 'PreliminaryProcessing.py',
                 'TermDictionary.py',
                 'Text_dis_alg.json',
                 'udk_504117.json',
                 ]

options = {
    'build_exe': {
        'zip_include_packages': zip_include_packages,
        'build_exe': 'Extracting_keywords',
        'include_files': include_files,
    }
}

setup(name='Extracting_keywords',
      version='0.1.0',
      description='Extract keywords from txt files.',
      executables=executables,
      options=options
      )