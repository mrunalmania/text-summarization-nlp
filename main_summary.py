import numpy as np
import PyPDF2
import sys
import matplotlib.pyplot as plt
import networkx as nx

from nltk.tokenize.punkt import PunktSentenceTokenizer
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer


def tokenize(document):
    doc_tokenizer = PunktSentenceTokenizer()
    sentences_list = doc_tokenizer.tokenize(document)
    return sentences_list


def main_summary(raw_text):
    document = raw_text

    sentences_list = tokenize(document)

    cv = CountVectorizer()
    cv_matrix = cv.fit_transform(sentences_list)

    cv_demo = CountVectorizer()  # a demo object of class CountVectorizer

    text_demo = ["Ashish is good, you are bad", "I am not bad"]
    res_demo = cv_demo.fit_transform(text_demo)

    normal_matrix = TfidfTransformer().fit_transform(cv_matrix)

    res_graph = normal_matrix * normal_matrix.T

    nx_graph = nx.from_scipy_sparse_matrix(res_graph)
    nx.draw_circular(nx_graph)

    ranks = nx.pagerank(nx_graph)

    sentence_array = sorted(
        ((ranks[i], s) for i, s in enumerate(sentences_list)), reverse=True)
    sentence_array = np.asarray(sentence_array)

    rank_max = float(sentence_array[0][0])
    rank_min = float(sentence_array[len(sentence_array) - 1][0])

    temp_array = []

    flag = 0
    if rank_max - rank_min == 0:
        temp_array.append(0)
        flag = 1

    # If the sentence has different ranks
    if flag != 1:
        for i in range(0, len(sentence_array)):
            temp_array.append(
                (float(sentence_array[i][0]) - rank_min) / (rank_max - rank_min))

    # Calculation of threshold:
    # We take the mean value of normalized scores
    # any sentence with the normalized score 0.2 more than the mean value is considered to be
    threshold = (sum(temp_array) / len(temp_array)) + 0.2

    # Separate out the sentences that satiasfy the criteria of having a score above the threshold
    sentence_list = []
    if len(temp_array) > 1:
        for i in range(0, len(temp_array)):
            if temp_array[i] > threshold:
                sentence_list.append(sentence_array[i][1])
    else:
        sentence_list.append(sentence_array[0][1])

    model = sentence_list

    summary = " ".join(str(x) for x in sentence_list)

    return(summary)


# # save the data in another file, names sum.txt
# f = open('sum.txt', 'a+')
# # print(type(f))
# f.write('-------------------\n')
# f.write(summary)
# f.write('\n')

# f.close

# # End of the notebook
