class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)

    def match(self, word_list):
        matches = [word for word in word_list if sorted(word.lower()) == self.sorted_word and word.lower() != self.word]
        return matches
