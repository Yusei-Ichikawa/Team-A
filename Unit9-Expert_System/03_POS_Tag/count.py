# TODO
# count the number of identical POS patterns in each dataset
# identify the least similiar dataset based on the number of identical POS patterns with questionned dataset
# suggest ruling out the least similiar dataset

import nltk
tag_list = tuple(["$", "''", "(", ")", ",", "--", ".", ":", "CC", "CD", "DT", 
                 "EX", "FW", "IN", "JJ", "JJR", "JJS", "LS", "MD", "NN", "NNP", 
                 "NNPS", "NNS", "PDT", "POS", "PRP", "PRP$", "RB", "RBR", "RBS", 
                 "RP", "SYM", "TO", "UH", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ",
                 "WDT", "WP", "WP$", "WRB", "``"])
# following will be overwritten when tagging is completed
sentence = """At eight o'clock on Thursday morning 
            Arthur didn't feel very good."""
tokens = nltk.word_tokenize(sentence)
sentence = """identify the least similiar dataset based on 
            the number of identical POS patterns with questionned dataset"""
tokens_2 = nltk.word_tokenize(sentence)

tagged_1 = nltk.pos_tag(tokens)
tagged_2 = nltk.pos_tag(tokens_2)
tagged_q = nltk.pos_tag(tokens)

class Dataset:
    def __init__(self, name, pn_dict):
        self.name = name
        self.pn_dict = pn_dict

def count_pos(tagged: list):
    pn_dict = {}
    for tp in tagged:
        if tp[1] in pn_dict.keys():
            pn_dict[tp[1]] += 1
        else:
            pn_dict[tp[1]] = 1
    return pn_dict


pn_dict_1 = count_pos(tagged_1)
pn_dict_2 = count_pos(tagged_2)
pn_dict_q = count_pos(tagged_q)

ds1 = Dataset("K1", pn_dict_1)
ds2 = Dataset("K2", pn_dict_2)
dsq = Dataset("Q", pn_dict_q)

def compare_pos(pn1: dict, tn1: int, pn2: dict, tn2: int):
    dev = 0
    for tag in tag_list:
        if tag not in pn1.keys() and tag not in pn2.keys():
            continue
        elif tag not in pn1.keys():
            dev += pn2[tag] / tn2
        elif tag not in pn2.keys():
            dev += pn1[tag] / tn1
        else:
            norm1 = pn1[tag] / tn1
            norm2 = pn2[tag] / tn2
            pdev = norm2 - norm1 if norm1 < norm2 else norm1 - norm2
            dev += pdev
    return dev

# kwargs == ds1:Dataset, ds2:Dataset,...
def find_unlikely(pnq: dict, tnq: int, **kwargs):
    max_dev = 0
    unl_dict = None
    for ds in kwargs.values():
        tn = 0
        for v in ds.pn_dict.values():
            tn += v
        dev = compare_pos(pnq, tnq, ds.pn_dict, tn)
        if dev > max_dev:
            max_dev = dev
            unl_dict = ds.name
    print(unl_dict)

find_unlikely(pn_dict_q, len(tokens), ds1=ds1, ds2=ds2)