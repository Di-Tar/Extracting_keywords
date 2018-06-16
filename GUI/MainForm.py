#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox, QPushButton, QWidget, \
    QLabel, QComboBox, QLineEdit, QGridLayout, QTextEdit, QListWidget, QApplication

from Extracting_keywords.GUI.AddSubjectAreaForm import AddSubjectAreaForm
from GUI.AlgorithmsEstimationForm import AlgorithmsEstimationForm


class MainForm(QWidget):

    def getx(self): return self.__addwin  # методы для чтения,

    def setx(self, value): self.__addwin = value  # записи

    def delx(self): del self.__addwin  # удаления свойства

    addwin = property(getx, setx, delx, "Свойство 'addwin'.")  # определение свойства

    # ---конец описания свойства

    def getx(self): return self.__addwin2  # методы для чтения,

    def setx(self, value): self.__addwin2 = value  # записи

    def delx(self): del self.__addwin2  # удаления свойства

    addwin2 = property(getx, setx, delx, "Свойство 'addwin2'.")  # определение свойства

    def __init__(self):
        super(MainForm, self).__init__()
        self.initUI()

    def initUI(self):
        addtextdocument = QPushButton("Добавить текстовый документ")

        but_subject_area = QPushButton("Добавить предметную область")

        but_extracting_keywords = QPushButton("Извлечь ключевые слова")

        but_add_dictionary = QPushButton("Добавить в словарь")

        but_save = QPushButton("Сохранить результат")

        but_algorithms_estimation = QPushButton("Оценка алгоритма")
        but_algorithms_estimation.clicked.connect(self.algorithms_Estimation)

        address = QLabel("Расположение файла")
        leb1 = QLabel("Предметная область")
        leb2 = QLabel("Размер выборки ключевых слов")
        results_extraction = QLabel("Результаты извлечения лкючевых слов:")

        comb_subject_area = QComboBox(self)

        sample_size = QLineEdit(self)

        keywords_line = QListWidget()

        # keywords_line.addItem("метод хи-квадрат")


        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(addtextdocument, 1, 0)
        grid.addWidget(address, 1, 1)
        grid.addWidget(leb1, 2, 0)
        grid.addWidget(comb_subject_area, 2, 1)
        grid.addWidget(but_subject_area, 2, 2)
        grid.addWidget(leb2, 3, 0)
        grid.addWidget(sample_size, 3, 1)
        grid.addWidget(results_extraction, 4, 0)
        grid.addWidget(keywords_line, 5, 0, 5, 2)
        grid.addWidget(but_extracting_keywords, 5, 2)
        grid.addWidget(but_add_dictionary, 6, 2)
        grid.addWidget(but_save, 10, 0)
        grid.addWidget(but_algorithms_estimation, 10, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Извлечение ключевых слов')
        self.show()

    @pyqtSlot()
    def algorithms_Estimation(self):
        self.addwin = AlgorithmsEstimationForm()


    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Выход', "Вы точно хотите выйти?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
