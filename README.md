# Query Document Processing Project

## Description
This project focuses on processing query and document texts using Python and the Natural Language Toolkit (nltk) library. The main goal is to prepare the texts for information retrieval tasks by performing several preprocessing steps, including tokenization, punctuation removal, conversion to lowercase, removal of stopwords, and stemming. The project includes two main scripts (`lab3.py` and `lab3.5.py`) that process document texts and query texts respectively.

### Files Included
- **lab3.py**: A Python script for processing document texts.
- **lab3.5.py**: A Python script for processing query texts.
- **npl.tar.gz**: A compressed file containing additional data required for the scripts.

### Notable Code Snippets

#### 1. Reading and Tokenizing Text (lab3.py)
This snippet reads the content of `doc-text` and tokenizes the text using the `nltk` library.

```python
import os
import nltk
nltk.download('punkt')

# Path to the input file
input_file = r'C:\Users\mini_\OneDrive\Documentos\Code Test\TEST 1\lab3\npl\doc-text'

# Read the content of the external file
with open(input_file, 'r', encoding='utf-8') as archivo:
    texto = archivo.read()

# Tokenization using NLTK
palabras = nltk.word_tokenize(texto)
```
#### 2. Removing Punctuation (lab3.py)

This snippet defines a regular expression to remove punctuation from the tokenized text.

```python
import re
import string

# Define regular expression to remove punctuation
simbolos_extra = '’'
re_punc = re.compile('[%s%s]' % (re.escape(string.punctuation), re.escape(simbolos_extra)))

# Replace "|" with space and remove other punctuation
stripped = re_punc.sub(lambda x: ' ' if x.group(0) == '|' else '', texto)
```

#### 3. Stemming and Lemmatization (lab3.5.py)

This snippet demonstrates the use of PorterStemmer to stem the cleaned text.

```python
from nltk.stem.porter import PorterStemmer

# Stemming with PorterStemmer
stemmer = PorterStemmer()

# Split content into lines
lines = filtered_words.split('\n')

# Stem words in each line
stemmed_lines = []
for line in lines:
    # Split line into words
    words = line.split()
    # Apply stemmer to each word
    stemmed_words = [stemmer.stem(word) for word in words]
    # Join stemmed words into a new line
    stemmed_line = ' '.join(stemmed_words)
    # Add stemmed line to list
    stemmed_lines.append(stemmed_line)

# Join stemmed lines into a single document
stemmed_content = '\n'.join(stemmed_lines)
```

### Installation and Usage

1.  Clone the repository to your local machine.
2.  Ensure you have Python and `nltk` installed.
3.  Extract the `npl.tar.gz` file to obtain the required data files.
4.  Run the `lab3.py` script to process document texts.
5.  Run the `lab3.5.py` script to process query texts.

```bash
git clone https://github.com/KPlanisphere/query-document-processing.git
cd query-document-processing
tar -xzf npl.tar.gz
python lab3.py
python lab3.5.py
```

### Dependencies

-   Python
-   NLTK library