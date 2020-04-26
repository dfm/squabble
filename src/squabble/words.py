# -*- coding: utf-8 -*-

# __all__ = []

import pkg_resources


with open(
    pkg_resources.resource_filename(__name__, "data/distribution.txt"), "r"
) as f:
    LETTERS = f.read().replace("\n", "")


def check_anagram(word1: str, word2: str) -> bool:
    return sorted(word1) == sorted(word2)


if __name__ == "__main__":
    word1 = "face"
    word2 = "cfae "
    print(check_anagram(word1, word2))
