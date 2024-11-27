# Authors: Kacper Kuźnik 160299, Piotr Foltyniewicz 160295

import random

# approximation of letters based on previous letters
def markov_source(text, order):
    probabilities = {'total': 0} # t -> total children

    # fill structure with counts of letters
    def traverse(dict, letters, n, order):
        if n > order:
            return
        if n >= len(letters):
            return
        l = letters[n]
        if l in dict:
            dict[l][0] += 1
            dict['total'] += 1
        else:
            dict[l] = [1, {'total': 0}]
            dict['total'] += 1
        traverse(dict[l][1], letters, n + 1, order)
        
    for i in range(len(text) - 1, -1, -1):
        traverse(probabilities, text[i: i + order + 1], 0, order)

    # convert counts to probabilities
    def traverse_change(dict):
        if 'total' not in dict:
            return
        total = dict['total']
        del dict['total']
        for key in dict:
            dict[key][0] /= total
            traverse_change(dict[key][1])
            if len(dict[key][1]) == 0:
                del dict[key][1]
    
    traverse_change(probabilities)
    return probabilities

def get_pop_and_weights(dict, seq):
    # traverse to proper dict in structure and then return data for random.choices
    for c in seq:
        if c in dict:
            if len(dict[c]) == 1:
                return None, None
            dict = dict[c][1]
        else:
            return None, None
        
    population = list(dict.keys())
    weights = [dict[key][0] for key in dict]

    return population, weights

def generate_markov_text(source, max_order, length, start=''):
    with open(source) as f:
        probabilities = markov_source(f.read(), max_order)
        curr_order = min(len(start), max_order)
        text = start
        i = len(start)
        while i < length:
            seq = text[i - curr_order:i]
            population, weights = get_pop_and_weights(probabilities, seq)
            # if algorithm cannot generate letter in current order, then decrement order by one and try again
            if population is None:
                curr_order -= 1
                continue
            text += random.choices(population=population, weights=weights)[0]
            curr_order = min(curr_order + 1, max_order)
            i += 1
        return text
    
def calculate_avg_word_len(text):
    words =  text.split(" ")
    return sum([len(i) for i in words ]) / len(words)

# Task 1
# Generate using first-order

text1 = generate_markov_text("norm_hamlet.txt", 1, 300)
avg_word1 = calculate_avg_word_len(text1)
print(text1)
print("Average word length: ", avg_word1)
print()

# Task 2
# Generate using third-order
text2 = generate_markov_text("norm_hamlet.txt", 3, 300)
avg_word2 = calculate_avg_word_len(text2)
print(text2)
print("Average word length: ", avg_word2)
print()

# Task 3
# Generate using fifth-order and startwing with 'probability'
text3 = generate_markov_text("norm_hamlet.txt", 5, 300, start='probability')
avg_word3 = calculate_avg_word_len(text3)
print(text3)
print("Average word length: ", avg_word3)
print()
