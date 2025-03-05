from collections import defaultdict

corpus = [
    "low",
    "lowest",
    "new",
    "newer",
    "wider",
    "widest",
]

# Convert words into a list of character tokens
def split_into_chars(word):
    return list(word)

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

pairs = count_pairs(tokenized_corpus)
print("Initial Token Pairs:", pairs)

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

# Merge most common pairs iteratively
num_merges = 5
for _ in range(num_merges):
    pairs = count_pairs(tokenized_corpus)
    if not pairs:
        break
    best_pair = max(pairs, key=pairs.get)
    tokenized_corpus = merge_pair(best_pair, tokenized_corpus)
    print(f"Merging: {best_pair} -> {tokenized_corpus}")

# Build the final vocabulary
def extract_vocabulary(tokenized_corpus):
    vocab = set()
    for word in tokenized_corpus:
        vocab.update(word)
    return vocab

final_vocab = extract_vocabulary(tokenized_corpus)
print("Final Vocabulary:", final_vocab)

# Tokenize a new word using the trained vocabulary
def tokenize_word(word, vocab):
    tokens = split_into_chars(word)
    i = 0
    while i < len(tokens) - 1:
        bigram = (tokens[i], tokens[i + 1])
        if "".join(bigram) in vocab:
            tokens[i] = "".join(bigram)
            tokens.pop(i + 1)  # Remove the second character after merging
        else:
            i += 1
    return tokens

# Test with a new word
new_word = "newest"
tokenized_word = tokenize_word(new_word, final_vocab)
print(f"Tokenized '{new_word}':", tokenized_word)