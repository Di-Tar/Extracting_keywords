import operator

from TextIO import TextIO
from Аlgorithms.DefinitionCharacteristics import DefinitionCharacteristics


class PreliminaryProcessing:

    def __init__(self, candidate_words):
        self.candidate_words = candidate_words
        self.PrelProc()

    def PrelProc(self):
        self.Rank_Cand()


    def Rank_Cand(self):
        for key_w in self.candidate_words:
            n_char = len(self.candidate_words[key_w]) - 1


        for i in range(n_char):
            n = 1
            for key_w in self.candidate_words:
                (self.candidate_words[key_w]).append(n)
                n += 1


        for key_w in self.candidate_words:
            (self.candidate_words[key_w]).append(0)


        for key_w in self.candidate_words:
            for key_w2 in self.candidate_words:
                if self.candidate_words[key_w][1] < self.candidate_words[key_w2][1] and \
                    self.candidate_words[key_w][1 + n_char] > self.candidate_words[key_w2][1 + n_char]:
                    self.candidate_words[key_w][1 + n_char], self.candidate_words[key_w2][1 + n_char] =\
                    self.candidate_words[key_w2][1 + n_char], self.candidate_words[key_w][1 + n_char]

                if self.candidate_words[key_w][2] < self.candidate_words[key_w2][2] and \
                        self.candidate_words[key_w][2 + n_char] < self.candidate_words[key_w2][2 + n_char]:
                    self.candidate_words[key_w][2 + n_char], self.candidate_words[key_w2][2 + n_char] = \
                        self.candidate_words[key_w2][2 + n_char], self.candidate_words[key_w][2 + n_char]
        print(self.candidate_words)

        for key_w in self.candidate_words:
            for i in range(3, 5):
                self.candidate_words[key_w][5] = \
                    (int(self.candidate_words[key_w][5]) + 1 / int(self.candidate_words[key_w][i]))

        for key_w in self.candidate_words:
            print(self.candidate_words[key_w][5])



base_text = TextIO()
f = DefinitionCharacteristics(base_text.ReadJson('Text_dis_alg.json'))
p = PreliminaryProcessing(f.candidate_words)