from histograms import Dictogram
from probabilityModel import StochasticSample
import refinedCorpus

def main():
    txt = open("/Users/ownernopassword/Desktop/Tweet-Generator-Course/harry.txt")
    cleanText = refinedCorpus.refineText(txt)
    histogram = Dictogram(cleanText)
    stochasticSampler = StochasticSample(histogram)

    return stochasticSampler.generateSentence()
