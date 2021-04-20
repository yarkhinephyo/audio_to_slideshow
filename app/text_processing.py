import re
import nltk
from nltk.corpus import stopwords
import os

VALID_POS = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ',
             'JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS']

STOPWORDS = stopwords.words('english')


def get_expressions_removed(string):
    r = re.compile('%[\w]+')
    return r.sub('', string)


def get_pos_tags(string):
    tokenized = nltk.word_tokenize(string)
    tagged = nltk.pos_tag(tokenized)
    return tagged


def get_search_terms(pos_tags):
    """Given list of words with their POS tags, returns search terms with their positions.
    Assumption that if the POS tags are inside VALID_POS, the words are meaningful as search terms.

    Args:
        pos_tags (list): List of tuples ( <word> , <POS> )

    Returns:
        search_terms (list): List of tuples ( <position_int>, <search_term> )
    """
    len_pos_tags = len(pos_tags)
    search_terms = []
    skip = False
    for i in range(len_pos_tags):

        if skip:
            skip = False
            continue
        if (i < len_pos_tags - 1) and (pos_tags[i][1] in VALID_POS) and (pos_tags[i+1][1] in VALID_POS) \
                and (pos_tags[i][0] not in STOPWORDS) and (pos_tags[i+1][0] not in STOPWORDS):
            search_terms.append((i, pos_tags[i][0] + ' ' + pos_tags[i+1][0]))
            skip = True
        elif (pos_tags[i][1] in VALID_POS) and (pos_tags[i][0] not in STOPWORDS):
            search_terms.append((i, pos_tags[i][0]))
    return search_terms


def get_sentences(pos_tags, search_terms):
    """Given all words with their POS tags, and the positions of the search terms,
    return list of meaningful sentences.
    Note: In the case, POS tags are not of use

    Args:
        pos_tags (list): List of tuples ( <word> , <POS> )
        search_terms (list): List of tuples ( <position_int>, <search_term> )

    Returns:
        list: List of meaningful sentence strings
    """
    sentences = []
    for pos, search_term in search_terms:
        sentence = ''
        while True:
            sentence += ' ' + pos_tags.pop(0)[0]
            if search_term in sentence:
                sentences.append(sentence)
                break
    return sentences


def get_frame_durations(sentences, timestamps):
    """Given a list of sentences and timestamps of all words, return timestamps of each sentence

    Args:
        sentences (list): List of sentences
        timestamps (list): [
            [<word_string>, <start_time_float>, <end_time_float>],
            ...
        ]

    Returns:
        list: List of tuples ( <sentence> , <end_time_millisecond> )
    """
    i = 0
    durations = []
    previous = None

    for j, sentence in enumerate(sentences):
        words = sentence.split()
        word_timestamps = []
        for word in words:
            if word in timestamps[i][0]:
                word_timestamps.append(
                    (word, timestamps[i][1], timestamps[i][2]))
                i += 1

        if j == 0:
            duration = int(word_timestamps[-1][2] * 1000)
        else:
            duration = int((word_timestamps[-1][2] - previous)*1000)
        previous = word_timestamps[-1][2]
        durations.append((sentence, duration))

    return durations


if __name__ == '__main__':

    mysentence = "this is a test when I talk about dog does the video show pictures of dogs and cats if it does then I will celebrate"
    pos_tags = get_pos_tags(mysentence)
    search_terms = get_search_terms(pos_tags)
    sentences = get_sentences(pos_tags, search_terms)

    timestamps = [['this', 1.58, 1.79], ['is', 1.79, 1.89], ['a', 1.89, 1.98], ['test', 1.98, 2.32], ['when', 2.8, 2.97], ['I', 2.97, 3.03], ['talk', 3.03, 3.33], ['about', 3.33, 3.62], ['dog', 3.62, 4.03], ['does', 4.43, 4.66], ['the', 4.66, 4.82], ['video', 4.82, 5.23], [
        'show', 5.23, 5.51], ['pictures', 5.51, 6.03], ['of', 6.03, 6.21], ['dogs', 6.21, 6.65], ['and', 6.74, 6.96], ['cats', 7.22, 7.55], ['if', 8.04, 8.22], ['it', 8.22, 8.36], ['does', 8.36, 8.77], ['then', 9.02, 9.22], ['I', 9.22, 9.35], ['will', 9.35, 9.53], ['celebrate', 9.53, 10.13]]

    print(get_frame_durations(sentences, timestamps))
