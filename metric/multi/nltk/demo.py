# -*-coding:utf-8-*-
import time

from nltk import word_tokenize
from nltk.translate.bleu_score import sentence_bleu


string = "All work and no play makes jack a dull boy, all work and no play"
result = word_tokenize(string)
# print(word_tokenize(string))
print(result)

# reference = [['this', 'is', 'a', 'test'], ['this', 'is' 'test']]
# candidate = ['this', 'is', 'a', 'test']
reference = [result]
candidate = result
score = sentence_bleu(reference, candidate)
print(score)
