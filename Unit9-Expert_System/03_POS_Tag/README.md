<Tag_POS.py>

from Tag_POS import get_pos_tags('ファイル名')

Enter the name of the text file you wish to run as an argument.
For example, if you want to specify "K1 dataset.txt", "K1" is also possible.
The program is designed to respond to the name of the text file if you enter some of the characters contained in the file name, so feel free to use it as you wish.
引数に実行したいテキストファイルの名前を入力してください。
例えば「K1 dataset.txt」を指定したいときは「K1」でも可能なようにしてあります。
テキストファイル名に含まれる一部の文字を入力すれば反応するようにしてあるので、自由にお使いください。

However, since there are "K1 dataset.txt" and "K2 dataset.txt" this time, just typing "K" will not respond.
ただし今回「K1 dataset.txt」、「K2 dataset.txt」があるので、「K」と入力しただけでは反応しません。

<count.py>

Returns the value and data name of the POS tag with the largest discrepancy.
```
from count import count

dev, unl_dict = count()
```
```
print(dev, unl_dict)
>> 0.9807692307692306, 'K2'
```
<Display_text.py>

14. allow the user to select any word or string and display the word or string in context essential
15. show 6 words before the target and 6 after the target word for each instance of the word in each dataset

The above functions have been implemented.
It can be checked by running the file.

<Display_pattern.py>

16. allow the user to search for POS patterns following the target word, e.g. absolutely + JJ essential

The above functions have been implemented.
It can be checked by running the file.
