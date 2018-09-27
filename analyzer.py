#!/usr/bin/env python3

from operator import itemgetter

def lines(current_file):
    text = read_file(current_file)
    print("Antal rader i filen " + current_file + ": " + str(len(text.split("\n"))))

def words(current_file):
    text = read_file(current_file)
    print("Antal ord i filen " + current_file + ": " + str(len(text.split(" "))))

def letters(current_file, output=True):
    text = read_file(current_file).lower()

    all_letters = "abcdefghijklmonpqrstuvwxyz"
    letter_count = 0
    for c in text:
        if c in all_letters:
            letter_count += 1

    if output:
        print("Antal bokstäver i filen " + current_file + ": " + str(letter_count))
    else:
        return letter_count

def word_frequency(current_file):
    text = read_file(current_file).lower()
    all_words = text.split(" ")
    number_of_words = len(all_words)
    words = {}

    for word in all_words:
        word = word.strip(",. \n")
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    print("Sju mest förekommande ord i texten:")
    for key, value in sorted(words.items(), key=itemgetter(1), reverse=True)[:7]:
        print(key + " " + str(round(100 * value / number_of_words, 2)) + " %")

def letter_frequency(current_file):
    text = read_file(current_file).lower()

    letter_count = letters(current_file, False)
    all_letters = "abcdefghijklmonpqrstuvwxyz"
    letter_dict = {}
    for c in text:
        if c in all_letters:
            if c in letter_dict:
                letter_dict[c] += 1
            else:
                letter_dict[c] = 1

    print("Sju mest förekommande bokstäver i texten:")
    for key, value in sorted(letter_dict.items(), key=itemgetter(1), reverse=True)[:7]:
        print(key + " " + str(round(100 * value / letter_count, 2)) + " %")


def all(current_file):
    lines(current_file)
    words(current_file)
    letters(current_file)
    word_frequency(current_file)
    letter_frequency(current_file)

def read_file(current_file):
    print()
    with open(current_file) as fh:
        return fh.read()
