# -*-coding:utf-8-*-
from sumeval.metrics.bleu import BLEUCalculator


bleu = BLEUCalculator()
score = bleu.bleu("I am waiting on the beach",
                  "He is walking on the beach")
print(score)

# bleu_ja = BLEUCalculator(lang="ja")
# score_ja = bleu_ja.bleu("私はビーチで待ってる", "彼がベンチで待ってる")
#
# print(score_ja)