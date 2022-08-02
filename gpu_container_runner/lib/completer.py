"""
ターミナルからshellを利用するときのように、tab入力で autocompletion を行うためのモジュール
ex)
import readline
from {$PATH}.completer import Completer

readline.parse_and_bind("tab: complete")
words = ['a', 'b']
completer = Completer(words)
readline.set_completer(completer.complete)
input()
"""
from typing import List


class Completer:
    def __init__(self, words: List[str]):
        self.words = words
        self.prefix = None

    def complete(self, prefix, index):
        if prefix != self.prefix:
            self.matching_words = [w for w in self.words if w.startswith(prefix)]
            self.prefix = prefix
        try:
            return self.matching_words[index]
        except IndexError:
            return None
