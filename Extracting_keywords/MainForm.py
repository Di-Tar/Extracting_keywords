#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Основное окно ПО. Отрисовывет основную форму, взаимодействует с алгоритмами
# и выводит результат.

from PyQt5.QtWidgets import QMessageBox, QPushButton, QWidget, QLabel, \
    QComboBox, QGridLayout, QListWidget, QFileDialog, QSpinBox

from AlgorithmsEstimationForm import AlgorithmsEstimationForm
from TextIO import TextIO
from DefinitionCharacteristics import DefinitionCharacteristics
from Postprocessing import Postprocessing
from PreliminaryProcessing import PreliminaryProcessing


class MainForm(QWidget):

    def getx(self): return self.__addwin

    def setx(self, value): self.__addwin = value

    def delx(self): del self.__addwin

    addwin = property(getx, setx, delx, "Свойство 'addwin'.")

    def __init__(self):
        super(MainForm, self).__init__()
        self.initUI()

    def initUI(self):

        addtextdocument = QPushButton("Добавить текстовый документ")
        addtextdocument.clicked.connect(self.ATDDialog)

        but_subject_area = QPushButton("Добавить предметную область")
        but_subject_area.setEnabled(False)


        self.but_extracting_keywords = QPushButton("Извлечь ключевые слова")
        self.but_extracting_keywords.setEnabled(False)
        self.but_extracting_keywords.clicked.connect(self.RunExtractingKey)

        but_add_dictionary = QPushButton("Добавить в словарь")
        but_add_dictionary.setEnabled(False)

        but_save = QPushButton("Сохранить результат")
        but_save.setEnabled(False)

        self.but_algorithms_estimation = QPushButton("Оценка алгоритма")
        # self.but_algorithms_estimation.setEnabled(False)
        self.but_algorithms_estimation.clicked.connect(self.RunEstimation)


        self.address = QLabel("Необходимо выборать файл с расширением '.txt'")
        leb1 = QLabel("Предметная область")
        leb2 = QLabel("Размер выборки ключевых слов")
        results_extraction = QLabel("Полученные ключевые слова:")

        self.comb_subject_area = QComboBox(self)
        self.comb_subject_area.setEditable(False)
        self.comb_subject_area.addItem("50.41.17 Системное программное обеспечение")


        self.sample_size = QSpinBox(self, minimum=0, maximum=20)
        self.sample_size.setEnabled(False)
        self.sample_size.valueChanged.connect(self.CheckExtract)


        self.keywords_line = QListWidget()


        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(addtextdocument, 1, 0)
        grid.addWidget(self.address, 1, 1, 1, 1,)
        grid.addWidget(leb1, 2, 0)
        grid.addWidget(self.comb_subject_area, 2, 1)
        grid.addWidget(but_subject_area, 2, 2)
        grid.addWidget(leb2, 3, 0)
        grid.addWidget(self.sample_size, 3, 1)
        grid.addWidget(results_extraction, 4, 0)
        grid.addWidget(self.keywords_line, 5, 0, 5, 2)
        grid.addWidget(self.but_extracting_keywords, 5, 2)
        grid.addWidget(but_add_dictionary, 6, 2)
        grid.addWidget(but_save, 10, 0)
        grid.addWidget(self.but_algorithms_estimation, 10, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 900, 600)
        self.setWindowTitle('Извлечение ключевых слов')
        self.show()


    def ATDDialog(self):
        self.address_text = QFileDialog.getOpenFileName(self, 'Выберите документ', '','Text Files (*.txt)')
        self.address.setText('Загруженный файл: ' + self.address_text[0])
        self.address.adjustSize()

        self.sample_size.setEnabled(True)



    def RunEstimation(self):
        self.addwin = AlgorithmsEstimationForm()



    def CheckExtract(self):
        if self.sample_size.value() != 0:
            self.but_extracting_keywords.setEnabled(True)
        else: self.but_extracting_keywords.setEnabled(False)


    def RunExtractingKey(self):
        self.but_extracting_keywords.setEnabled(False)
        self.keywords_line.clear()
        self.keyword = PreliminaryProcessing(self.address_text[0])
        print('End PreliminaryProcessing')
        self.keyword = DefinitionCharacteristics(self.keyword.fin_dict_Cand)
        print('End DefinitionCharacteristics')
        self.keyword = Postprocessing(self.keyword.candidate_words, int(self.sample_size.value()))
        print('End Postprocessing')

        for n in self.keyword.fin_KeyWords:
            self.keywords_line.addItem(n)

        self.but_extracting_keywords.setEnabled(True)
        self.but_algorithms_estimation.setEnabled(True)



    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Выход', 'Вы точно хотите выйти?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()