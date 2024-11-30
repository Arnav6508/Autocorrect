from collections import Counter
import numpy as np
from operations import edit_one_letter, edit_two_letters

def get_count(word_l):
    return Counter(word_l)

def get_probs(word_count_dict):
    probs = {}
    tot = sum(word_count_dict.values())
    
    for key, value in word_count_dict.items():
        probs[key] = value/tot

    return probs

def get_corrections(word, probs, vocab, n = 2):

    suggestions = list((word in vocab and word) or edit_one_letter(word).intersection(vocab) or edit_two_letters(word).intersection(vocab))
    sugg_probs = [probs[sugg] for sugg in suggestions]

    n_best_idx = np.argsort(np.array(sugg_probs))[::-1][:n]
    n_best = [[suggestions[idx], probs[suggestions[idx]]] for idx in n_best_idx]

    return n_best