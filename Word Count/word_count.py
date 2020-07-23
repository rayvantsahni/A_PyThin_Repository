import re
from collections import Counter

def count_words(path):
    with open(path) as file:
        all_words = re.findall(r"[0-9a-zA-z']+", file.read())
        all_words = [word.upper() for word in all_words]
        print("\nTotal number of words are:", len(all_words))
        
        word_counts = Counter()
        for word in all_words:
            word_counts[word] += 1
            
        print("\nTop most frequent words are-")
        for word in word_counts.most_common(20):
            print(word[0], "\t\t", word[1])
