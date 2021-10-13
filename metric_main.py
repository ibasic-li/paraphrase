# -*-coding:utf-8-*-
from metric.bleu import bleu_metric
from metric.multi import metric_nlg_eval
from metric.rouge_my import rouge_metric
from common import constant
import os


def metric_from_file(hypothesis, references, size):
    # 句子个数
    size = -1

    is_rough = False
    is_bleu = True
    is_meteor = True
    result = ''
    if is_rough:
        rouge_result = rouge_metric.metric_from_file(hypothesis, references, size)
        result += rouge_result
    if is_bleu:
        bleu_result = bleu_metric.metric_from_file(hypothesis, references, size, 'bleu')
        result += bleu_result
    if is_meteor:
        meteor_result = metric_nlg_eval.metric_from_file(hypothesis, references, size)
        result += meteor_result
    return result


if __name__ == "__main__":
    # 模型生成的句子
    DATA_PATH = constant.DATA_DIR
    hypothesis_path = constant.OUTPUT_DIR + 'jl_qqp_5000_gen_1013.txt1634126019.4987907'
    # 参考的句子
    references_path = constant.OUTPUT_DIR + 'tgt_1013.txt1634126019.5007865'
    print('hypothesis_path:' + hypothesis_path)

    print('references_path:' + references_path)
    size = -1
    metric_from_file(hypothesis_path, references_path, size)
