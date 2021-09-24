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
    out_path = os.path.join('.', '../output', "rouge_{}.metric".format(time.time()))

    with open(out_path, 'w') as out_file:
        bleu = BLEU()
        score = bleu.corpus_score(all_hypothesis, [all_references])
        print(score)
        out_file.write("{}".format(score))
        print("输出文件路径：", out_path)


def metric_from_file(hypothesis_path, references_path, size):
    """
    :param hypothesis_path:
    :param references_path:
    :return:
    """
    # all_hypothesis = []
    # all_references = []
    with open(hypothesis_path, 'r') as hypothesis_file:
        all_hypothesis = hypothesis_file.readlines()
    with open(references_path, 'r') as references_file:
        all_references = references_file.readlines()

    start_time = time.time()
    if size == -1:
        size = len(all_hypothesis)
    bleu_metric(all_hypothesis[:size], all_references[:size])
    end_time = time.time()
    duration = end_time - start_time
    print("持续时间：", duration)


if __name__ == "__main__":
    # BLEU = 6.41 34.8/10.7/3.5/1.3 (BP = 1.000 ratio = 1.019 hyp_len = 1728602 ref_len = 1695740)
    hypothesis_path = '../data/predict/mscoco_gen_chen.predict'
    # 5.05 36.5/10.2/3.3/1.4 (BP = 0.780 ratio = 0.801 hyp_len = 84090 ref_len = 104997)
    # hypothesis_path = '../data/predict/result_1632464778.2831151.predict'
    # BLEU = 100.00 100.0/100.0/100.0/100.0 (BP = 1.000 ratio = 1.000 hyp_len = 108 ref_len = 108)
    # hypothesis_path = '../data/mscoco/test_target.txt'
    references_path = '../data/mscoco/test_target.txt'
    # 句子个数
    size = -1
    metric_from_file(hypothesis_path, references_path, size)
