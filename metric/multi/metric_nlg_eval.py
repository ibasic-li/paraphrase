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


from nlg_eval import compute_metrics
"""
可以同时计算meteor、rouge、cider这三种指标
"""
hypothesis_path = '../../data/predict/qqp_5000_gen_1009.txt'
references_path = '../../data/qqp/tgt_test_1009.txt'

metrics_dict = compute_metrics(hypothesis=hypothesis_path,
                               references=[references_path], no_overlap=False, no_skipthoughts=True, no_glove=True)

print(metrics_dict)