from collections import defaultdict
import json

# Sample Corpus with More Words
corpus = [
    "low", "lowest", "new", "newer", "wider", "widest",
    "faster", "fastest", "slower", "slowest", "better", "best"
]

# Convert words into a list of character tokens
def split_into_chars(word):
    return list(word) + ['</w>']  # Adding end-of-word marker

# Tokenize each word in the corpus
tokenized_corpus = [split_into_chars(word) for word in corpus]
print("Initial Tokenized Corpus:", tokenized_corpus)

# Count occurrences of adjacent token pairs
def count_pairs(tokenized_corpus):
    pairs = defaultdict(int)
    for word in tokenized_corpus:
        for i in range(len(word) - 1):
            pairs[(word[i], word[i + 1])] += 1
    return pairs

# Merge the most frequent token pair
def merge_pair(pair, tokenized_corpus):
    new_tokenized_corpus = []
    for word in tokenized_corpus:
        new_word = []
        i = 0
        while i < len(word):
            if i < len(word) - 1 and (word[i], word[i + 1]) == pair:
                new_word.append(word[i] + word[i + 1])
                i += 2
            else:
                new_word.append(word[i])
                i += 1
        new_tokenized_corpus.append(new_word)
    return new_tokenized_corpus

# Store learned merges
merges = {}

# Merge most common pairs iteratively
num_merges = 10  # Increase the number of merges for better learning
for _ in range(num_merges):
    pairs = count_pairs(tokenized_corpus)
    if not pairs:
        break
    best_pair = max(pairs, key=pairs.get)
    tokenized_corpus = merge_pair(best_pair, tokenized_corpus)
    merges[best_pair] = best_pair[0] + best_pair[1]
    print(f"Merging: {best_pair} -> {tokenized_corpus}")

# Build final vocabulary
def extract_vocabulary(tokenized_corpus):
    vocab = set()
    for word in tokenized_corpus:
        vocab.update(word)
    return vocab

final_vocab = extract_vocabulary(tokenized_corpus)
print("Final Vocabulary:", final_vocab)

# Save vocabulary and merges for reuse
with open("bpe_vocab.json", "w") as vocab_file:
    json.dump(list(final_vocab), vocab_file, indent=4)

with open("bpe_merges.json", "w") as merge_file:
    json.dump(merges, merge_file, indent=4)

# Tokenize a new word using trained merges
def tokenize_word(word, merges):
    tokens = split_into_chars(word)
    while True:
        pairs = [(tokens[i], tokens[i + 1]) for i in range(len(tokens) - 1)]
        possible_merges = {pair: merges[pair] for pair in pairs if pair in merges}
        if not possible_merges:
            break
        best_pair = min(possible_merges, key=lambda p: list(merges.keys()).index(p))
        new_tokens = []
        i = 0
        while i < len(tokens):
            if i < len(tokens) - 1 and (tokens[i], tokens[i + 1]) == best_pair:
                new_tokens.append(merges[best_pair])
                i += 2
            else:
                new_tokens.append(tokens[i])
                i += 1
        tokens = new_tokens
    return tokens

# Test new word tokenization
new_word = "slowest"
tokenized_word = tokenize_word(new_word, merges)
print(f"Tokenized '{new_word}':", tokenized_word)
