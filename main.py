import pickle
from preprocess import preprocess
from utils import get_count, get_probs, get_corrections

def build_model(file_name):
    word_l = preprocess(file_name)
    vocab = set(word_l)
    word_count_dict = get_count(word_l)
    probs = get_probs(word_count_dict)

    model_weights = {
        'vocab': vocab,
        'probs': probs
    }

    with open('model.pkl', 'wb') as file:
        pickle.dump(model_weights, file)

def predict_correction(word, n = 2):
    with open('model.pkl', 'rb') as file:
        model_weights = pickle.load(file)
    
    vocab = model_weights['vocab']
    probs = model_weights['probs']

    suggestions = get_corrections(word, probs, vocab, n)

    for word, prob in suggestions:
        print(word,":",prob)

    return suggestions