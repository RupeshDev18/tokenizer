import streamlit as st
from transformers import AutoTokenizer
import tiktoken
from nltk.tokenize import word_tokenize
import nltk


nltk.download('punkt')

# Title
st.title("Tokenization Techniques")

# Dropdown for tokenization methods
tokenization_method = st.selectbox(
    "Choose a Tokenization Method",
    ["Byte-Pair Encoding (BPE)", "WordPiece", "Unigram LM"]
)

# Input text
text = st.text_area("Enter text to tokenize", "Hello, world!")

# Tokenize based on selected method
# if tokenization_method == "Word Tokenization":
#     tokens = word_tokenize(text)
# el

if tokenization_method == "Byte-Pair Encoding (BPE)":
    enc = tiktoken.get_encoding("cl100k_base")
    tokens = enc.encode(text)
elif tokenization_method == "WordPiece":
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    tokens = tokenizer.tokenize(text)
elif tokenization_method == "Unigram LM":
    from sentencepiece import SentencePieceProcessor
    sp = SentencePieceProcessor(model_file="t5-spiece.model")
    tokens = sp.encode(text, out_type=str)

# Display tokens
st.write("Tokens:", tokens)