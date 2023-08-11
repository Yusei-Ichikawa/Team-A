import os
from collections import Counter
from nltk.tokenize import word_tokenize
from Tag_POS import get_pos_tags

def display_pos_patterns(tagged_words, selected_word):
    pos_patterns = []
    for i in range(len(tagged_words) - 1):
        word, pattern = tagged_words[i][0], tagged_words[i + 1][1]
        if word == selected_word:
            pos_patterns.append(pattern)
    pos_patterns_counter = Counter(pos_patterns)

    print("\n<part-of-speech pattern>")
    idx = 1
    for pattern, count in pos_patterns_counter.items():
        print(f"({idx}){selected_word} + {pattern}  x {count}")
        idx += 1

    print("\n")
    return pos_patterns_counter

def save_all_pos_patterns(tagged_words, filename):
    pos_patterns = []
    for i in range(len(tagged_words) - 1):
        word, next_pos = tagged_words[i][0], tagged_words[i + 1][1]
        if word.isalpha():
            pos_patterns.append((word, next_pos))
    pos_patterns_counter = Counter(pos_patterns)

    pattern_list = []

    # Creation of directories
    new_fileplace = 'Unit9-Expert_System/POSpattern_Datasets'
    if not os.path.exists(new_fileplace):
        os.makedirs(new_fileplace)

    # Create File Name
    new_filename = "POSpattern_" + filename.replace(" ", "_")

    # Creating and Writing Files
    with open(os.path.join(new_fileplace, new_filename), 'w') as new_file:
        for (word, pattern), count in pos_patterns_counter.items():
            pattern_tuple = (word, pattern, count)
            pattern_list.append(pattern_tuple)

        # ファイルにリスト形式で書き込み
        new_file.write(str(pattern_list))

    return pattern_list

def main():
    fileplace = 'Unit9-Expert_System/Datasets'
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

    # Save all part-of-speech patterns to a file
    save_all_pos_patterns(tagged_words, selected_filename)


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
