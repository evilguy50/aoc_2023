import re

def replace_words_with_numbers(word: str):
    replacements = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    new_word = word
    if not re.match('\d', word):
        new_word = replacements[word]
    return new_word