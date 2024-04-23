# your code goes here!

class Anagram:

    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        matches = []
        sorted_word = sorted(self.word.lower())
        for word in word_list:
            if sorted(word.lower()) == sorted_word and word.lower() != self.word.lower():
                matches.append(word)
        return matches