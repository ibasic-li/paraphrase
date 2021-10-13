# -*-coding:utf-8-*-
import time
from nltk import word_tokenize
from nltk.translate.bleu_score import sentence_bleu, corpus_bleu


def metric_from_file(hypothesis_path, references_path, size, metric_type):
    """
    :param hypothesis_path:
    :param references_path:
    :return:
    """
    # all_hypothesis = []
    # all_references = []
    with open(hypothesis_path, 'r', encoding='utf8') as hypothesis_file:
        all_hypothesis = hypothesis_file.readlines()
    with open(references_path, 'r', encoding='utf8') as references_file:
        all_references = references_file.readlines()

    start_time = time.time()
    if size == -1:
        size = len(all_hypothesis)
    print("开始评测，数据量：", size)

    all_hypothesis_token = []
    for hy in all_hypothesis:
        result_hy = word_tokenize(hy)
        all_hypothesis_token.append(result_hy)

    all_references_toekn = []
    for refer in all_references:
        result_re = word_tokenize(refer)
        all_references_toekn.append([result_re])

    score = corpus_bleu(all_references_toekn, all_hypothesis_token)
    print(score)
    # if metric_type == "bleu":
    #     bleu_metric(all_hypothesis[:size], all_references[:size])
    # elif metric_type == "ter":
    #     ter_metric(all_hypothesis[:size], all_references[:size])
    # elif metric_type == "chrf":
    #     chrf_metric(all_hypothesis[:size], all_references[:size])
    end_time = time.time()
    duration = end_time - start_time
    print("持续时间：", duration)


if __name__ == "__main__":
    # BLEU = 6.41 34.8/10.7/3.5/1.3 (BP = 1.000 ratio = 1.019 hyp_len = 1728602 ref_len = 1695740)
    # hypothesis_path = '../data/predict/mscoco_gen_chen.pred'
    # 5.72 37.2/11.1/3.8/1.7 (BP = 0.800 ratio = 0.818 hyp_len = 1386274 ref_len = 1695740)
    # hypothesis_path = '../data/predict/mscoco_neural_lstm.pred'
    # BLEU = 100.00 100.0/100.0/100.0/100.0 (BP = 1.000 ratio = 1.000 hyp_len = 108 ref_len = 108)
    # hypothesis_path = '../data/mscoco/test_target.txt'
    # BLEU = 10.96 44.1/17.5/7.4/3.5 (BP = 0.918 ratio = 0.921 hyp_len = 1562279 ref_len = 1695740)
    # hypothesis_path = '../data/predict/mscoco_t5_all.pred'
    # references_path = '../data/mscoco/test_target.txt'
    # BLEU = 0.03 5.0/0.1/0.0/0.0
    # hypothesis_path = '../../../data/predict/qqp_5000_gen_1009.txt'
    # references_path = '../../../data/qqp/tgt_test_1009.txt'
    hypothesis_path = '../../../data/predict/jl_qqp_5000_gen_1013.txt'
    references_path = '../../../data/qqp/tgt_1013.txt'
    # 句子个数
    size = -1
    # bleu, chrf, ter
    metric_from_file(hypothesis_path, references_path, size, 'bleu')
