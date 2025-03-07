# Tokenization Repository

with few features live on : https://tokenization.streamlit.app/

This repository explains and implements various tokenization techniques used in Natural Language Processing (NLP) and Large Language Models (LLMs). It also includes a Streamlit-based UI to demonstrate different tokenization methods.

## Contents

1. **Tokenization Explanation**: A detailed explanation of tokenization, its importance, and different techniques.
2. **BPE Implementation**: A Python implementation of Byte Pair Encoding (BPE) from scratch.
3. **Tokenization UI**: A Streamlit app to interactively tokenize text using different methods.

## How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/rupeshdev18/tokenizer.git
   cd tokenization-repo
   ```
   2. Install dependencies:

      On Linux/macOS:

      ```sudo
      sudo apt-get install build-essential cmake
      pip install -r requirements.txt
      ```
      On Windows (if facing issues with sentencepiece):

      ```bash
      choco install cmake
      pip install -r requirements.txt

      ```
   3. Run the streamlit app:

      ```
      bash
      streamlit run tokenization_ui.py
      ```
   4. Explore the code and explanations in the respective files.

   ### Files


   * `tokenization_explanation.md`: Detailed explanation of tokenization.
   * `bpe_implementation.py`: Implementation of Byte Pair Encoding (BPE).
   * `tokenization_ui.py`: Streamlit app for tokenization.
   * `requirements.txt`: List of dependencies.
