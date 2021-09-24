# -*-coding:utf-8-*-
from sacrebleu.metrics import BLEU, CHRF, TER

# refs = [  # First set of references
#     ['The dog bit the man.', 'It was not unexpected.', 'The man bit him first.'],
#     # Second set of references
#     ['The dog had bit the man.', 'No one was surprised.', 'The man had bitten the dog.'],
# ]
# BLEU = 45.07 70.6/42.9/36.4/37.5 (BP = 1.000 ratio = 1.000 hyp_len = 17 ref_len = 17) <class 'sacrebleu.metrics.bleu.BLEUScore'>
refs = [['The dog bit the man.', 'It was not unexpected.', 'The man bit him first.']]
# BLEU = 0.00 0.0/0.0/0.0/0.0 (BP = 1.000 ratio = 5.667 hyp_len = 17 ref_len = 3) <class 'sacrebleu.metrics.bleu.BLEUScore'>
# refs = ['The dog bit the man.', "It wasn't surprising.", 'The man had just bitten him.']
#BLEU = 100.00 100.0/100.0/100.0/100.0 (BP = 1.000 ratio = 1.000 hyp_len = 17 ref_len = 17) <class 'sacrebleu.metrics.bleu.BLEUScore'>
# refs = [['The dog bit the man.', "It wasn't surprising.", 'The man had just bitten him.']]

sys = ['The dog bit the man.', "It wasn't surprising.", 'The man had just bitten him.']
bleu = BLEU()
score = bleu.corpus_score(sys, refs)
print(score, type(score))
# BLEU = 48.53 82.4/50.0/45.5/37.5 (BP = 0.943 ratio = 0.944 hyp_len = 17 ref_len = 18)
bleu.get_signature()
# nrefs:2|case:mixed|eff:no|tok:13a|smooth:exp|version:2.0.0
chrf = CHRF()
chrf.corpus_score(sys, refs)
# chrF2 = 59.73


# sacrebleu .\data\mscoco\test_target.txt -i .\data\predict\mscoco_gen_chen.predict -m bleu -b -w 4
