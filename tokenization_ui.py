import streamlit as st
from transformers import AutoTokenizer
import tiktoken
from sentencepiece import SentencePieceProcessor

# Custom Styling
st.markdown("""
    <style>
    .token-box {
        border: 1px solid #ddd; 
        padding: 10px; 
        border-radius: 5px; 
        background-color: #f9f9f9;
        text-align: center;
    }
    .token {
        display: inline-block;
        padding: 5px 8px;
        margin: 3px;
        background-color: #e6f7ff;
        border-radius: 4px;
        font-weight: bold;
        color: #333;
    }
    .token-id {
        display: inline-block;
        padding: 5px 8px;
        margin: 3px;
        color: #666;
        font-weight: bold;
        background-color: #f0f0f0;
        border-radius: 4px;
    }
    .centered {
        display: flex; 
        justify-content: center; 
        align-items: center;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🔠 Tokenization Techniques")

st.write("This tool demonstrates different tokenization methods used in NLP and LLMs.")

# Dropdown for tokenization methods
tokenization_method = st.selectbox(
    "Select a Tokenization Method:",
    ["Byte-Pair Encoding (BPE)", "WordPiece", "Unigram LM"]
)

# Input text area
text = st.text_area("Enter text to tokenize:", "Hello, world! 👋")

tokens, token_ids = [], []

# Tokenization Logic
if text.strip():  # Ensure non-empty input
    if tokenization_method == "Byte-Pair Encoding (BPE)":
        enc = tiktoken.get_encoding("cl100k_base")
        token_ids = enc.encode(text)
        tokens = [enc.decode_single_token_bytes(tid).decode('utf-8', errors='replace') for tid in token_ids]
        
    elif tokenization_method == "WordPiece":
        tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        tokens = tokenizer.tokenize(text)
        token_ids = tokenizer.convert_tokens_to_ids(tokens)
        
    elif tokenization_method == "Unigram LM":
        sp = SentencePieceProcessor()
        sp.load("spiece.model")  # Ensure model file exists
        tokens = sp.encode_as_pieces(text)
        token_ids = sp.encode_as_ids(text)

    # Display tokens & IDs in two columns
    st.subheader("🔹 Tokenization Results")
    col1, col2 = st.columns([2, 3])

    with col1:
        st.markdown("**Tokens:**")
        token_str = "".join([f"<span class='token'>{t}</span>" for t in tokens])
        st.markdown(f"<div class='token-box'>{token_str}</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("**Token IDs:**")
        id_str = "".join([f"<span class='token-id'>{tid}</span>" for tid in token_ids])
        st.markdown(f"<div class='token-box'>{id_str}</div>", unsafe_allow_html=True)

else:
    st.warning("⚠️ Please enter some text to tokenize!")

# Footer
st.markdown("<br><hr><small class='centered'>Built with ❤️ using Streamlit</small>", unsafe_allow_html=True)
