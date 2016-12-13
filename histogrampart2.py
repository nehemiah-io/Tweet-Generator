import random


class Histogram:

    def __init__(self, source_text):
        self.totalCount = 0
        self.histDict = self.makeHistogram(source_text)

    def makeHistogram(source_text):
        hist_dict = {}
        doc = open(source_text)
        lines = doc.readlines()
        for line in lines:
            for word in line.split(" "):
                if word in hist_dict:
                    hist_dict[word] = hist_dict[word]+1
                else:
                    hist_dict[word] = 1

        return hist_dict

    def frequency(histogram):
        pass

    def numberLine(self):
        ti = 0
        randomNumber = random.randint(0, self.count)
        for key, value in self.hist_dict.items():
            if randomNumber in range(ti, (ti + value)):
                return key
            else:
                ti += value
