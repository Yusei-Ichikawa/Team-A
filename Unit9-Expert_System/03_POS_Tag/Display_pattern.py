// Display_pattern.py

import os
from collections import Counter
from nltk.tokenize import word_tokenize
from Tag_POS import get_pos_tags

def display_pos_patterns(tagged_words, selected_word):
    pos_patterns = []
    for i in range(len(tagged_words) - 1):
        if tagged_words[i][0] == selected_word:
            pos_patterns.append(tagged_words[i + 1][1])
    pos_patterns_counter = Counter(pos_patterns)

    print("\n<part-of-speech pattern>")
    idx = 1
    for pattern, count in pos_patterns_counter.items():
        print(f"({idx}){selected_word} + {pattern}  x {count}")
        idx += 1

    print("\n")

def main():
    fileplace = 'Unit9/Datasets'
    filenames = [filename for filename in os.listdir(fileplace) if filename.endswith('.txt')]

    # Allow user to select email
    print("\n")
    for idx, filename in enumerate(filenames, start=1):
        print(f"{idx}: {filename}")
    print("\n")
    selected_idx = get_user_selection("Please select a mail by entering its index: ", len(filenames))
    selected_filename = filenames[selected_idx - 1]

    # Part-of-Speech Tagging
    tagged_words = get_pos_tags(selected_filename, fileplace)

    # Select a word
    selected_word = display_words_and_select(fileplace, selected_filename)

    # Show part-of-speech patterns following the selected word
    display_pos_patterns(tagged_words, selected_word)

def get_user_selection(prompt, max_index):
    while True:
        try:
            selected_idx = int(input(prompt))
            if 1 <= selected_idx <= max_index:
                return selected_idx
            else:
                print(f"Please enter a number between 1 and {max_index}.")
        except ValueError:
            print("Please enter a number.")

def display_words_and_select(fileplace, filename):
    with open(os.path.join(fileplace, filename), 'r') as file:
        text = file.read()

    # Get a list of words without symbols and numbers
    words = word_tokenize(text)
    unique_words = []
    for word in words:
        if word.isalpha() and word not in unique_words:
            unique_words.append(word)

    unique_words.sort()
    print("\n", ", ".join(unique_words))

    # Let the user select a word
    selected_word = input("Please select a word from the list above: ")

    if selected_word not in unique_words:
        print("Word not found in the list. Please run the program again.")
        exit()

    return selected_word

if __name__ == "__main__":
    main()
