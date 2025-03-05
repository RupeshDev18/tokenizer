# Tokenization Explained

## What is Tokenization?

Tokenization is the process of breaking down text into smaller units (tokens) so that a machine can process it. In Large Language Models (LLMs), tokenization is the first step before training or inference.

### Example:

- **Text**: "I love AI!"
- **Tokens (word-based)**: ["I", "love", "AI", "!"]
- **Tokens (character-based)**: ["I", " ", "l", "o", "v", "e", " ", "A", "I", "!"]
- **Tokens (subword-based)**: ["I", "love", "A", "I", "!"]

## Why is Tokenization Important?

1. **Reduces Model Complexity**: Instead of handling raw text, models process numbers (tokens mapped to IDs).
2. **Improves Efficiency**: Splitting text into meaningful units makes training and inference faster.
3. **Handles Different Languages**: Different tokenization methods can handle English, Chinese, and multilingual text efficiently.

## Types of Tokenization

### 1. Word-Based Tokenization

Splits text by spaces or punctuation.

**Example**:

- "I love LLMs!" → ["I", "love", "LLMs", "!"]

**Issues**:

- Fails with words like "don't" (should be ["do", "n't"]).
- Struggles with rare words (e.g., "antidisestablishmentarianism").

### 2. Character-Based Tokenization

Treats every character as a token.

**Example**:

- "AI is cool!" → ["A", "I", " ", "i", "s", " ", "c", "o", "o", "l", "!"]

**Issues**:

- Too many tokens → longer sequences → inefficient for large models.

### 3. Subword-Based Tokenization (Most Common in LLMs)

Breaks words into frequently used subwords.

**Example**:

- "I love tokenization!" → ["I", "love", "token", "ization", "!"]

**Why?**

- Handles rare words better.
- Efficient in terms of model size and training.

**Techniques**:

- **Byte Pair Encoding (BPE)**: Used in OpenAI models like GPT-3/4.
- **WordPiece**: Used in BERT and Google’s models.
- **Unigram LM (SentencePiece)**: Used in Llama and other multilingual models.

## Byte Pair Encoding (BPE) – How It Works

BPE is a subword tokenization algorithm that helps LLMs efficiently break down words into smaller, reusable pieces.

### Why BPE?

- Handles rare words better.
- Reduces vocabulary size while keeping meaningful subwords.
- Improves generalization.

### How BPE Works (Step by Step)

1. **Initialize Tokens**: Split words into individual characters.
2. **Count Token Pairs**: Find the most frequent adjacent character pairs.
3. **Merge the Most Frequent Pair**: Combine the most frequent pair into a new token.
4. **Repeat**: Continue merging until the vocabulary size is reached.

---

## Code Implementation

See `bpe_implementation.py` for a Python implementation of BPE.
