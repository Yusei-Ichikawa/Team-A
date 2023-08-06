from wordFreq_KeywordFreq import count_word_frequency, CreateDict_SharedWords
from wordFreq_KeywordFreq import wordFreq, keywordFreq

##### word ferquecies: QとK1、QとK2の共通する単語数をそれぞれ出力する
########## (Output the number of words in common between Q and K1, and Q and K2 respectively)
##### keyword frequencies: QとK1、QとK2の共通する単語数をそれぞれ出力する
########## (Output the number of words in common between Q and K1, and Q and K2 respectively)
def main(num=1000):
    # Dataset Path
    path_Q = 'Q dataset.txt'
    path_K1 = 'K1 dataset.txt'
    path_K2 = 'K2 dataset.txt'

    # ファイル全体を text として読み込み
    f_Q = open(path_Q)
    f_K1 = open(path_K1)
    f_K2 = open(path_K2)
    dataset_Q = f_Q.read()
    dataset_K1 = f_K1.read()
    dataset_K2 = f_K2.read()

    # count, list and order the words
    dict_Q = count_word_frequency(dataset_Q)
    dict_K1 = count_word_frequency(dataset_K1)
    dict_K2 = count_word_frequency(dataset_K2)

    #### Comper with Q and K1 ####
    S_Dict1 = CreateDict_SharedWords(dict_Q, dict_K1, num)
    #S_List1 = list(S_Dict1)

    # Word Frequencies
    S_wf1 = wordFreq(S_Dict1)

    # Keyword Frequencies
    S_kw1 = keywordFreq(S_Dict1, S_wf1)


    #### Comper with Q and K2 ####
    S_Dict2 = CreateDict_SharedWords(dict_Q, dict_K2, num)
    #S_List2 = list(S_Dict2)

    # Word Frequencies
    S_wf2 = wordFreq(S_Dict2)

    # Keyword Frequencies
    S_kw2 = keywordFreq(S_Dict2, S_wf2)

    f_Q.close()
    f_K1.close()
    f_K2.close()

    return S_wf1, S_wf2, S_kw1, S_kw2


if __name__ == '__main__':

    print('Input reference corpus ->', end=' ')
    ReCorpus = input()

    # How to use main.py of worfFreq and keywordFreq.
    #### Word Frequecies and Keyword Frequecies ####
    ## Output
    ### List type variable of wordfreq and keywordfreq is wf, kw, respectively, and lsit length is n_.
    ### Q and K1 is 1, QとK2 is 2.
    ## Comper n_wf1 and n_wf2, n_kw1 and n_kw2.
    wf1, wf2, kw1, kw2 = main(int(ReCorpus))

    print(f'n_wf1:{len(wf1)}, n_kw1:{len(kw1)}, n_wf2:{len(wf2)}, n_kw2:{len(kw2)}')
    print('---------------------------------------')
    print('Word freq')
    print(f'wf1: {sorted(wf1.items(), key=lambda x: x[1], reverse=True)[:20]}')
    print(f'wf2{sorted(wf2.items(), key=lambda x: x[1], reverse=True)[:20]}')
    print('Keyword freq')
    print(f'kw1: {sorted(kw1.items(), key=lambda x: x[1], reverse=True)[:20]}')
    print(f'kw2: {sorted(kw2.items(), key=lambda x: x[1], reverse=True)[:20]}')

    # for k, v in kw2.items():
    #     if v <= 2:
    #         print(f'word: ({k}, {v})')
