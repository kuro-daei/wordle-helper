# coding: UTF-8
import argparse
import re

# check args
parser = argparse.ArgumentParser(description="wordle helper")
parser.add_argument(
    "pattern",
    type=str,
    help="regex. ex) ..r.h",
)
parser.add_argument(
    "ignore_chars", type=str, help="ignore chars. ex) abcz", nargs="?", default="-"
)
args = parser.parse_args()

# read the dictionary
words = []
with open("words_alpha.txt", "r") as file:
    for i in file.read().splitlines():
        if len(i) != 5:
            continue
        words.append(i)

#
for word in words:
    if re.match(args.pattern, word) and re.match(
        "^[^" + args.ignore_chars + "]+$", word
    ):
        print(word)
