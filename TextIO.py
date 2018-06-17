# -*- coding: utf-8 -*-
import codecs
import json


class TextIO:

    # Считывание текста из фала
    def ReadTeaxt(self, addresIn):
        self.addresIn = addresIn
        with codecs.open(self.addresIn, 'r', "utf_8_sig") as file:
            IntermText = [row for row in file]

        IntermText = [line.rstrip() for line in IntermText]

        self.InputText = ""
        for part in IntermText:
            if part[-1] == '-':
                self.InputText += part[:-1]
            else:
                self.InputText += part + ' '

        print(self.InputText)

    def WriteTeaxt(self, text, addresOut):
        self.addresOut = addresOut
        with codecs.open(addresOut, 'w', "utf_8_sig") as out_file:
            json.dump(text, out_file, ensure_ascii=False, indent=4)
            # file.write(text)

# Testing

# t = TextIO('tren_text_1.txt')
# t.ReadTeaxt()
