# TODO
# count the number of identical POS patterns in each dataset
# identify the least similiar dataset based on the number of identical POS patterns with questionned dataset
# suggest ruling out the least similiar dataset

from Tag_POS import get_pos_tags
from Display_pattern import save_all_pos_patterns


# 辞書化したパターンを名前付きで保存
class Dataset:
    def __init__(self, name, pn_dict):
        self.name = name
        self.pn_dict = pn_dict


# リストを辞書型に変換
def convdict(patterns: list):
    pdict = {}
    for p in patterns:
        ptpl = tuple([p[0], p[1]])
        pdict[ptpl] = p[2]
    return pdict


# 2つのデータの(各パターン数/総数)を比較
# ズレの総和を返す
def compare_pattern(pnd1: dict, pn1: int, pnd2: dict, pn2: int):
    dev = 0
    pnd2_cp = dict(pnd2)
    for p in pnd1.keys():
        if p in pnd2_cp.keys():
            norm1 = pnd1[p] / pn1
            norm2 = pnd2_cp.pop(p) / pn2
            pdev = norm2 - norm1 if norm1 < norm2 else norm1 - norm2
            dev += pdev
    for pn in pnd2_cp.values():
        dev += pn / pn2
    return dev


# kwargs == ds1:Dataset, ds2:Dataset,...
# 対象と既存データセットを比較、類似度が最も低いデータ名とズレの値を返す
def find_unlikely(dsq: Dataset, **kwargs: Dataset):
    max_dev = 0
    unl_dict = None
    pnq = 0
    for v in dsq.pn_dict.values():
        pnq += v
    for ds in kwargs.values():
        pn = 0
        for v in ds.pn_dict.values():
            pn += v
        dev = compare_pattern(dsq.pn_dict, pnq, ds.pn_dict, pn)
        if dev > max_dev:
            max_dev = dev
            unl_dict = ds.name
    return max_dev, unl_dict


# 以上を実行する
def compare():
    taggedq = get_pos_tags("Q dataset.txt")
    tagged1 = get_pos_tags("K1 dataset.txt")
    tagged2 = get_pos_tags("K2 dataset.txt")

    plist_q = save_all_pos_patterns(taggedq, "Q.txt")
    plist_1 = save_all_pos_patterns(tagged1, "K1.txt")
    plist_2 = save_all_pos_patterns(tagged2, "K2.txt")

    pdict_q = convdict(plist_q)
    pdict_1 = convdict(plist_1)
    pdict_2 = convdict(plist_2)

    dsq = Dataset("Q", pdict_q)
    ds1 = Dataset("K1", pdict_1)
    ds2 = Dataset("K2", pdict_2)

    return find_unlikely(dsq=dsq, ds1=ds1, ds2=ds2)

print(compare())