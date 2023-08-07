# TODO
# count the number of identical POS patterns in each dataset
# identify the least similiar dataset based on the number of identical POS patterns with questionned dataset
# suggest ruling out the least similiar dataset

from Tag_POS import get_pos_tags

# nltkの全タグ
tag_list = tuple(
    [
        "$",
        "''",
        "(",
        ")",
        ",",
        "--",
        ".",
        ":",
        "CC",
        "CD",
        "DT",
        "EX",
        "FW",
        "IN",
        "JJ",
        "JJR",
        "JJS",
        "LS",
        "MD",
        "NN",
        "NNP",
        "NNPS",
        "NNS",
        "PDT",
        "POS",
        "PRP",
        "PRP$",
        "RB",
        "RBR",
        "RBS",
        "RP",
        "SYM",
        "TO",
        "UH",
        "VB",
        "VBD",
        "VBG",
        "VBN",
        "VBP",
        "VBZ",
        "WDT",
        "WP",
        "WP$",
        "WRB",
        "``",
    ]
)


# POSタグとその数を名前付きで保存
class Dataset:
    def __init__(self, name, pn_dict):
        self.name = name
        self.pn_dict = pn_dict


# それぞれのPOSタグ数をカウント
def count_pos(tagged: list):
    pn_dict = {}
    for tp in tagged:
        if tp[1] in pn_dict.keys():
            pn_dict[tp[1]] += 1
        else:
            pn_dict[tp[1]] = 1
    return pn_dict


# 2つのデータの(各タグ数/総トークン数)を比較
# ズレの総和を返す
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
# 対象と既存データセットを比較、類似度が最も低いデータ名とズレの値を返す
def find_unlikely(dsq: Dataset, **kwargs: Dataset):
    max_dev = 0
    unl_dict = None
    tnq = 0
    for v in dsq.pn_dict.values():
        tnq += v
    for ds in kwargs.values():
        tn = 0
        for v in ds.pn_dict.values():
            tn += v
        dev = compare_pos(dsq.pn_dict, tnq, ds.pn_dict, tn)
        if dev > max_dev:
            max_dev = dev
            unl_dict = ds.name
    return max_dev, unl_dict


# 以上を実行する
def count():
    taggedq = get_pos_tags("Q dataset.txt")
    tagged1 = get_pos_tags("K1 dataset.txt")
    tagged2 = get_pos_tags("K2 dataset.txt")

    pn_dict_q = count_pos(taggedq)
    pn_dict_1 = count_pos(tagged1)
    pn_dict_2 = count_pos(tagged2)

    dsq = Dataset("Q", pn_dict_q)
    ds1 = Dataset("K1", pn_dict_1)
    ds2 = Dataset("K2", pn_dict_2)

    return find_unlikely(dsq=dsq, ds1=ds1, ds2=ds2)
