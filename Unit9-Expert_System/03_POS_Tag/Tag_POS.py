# Tag_POS.py

import os
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

def get_pos_tags(partial_filename, fileplace='Unit9-Expert_System/Datasets'):

    # ファイルが存在することを確認
    matching_files = [filename for filename in os.listdir(fileplace) if partial_filename in filename]
    if len(matching_files) > 1:
        raise ValueError("Error: Please specify the file more clearly.")
    elif not matching_files:
        raise FileNotFoundError(f"No such file or directory: '{partial_filename}'")

    filename = matching_files[0]

    with open(os.path.join(fileplace, filename), 'r', encoding="utf-8") as file:
        text = file.read()

    # テキストを単語に分割
    words = word_tokenize(text)

    # 各単語に品詞タグを付ける
    tagged_words = pos_tag(words)

    new_fileplace = 'Unit9-Expert_System/03_POS_Tag/POS_datasets'

    # 新しいディレクトリが存在しない場合、作成する
    if not os.path.exists(new_fileplace):
        os.makedirs(new_fileplace)

    # 空白をアンダーバーに変換した新しいファイル名を作成
    new_filename = "POS_" + filename.replace(" ", "_")

    # 新しいテキストファイルに出力
    with open(os.path.join(new_fileplace, new_filename), 'w', encoding="utf-8") as new_file:
            for word, pos in tagged_words:
                new_file.write(f"({word}, {pos}), ")

    return tagged_words
