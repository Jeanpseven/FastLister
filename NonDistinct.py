# generate Non Distincts passwords combinations 
#!/usr/bin/python3
"""Wordlister, a simple wordlist generator and mangler written in python 3.10.1."""
# Written By Ananke: https://github.com/4n4nk3

import argparse
from copy import copy
from itertools import permutations
from sys import exit 

class Wordlister:
    LEET_TRANSLATIONS = str.maketrans('oOaAeEiIsS', '0044331155')

    def __init__(self, arguments):
        self.args = arguments
        self.wordlist = []


    def leet_and_append_and_prepend(self, line_leet: str) -> list:
        """
        Generator that returns the leeted version of a string and also returns it with applied prepend
        and append mutagens if required by user's parameters.

        :param line_leet: the string to be leeted
        :type line_leet: str
        :return result: list
        """

        line_leet = line_leet.translate(self.LEET_TRANSLATIONS)
        result: list = [line_leet + '\n',]
        if self.args.append is not None:
            result.append(f'{line_leet}{self.args.append}\n')
        if self.args.prepend is not None:
            result.append(f'{self.args.prepend}{line_leet}\n')
        return result


    def get_input_words(self, file_path: str) -> set:
        """
        Read input file and return a set of words containing them also capitalized and uppercased if needed.

        :param file_path: the path to the file with the user supplied wordlist
        :type file_path: str
        :return _: set
        """

        try:
            with open(file_path, 'r') as input_file:
                words = set(input_file.read().splitlines())
        except FileNotFoundError:
            print('Input file not found!\nExiting...\n')
            exit(1)
        
        # Apply capitalize mutagen and upper mutagen if needed
        prepped_words: set = copy(words)
        if self.args.cap is True or self.args.up is True:
            for word in words:
                if self.args.cap is True:
                    prepped_words.add(word.capitalize())
                if self.args.up is True:
                    prepped_words.add(word.upper())
                
        return prepped_words
    
    
    def printer(self, permutation: tuple):
        """
        Generate words from permutation applying append, prepend and, leet mutagens.
        The words are then added to the list which will contain all the generated words.

        :param perms: tuple containing a permutation of the word list that must be elaborated
        :type perms: tuple
        """
        
        if len(set(map(str.lower, permutation))) == len(permutation):
            line_printer = ''.join(permutation)
            if self.args.min <= len(line_printer) <= self.args.max:
                self.wordlist.append(line_printer + '\n')
                if self.args.append is not None and len(line_printer) + len(self.args.append) <= self.args.max:
                    self.wordlist.append(f'{line_printer}{self.args.append}\n')
                if self.args.prepend is not None and len(line_printer) + len(self.args.prepend) <= self.args.max:
                    self.wordlist.append(f'{self.args.prepend}{line_printer}\n')
                if self.args.leet is True:
                    self.wordlist.extend(self.leet_and_append_and
