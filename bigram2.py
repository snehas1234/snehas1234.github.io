import csv
import nltk
from nltk.corpus import gutenberg
from nltk.util import ngrams
from collections import Counter
import string
import itertools


nltk.download('gutenberg')
nltk.download('punkt')


def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return nltk.word_tokenize(text)


def get_common_elements(text):
    words = clean_text(text)
    word_freq = Counter(words).most_common(5)  
    bigrams = Counter(ngrams(words, 2)).most_common(5)  
    trigrams = Counter(ngrams(words, 3)).most_common(5)  
    return word_freq, bigrams, trigrams


def find_palindromes(text):
    words = set(clean_text(text))
    palindromes = [w for w in words if w == w[::-1] and len(w) > 1]
    return palindromes


def find_anagrams(text):
    words = set(clean_text(text))
    pairs = []
    for w1, w2 in itertools.combinations(words, 2):
        if sorted(w1) == sorted(w2):
            pairs.append((w1, w2))
    return pairs


def find_rhymes(text):
    words = set(clean_text(text))
    rhymes = {}
    for word in words:
        if len(word) > 2:
            ending = word[-3:]
            rhymes.setdefault(ending, []).append(word)
    return {k: v for k, v in rhymes.items() if len(v) > 1}


csv_path = r'C:\Users\user\Desktop\mvprlab1\text1.csv'

with open(csv_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)  
    csv_text = ' '.join(row[0] for row in reader)


print("Analysis for CSV File:")
words, bigrams, trigrams = get_common_elements(csv_text)
palindromes = find_palindromes(csv_text)
anagrams = find_anagrams(csv_text)
rhymes = find_rhymes(csv_text)


print(f"Most common words from the CSV file: {words}")
print(f"Most common bigrams from the CSV file: {bigrams}")
print(f"Most common trigrams from the CSV file: {trigrams}")
print(f"Palindrome words from the CSV file: {palindromes}")
print(f"Anagram pairs from the CSV file: {anagrams}")
print(f"Rhyming words from the CSV file: {rhymes}\n")


austen_text = gutenberg.raw('austen-emma.txt')
shakespeare_text = gutenberg.raw('shakespeare-hamlet.txt')


print("\nAnalysis for Austen's Emma:")
words, bigrams, trigrams = get_common_elements(austen_text)
palindromes = find_palindromes(austen_text)
anagrams = find_anagrams(austen_text)
rhymes = find_rhymes(austen_text)

print(f"Most common words from Austen's Emma: {words}")
print(f"Most common bigrams from Austen's Emma: {bigrams}")
print(f"Most common trigrams from Austen's Emma: {trigrams}")
print(f"Palindrome words from Austen's Emma: {palindromes}")
print(f"Anagram pairs from Austen's Emma: {anagrams}")
print(f"Rhyming words from Austen's Emma: {rhymes}\n")


print("\nAnalysis for Shakespeare's Hamlet:")
words, bigrams, trigrams = get_common_elements(shakespeare_text)
palindromes = find_palindromes(shakespeare_text)
anagrams = find_anagrams(shakespeare_text)
rhymes = find_rhymes(shakespeare_text)


print(f"Most common words from Shakespeare's Hamlet: {words}")
print(f"Most common bigrams from Shakespeare's Hamlet: {bigrams}")
print(f"Most common trigrams from Shakespeare's Hamlet: {trigrams}")
print(f"Palindrome words from Shakespeare's Hamlet: {palindromes}")
print(f"Anagram pairs from Shakespeare's Hamlet: {anagrams}")
print(f"Rhyming words from Shakespeare's Hamlet: {rhymes}\n")


