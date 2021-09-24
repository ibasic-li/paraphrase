# -*-coding:utf-8-*-
import time

import rouge
from tqdm import tqdm

def prepare_results(metric, p, r, f):
    return '\t{}:\t{}: {:5.2f}\t{}: {:5.2f}\t{}: {:5.2f}'.format(metric, 'P', 100.0 * p, 'R', 100.0 * r, 'F1',
                                                                 100.0 * f)


def rouge_metric(all_hypothesis, all_references, aggregator_list):
    """

    :param all_hypothesis:
    :param all_references:
    :param aggregator_list: ['Avg', 'Best', 'Individual']
    :return:
    """
    for aggregator in aggregator_list:
        print('Evaluation with {}'.format(aggregator))
        apply_avg = aggregator == 'Avg'
        apply_best = aggregator == 'Best'

        evaluator = rouge.Rouge(metrics=['rouge-n', 'rouge-l', 'rouge-w'],
                                max_n=4,
                                limit_length=True,
                                length_limit=100,
                                length_limit_type='words',
                                apply_avg=apply_avg,
                                apply_best=apply_best,
                                alpha=0.5,  # Default F1_score
                                weight_factor=1.2,
                                stemming=True)

        # hypothesis_1 = "King Norodom Sihanouk has declined requests to chair a summit of Cambodia 's top political leaders , saying the meeting would not bring any progress in deadlocked negotiations to form a government .\nGovernment and opposition parties have asked King Norodom Sihanouk to host a summit meeting after a series of post-election negotiations between the two opposition groups and Hun Sen 's party to form a new government failed .\nHun Sen 's ruling party narrowly won a majority in elections in July , but the opposition _ claiming widespread intimidation and fraud _ has denied Hun Sen the two-thirds vote in parliament required to approve the next government .\n"
        # references_1 = [
        #     "Prospects were dim for resolution of the political crisis in Cambodia in October 1998.\nPrime Minister Hun Sen insisted that talks take place in Cambodia while opposition leaders Ranariddh and Sam Rainsy, fearing arrest at home, wanted them abroad.\nKing Sihanouk declined to chair talks in either place.\nA U.S. House resolution criticized Hun Sen's regime while the opposition tried to cut off his access to loans.\nBut in November the King announced a coalition government with Hun Sen heading the executive and Ranariddh leading the parliament.\nLeft out, Sam Rainsy sought the King's assurance of Hun Sen's promise of safety and freedom for all politicians.",
        #     "Cambodian prime minister Hun Sen rejects demands of 2 opposition parties for talks in Beijing after failing to win a 2/3 majority in recent elections.\nSihanouk refuses to host talks in Beijing.\nOpposition parties ask the Asian Development Bank to stop loans to Hun Sen's government.\nCCP defends Hun Sen to the US Senate.\nFUNCINPEC refuses to share the presidency.\nHun Sen and Ranariddh eventually form a coalition at summit convened by Sihanouk.\nHun Sen remains prime minister, Ranariddh is president of the national assembly, and a new senate will be formed.\nOpposition leader Rainsy left out.\nHe seeks strong assurance of safety should he return to Cambodia.\n",
        #     ]
        #
        # hypothesis_2 = "China 's government said Thursday that two prominent dissidents arrested this week are suspected of endangering national security _ the clearest sign yet Chinese leaders plan to quash a would-be opposition party .\nOne leader of a suppressed new political party will be tried on Dec. 17 on a charge of colluding with foreign enemies of China '' to incite the subversion of state power , '' according to court documents given to his wife on Monday .\nWith attorneys locked up , harassed or plain scared , two prominent dissidents will defend themselves against charges of subversion Thursday in China 's highest-profile dissident trials in two years .\n"
        # references_2 = "Hurricane Mitch, category 5 hurricane, brought widespread death and destruction to Central American.\nEspecially hard hit was Honduras where an estimated 6,076 people lost their lives.\nThe hurricane, which lingered off the coast of Honduras for 3 days before moving off, flooded large areas, destroying crops and property.\nThe U.S. and European Union were joined by Pope John Paul II in a call for money and workers to help the stricken area.\nPresident Clinton sent Tipper Gore, wife of Vice President Gore to the area to deliver much needed supplies to the area, demonstrating U.S. commitment to the recovery of the region.\n"
        #
        # all_hypothesis = [hypothesis_1, hypothesis_2]
        # all_references = [references_1, references_2]

        scores = evaluator.get_scores(all_hypothesis, all_references)

        for metric, results in sorted(scores.items(), key=lambda x: x[0]):
            if not apply_avg and not apply_best:  # value is a type of list as we evaluate each summary vs each reference
                ""
                for hypothesis_id, results_per_ref in enumerate(results):
                    nb_references = len(results_per_ref['p'])
                    for reference_id in range(nb_references):
                        print('\tHypothesis #{} & Reference #{}: '.format(hypothesis_id, reference_id))
                        print('\t' + prepare_results(metric,
                                                     results_per_ref['p'][reference_id],
                                                     results_per_ref['r'][reference_id],
                                                     results_per_ref['f'][reference_id]))
                print()
            else:
                print(prepare_results(metric, results['p'], results['r'], results['f']))
        print()


def metric_from_file(hypothesis_path, references_path):
    """
    1000条大约耗时4.3秒
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
    aggregator_list = ['Avg', 'Best']
    start_time = time.time()
    rouge_metric(all_hypothesis, all_references, aggregator_list)
    end_time = time.time()
    duration = end_time - start_time
    print("持续时间：", duration)


def test1():
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
    rouge_metric(all_hypothesis, all_references, aggregator_list)
