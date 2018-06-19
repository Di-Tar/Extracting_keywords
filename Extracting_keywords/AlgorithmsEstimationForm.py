#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re


from PyQt5.QtWidgets import QPushButton, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QInputDialog


class AlgorithmsEstimationForm(QWidget):

    def __init__(self):
        super(AlgorithmsEstimationForm, self).__init__()
        self.initUI()


    def initUI(self):
        but_add_dictionary = QPushButton("Произвести оценку")
        but_add_dictionary.clicked.connect(self.Evaluate)

        self.leb1 = QLabel("Введите ключевые слова проставленные экспертом")
        self.leb2 = QLabel("Введите ключевые слова полученные в программе")
        self.leb3 = QLabel("Оценка: ")

        self.keywords = QLineEdit(self)
        self.fin_KeyWords = QLineEdit(self)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.leb1, 1, 1)
        grid.addWidget(self.keywords, 2, 0, 1, 3)
        grid.addWidget(self.leb2, 3, 1)
        grid.addWidget(self.fin_KeyWords, 4, 0, 1, 3)
        grid.addWidget(self.leb3, 5, 1)
        grid.addWidget(but_add_dictionary, 6, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Оценка работы алгоритма')
        self.show()

    def Evaluate(self):

        self.keywords.text()
        words = re.split('[ ]', self.keywords.text())
        for i in words:
            i.strip(' ')

        self.fin_KeyWords.text()
        fin_words = re.split('[ ]', self.fin_KeyWords.text())
        for i in fin_words:
            i.strip(' ')

        TPosit = 0

        for i in fin_words:
            for j in words:
                if i == j:
                    TPosit += 1

        FP = len(fin_words) - TPosit

        Prec = TPosit / (TPosit + FP)
        print('4')
        self.leb3.setText('Оценка: Точность = ' + str(Prec))







