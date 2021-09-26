# -*-coding:utf-8-*-
import time
import os
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
    out_path = os.path.join('.', '../output', "rouge_{}.metric".format(time.time()))

    with open(out_path, 'w') as out_file:
        for aggregator in aggregator_list:
            out_title = 'Evaluation with {}'.format(aggregator)
            out_file.write(out_title + '\n')
            print(out_title)
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
                    # for hypothesis_id, results_per_ref in enumerate(results):
                    #     nb_references = len(results_per_ref['p'])
                    #     for reference_id in range(nb_references):
                    #         out_str_title = '\tHypothesis #{} & Reference #{}: '.format(hypothesis_id, reference_id)
                    #         out_str_content = '\t' + prepare_results(metric,
                    #                                                  results_per_ref['p'][reference_id],
                    #                                                  results_per_ref['r'][reference_id],
                    #                                                  results_per_ref['f'][reference_id])
                    #         out_file.write(out_str_title+'\n')
                    #         out_file.write(out_str_content+'\n')
                    #         print(out_str_title)
                    #         print(out_str_content)
                    # out_file.write('\n')
                    # print()
                else:
                    out_str = prepare_results(metric, results['p'], results['r'], results['f'])
                    out_file.write(out_str + '\n')
                    print(out_str)
            print()
            print("输出文件路径：", out_path)


def metric_from_file(hypothesis_path, references_path, size):
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
    # aggregator_list = ['Avg', 'Best', 'Individual']
    aggregator_list = ['Avg']
    start_time = time.time()
    if size == -1:
        size = len(all_hypothesis)
    rouge_metric(all_hypothesis[:size], all_references[:size], aggregator_list)
    end_time = time.time()
    duration = end_time - start_time
    print("持续时间：", duration)





if __name__ == "__main__":
    hypothesis_path = '../data/predict/mscoco_neural_lstm.pred'
    # hypothesis_path = '../data/predict/mscoco_gen_chen.pred'
    references_path = '../data/mscoco/test_target.txt'
    # 句子个数
    size = -1
    metric_from_file(hypothesis_path, references_path, size)

"""
neural-lstm 全量test数据的评测结果		
    rouge-1:	P: 38.18	R: 31.26	F1: 33.92
	rouge-2:	P: 11.38	R:  9.14	F1:  9.98
	rouge-3:	P:  4.02	R:  3.16	F1:  3.47
	rouge-4:	P:  1.74	R:  1.33	F1:  1.47
	rouge-l:	P: 40.97	R: 34.79	F1: 37.28
	rouge-w:	P: 31.16	R: 16.16	F1: 20.97


t5 全量test数据的评测结果		
Evaluation with Avg
	rouge-1:	P: 41.34	R: 38.15	F1: 38.88
	rouge-2:	P: 13.24	R: 12.10	F1: 12.34
	rouge-3:	P:  4.70	R:  4.27	F1:  4.35
	rouge-4:	P:  1.83	R:  1.65	F1:  1.68
	rouge-l:	P: 42.01	R: 39.25	F1: 40.00
	rouge-w:	P: 32.16	R: 18.70	F1: 23.13
	
neural-lstm 10000条数据的评测结果
Evaluation with Avg
	rouge-1:	P: 37.27	R: 29.86	F1: 32.71
	rouge-2:	P: 10.40	R:  8.14	F1:  8.98
	rouge-3:	P:  3.42	R:  2.60	F1:  2.90
	rouge-4:	P:  1.49	R:  1.10	F1:  1.24
	rouge-l:	P: 40.27	R: 33.57	F1: 36.27
	rouge-w:	P: 30.48	R: 15.45	F1: 20.20
		
t5 100000条数据的评测结果	
Evaluation with Avg
	rouge-1:	P: 40.96	R: 37.93	F1: 38.60
	rouge-2:	P: 12.98	R: 11.89	F1: 12.12
	rouge-3:	P:  4.65	R:  4.23	F1:  4.30
	rouge-4:	P:  1.83	R:  1.64	F1:  1.67
	rouge-l:	P: 41.81	R: 39.17	F1: 39.88
	rouge-w:	P: 32.00	R: 18.68	F1: 23.08
"""
