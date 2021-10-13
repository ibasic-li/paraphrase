# -*-coding:utf-8-*-
import time
import os
import rouge
from tqdm import tqdm
from sacrebleu.metrics import BLEU, CHRF, TER


def prepare_results(metric, p, r, f):
    return '\t{}:\t{}: {:5.2f}\t{}: {:5.2f}\t{}: {:5.2f}'.format(metric, 'P', 100.0 * p, 'R', 100.0 * r, 'F1',
                                                                 100.0 * f)


def bleu_metric(all_hypothesis, all_references):
    """

    :param all_hypothesis:
    :param all_references:
    :return:
    """
    out_path = os.path.join('', '../output', "rouge_{}.metric".format(time.time()))

    with open(out_path, 'w') as out_file:
        bleu = BLEU()
        score = bleu.corpus_score(all_hypothesis, [all_references])
        print(score)
        out_file.write("{}".format(score))
        print("输出文件路径：", out_path)


def ter_metric(all_hypothesis, all_references):
    ter = TER()
    score = ter.corpus_score(all_hypothesis, [all_references])
    print(score)


def chrf_metric(all_hypothesis, all_references):
    chrf = CHRF()
    score = chrf.corpus_score(all_hypothesis, [all_references])
    print(score)


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
    if metric_type == "bleu":
        bleu_metric(all_hypothesis[:size], all_references[:size])
    elif metric_type == "ter":
        ter_metric(all_hypothesis[:size], all_references[:size])
    elif metric_type == "chrf":
        chrf_metric(all_hypothesis[:size], all_references[:size])
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
    # BLEU = 24.15 55.5/31.2/20.3/13.8 (BP = 0.914 ratio = 0.918 hyp_len = 50822 ref_len = 55372)
    hypothesis_path = '../../data/predict/qqp_5000_gen_1009.txt'
    references_path = '../../data/qqp/tgt_test_1009.txt'

    # 句子个数
    size = -1
    # bleu, chrf, ter
    metric_from_file(hypothesis_path, references_path, size, 'bleu')
