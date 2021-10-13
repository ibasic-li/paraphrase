# -*-coding:utf-8-*-
# from nlgeval import compute_metrics
#
# hypothesis_path = '../data/predict/qqp_5000_gen_1009.txt'
# references_path = '../data/qqp/tgt_test_1009.txt'
#
# metrics_dict = compute_metrics(hypothesis=hypothesis_path,
#                                references=[references_path])
#
# print(metrics_dict)


from .nlg_eval import compute_metrics


def metric_from_file(hypothesis, references, size, is_meteor=True, is_rouge=False, is_cider=False):
    metrics_dict = compute_metrics(hypothesis=hypothesis,
                                   references=[references], no_overlap=False, no_skipthoughts=True, no_glove=True,
                                   is_meteor=is_meteor, is_rouge=is_rouge, is_cider=is_cider)

    print(metrics_dict)
    return '{}'.format(metrics_dict)


if __name__ == "__main__":
    """
    可以同时计算meteor、rouge、cider这三种指标
    """
    hypothesis_path = '../../data/predict/jl_qqp_5000_gen_1013.txt'
    references_path = '../../data/qqp/tgt_1013.txt'
    size = -1
    metric_from_file(hypothesis_path, references_path, size)
