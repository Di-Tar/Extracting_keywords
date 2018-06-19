from TextIO import TextIO
from DefinitionCharacteristics import DefinitionCharacteristics


class Postprocessing:

    def __init__(self, candidate_words, size):
        self.candidate_words = candidate_words
        self.size = size
        self.PrelProc()


    def PrelProc(self):
        self.Rank_Cand()
        self.KSampCalculare()



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

        for key_w in self.candidate_words:
            for i in range(3, 5):
                self.candidate_words[key_w][5] = \
                    (int(self.candidate_words[key_w][5]) + 1 / int(self.candidate_words[key_w][i]))

        print(self.candidate_words)
        print('Fin Rank_Cand')


    def KSampCalculare(self):

        sorted_x = self.candidate_words.items()

        KeyWords = []
        for n in sorted_x:
            KeyWords.append([n[0], n[1][5]])


        KeyWords.sort(key=lambda i: i[1], reverse=1)
        try:
            i = 0
            self.fin_KeyWords = []
            while i < self.size:
                self.fin_KeyWords.append(KeyWords[i][0])
                i += 1
        except IndexError:
            print('IndexError')
        print(self.fin_KeyWords)

        print('Fin KSampCalculare')

# base_text = TextIO()
# f = DefinitionCharacteristics(base_text.ReadJson('Text_dis_alg.json'))
# p = Postprocessing(f.candidate_words, 10)