"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    def __init__(self,path):
        self.path = path
        self.words=self.readfile()
        print(f'{len(self.words)} words read')
    def readfile (self):
        with open(self.path, "r") as file:
            return[line.strip() for line in file]
    def random (self):
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    def readfile(self):
        with open(self.path, "r") as file:
            return[line.strip() for line in file if line.strip() and not line.startswith('#')]
a = WordFinder('words.txt')
print(a.words[:25])
