#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QInputDialog


class AlgorithmsEstimationForm(QWidget):
    def __init__(self):
        super(AlgorithmsEstimationForm, self).__init__()
        self.initUI()

    def initUI(self):
        but_add_dictionary = QPushButton("Произвести оценку")

        leb1 = QLabel("Введите ключевые слова проставленные экспертом")

        keywords = QTextEdit(self)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(leb1, 1, 1)
        grid.addWidget(keywords, 2, 0, 1, 3)
        grid.addWidget(but_add_dictionary, 3, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Оценка работы алгоритма')
        self.show()

        # but_add_dictionary = QPushButton("Выход")
        #
        # leb1 = QLabel("Результаты оценки")
        # leb2 = QLabel("Precision = 40 %")
        # leb3 = QLabel("Recall = 68.6 %")
        # leb4 = QLabel("AvP = 50.5 %")
        #
        #
        # grid = QGridLayout()
        # grid.setSpacing(10)
        #
        # grid.addWidget(leb1, 1, 0)
        # grid.addWidget(leb2, 2, 0)
        # grid.addWidget(leb3, 3, 0)
        # grid.addWidget(leb4, 4, 0)
        # grid.addWidget(but_add_dictionary, 5, 0)
        #
        # self.setLayout(grid)
        #
        # self.setGeometry(300, 300, 400, 200)
        # self.setWindowTitle('Оценка работы алгоритма')
        # self.show()
