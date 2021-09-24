# -*-coding:utf-8-*-
import rouge_metric


def test_metric_from_file():
    rouge_metric.metric_from_file("./data/mscoco/test_source.txt", "./data/mscoco/test_target.txt", 10000)