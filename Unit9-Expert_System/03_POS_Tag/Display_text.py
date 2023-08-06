// Display_text.py

import os
from nltk.tokenize import word_tokenize
from Tag_POS import get_pos_tags

def display_words_and_select(fileplace, filename):
    with open(os.path.join(fileplace, filename), 'r') as file:
        text = file.read()

    words = word_tokenize(text)
    unique_words = []
    for word in words:
        if word.isalpha() and word not in unique_words:
            unique_words.append(word)

    unique_words.sort()
    print("\n", ", ".join(unique_words))

    selected_word = input("Please select a word from the list above: ")
    if selected_word not in unique_words:
        print("Word not found in the list. Please run the program again.")
        exit()

    return selected_word

def display_sentences_with_word(fileplace, filename, word):
    with open(os.path.join(fileplace, filename), 'r') as file:
        text = file.read()

    words = word_tokenize(text)
    count = 0
    print("\n<Locations used>")
    for idx, w in enumerate(words):
        if w == word:
            count += 1
            start_idx = max(0, idx - 6)
            end_idx = min(len(words), idx + 7)
            context = " ".join(words[start_idx:end_idx]).replace(word, f'"{word}"')
            print(f"({count}) {context}")

    print(f"\nThe word '{word}' is used {count} times.")

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

def main():
    fileplace = 'Unit9/Datasets'
    filenames = [filename for filename in os.listdir(fileplace) if filename.endswith('.txt')]

    print("\n")
    for idx, filename in enumerate(filenames, start=1):
        print(f"{idx}: {filename}")
    print("\n")
    selected_idx = get_user_selection("Enter a number and select Email：", len(filenames))
    selected_filename = filenames[selected_idx - 1]

    tagged_words = get_pos_tags(selected_filename, fileplace)
    selected_word = display_words_and_select(fileplace, selected_filename)
    display_sentences_with_word(fileplace, selected_filename, selected_word)

if __name__ == "__main__":
    main()
