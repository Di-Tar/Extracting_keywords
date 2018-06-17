#!/usr/bin/python3
# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QPushButton, QWidget, QGridLayout, QListWidget, QLabel


class AddToDictionaryForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        but_add_dictionary = QPushButton("Добавить в словарь")
        but_exit = QPushButton("Выход")

        leb1 = QLabel("Ключевые слова")
        leb2 = QLabel("Кандидаты на добавление")

        list_keywords1 = QListWidget()
        list_keywords1.resize(300, 120)

        list_keywords1.addItem("паралельные вычисления");
        list_keywords1.addItem("дисковые массивы");
        list_keywords1.addItem("сертификация");
        list_keywords1.addItem("тестирование");

        list_keywords2 = QListWidget()
        list_keywords2.resize(300, 120)

        list_keywords2.addItem("открытое татистическое исследование");
        list_keywords2.addItem("статистическое исследование");

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(leb1, 1, 0)
        grid.addWidget(leb2, 1, 1)
        grid.addWidget(list_keywords1, 2, 0)
        grid.addWidget(list_keywords2, 2, 1)
        grid.addWidget(but_add_dictionary, 3, 0)
        grid.addWidget(but_exit, 3, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 700, 400)
        self.setWindowTitle('Добавлеие ключевых слов в словарь')
        self.show()
