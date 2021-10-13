# -*-coding:utf-8-*-
from nltk.translate.bleu_score import sentence_bleu, corpus_bleu
# reference = [['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']]
# candidate = ['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']
reference = ['The dog bit the man.', 'It was not unexpected.', 'The man bit him first.']
candidate = ['The dog bit the man.', "It wasn't surprising.", 'The man had just bitten him.']
# score = sentence_bleu(reference, candidate)
score = corpus_bleu(reference, candidate, weights=(1, 0, 0, 0))
print(score)