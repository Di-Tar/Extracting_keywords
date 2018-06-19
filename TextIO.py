# -*- coding: utf-8 -*-
import codecs
import json


class TextIO:

    # Считывание текста из фала
    def ReadTeaxt(self, addresIn):

        self.addresIn = addresIn

        # with codecs.open(self.addresIn, 'r', "utf_8_sig") as file:
        #     IntermText = [row for row in file]


        encoding = [
            'utf-8',
            'utf-16',
            'GBK',
            'windows-1251',
            'ASCII',
            'US-ASCII',
            'Big5',
        ]

        self.correct_encoding = ''

        for enc in encoding:
            try:
                open(self.addresIn, encoding=enc).read()
            except (UnicodeDecodeError, LookupError):
                pass
            else:
                self.correct_encoding = enc
                print('Done!')
                break

        print(self.correct_encoding)




        with codecs.open(self.addresIn, 'r', self.correct_encoding) as file:
            IntermText = [row for row in file]

        IntermText = [line.rstrip() for line in IntermText]

        IntermText2 = []
        self.InputText = ""

        for string in IntermText:
            if string != '':
                IntermText2.append(string)

        if self.correct_encoding != 'windows-1251':
            for part in IntermText2:
                if part[-1] == '-':
                    self.InputText += part[:-1]
                else:
                    self.InputText += part + ' '
        else:
            self.InputText = IntermText2

        print(self.InputText)
        print('Fin ReadTeaxt')
        return self.InputText

    def WriteJson(self, text, addresOut):
        self.addresOut = addresOut
        with codecs.open(self.addresOut, 'w', "utf_8_sig") as OutFile:
            json.dump(text, OutFile, ensure_ascii=False, indent = 4, sort_keys = True)
        print('Fin WriteJson')

    def ReadJson(self, addresIn):
        self.addresIn = addresIn
        with codecs.open(self.addresIn, 'r', "utf_8_sig") as InFile:
            InputText = json.load(InFile, )

        print('Fin ReadJson')
        return InputText

# Testing

# t = TextIO('tren_text_1.txt')
# t.ReadTeaxt()
