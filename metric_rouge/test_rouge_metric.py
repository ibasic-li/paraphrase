# -*-coding:utf-8-*-
import rouge_metric


def test_metric_from_file():
    rouge_metric.metric_from_file("../data/mscoco/test_source.txt", "../data/mscoco/test_target.txt", 10000)


def test_demo():
    all_hypothesis = [
        'a bicycle replica with a clock as the front wheel',
        'the bike has a clock as a tire',
        'a black honda motorcycle parked in front of a garage',
        'a honda motorcycle parked in a grass driveway',
        'a room with blue walls and a white sink and door',
        'blue and white color scheme in a small bathroom',
        'a car that seems to be parked illegally behind a legally parked car',
        'two cars parked on the sidewalk on the street',
        'a large passenger airplane flying through the air',
        'there is a gol plane taking off in a partly cloudy sky',
    ]

    all_references = [
        'a clock tower with a clock on the',
        'a clock tower with a clock on the',
        'a large white car parked in front of a',
        'a large metal wagon with a clock on the',
        'a kitchen with a refrigerator refrigerator and',
        'a close up of a white refrigerator with a',
        'a car parked in a car parked on a',
        'a clock tower with two cars on the',
        'a large train tower with a large',
        'a large refrigerator with a large metal',
    ]

    aggregator_list = ['Avg', 'Best', 'Individual']
    # size = -1
    rouge_metric.rouge_metric(all_hypothesis, all_references, aggregator_list)