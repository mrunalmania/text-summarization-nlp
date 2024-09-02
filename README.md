# Text Summarization Project

This repository contains multiple implementations of text summarization using different Natural Language Processing (NLP) techniques. The primary focus is on providing concise summaries of input text by leveraging popular Python libraries such as NLTK, SpaCy, and Gensim.

### Table of Contents
- [Usage](#usage)
- [Overview](#overview)
- [File Descriptions](#file-descriptions)
- [Contributing](#contributing)
- [License](#license)

### Usage

Each script can be executed individually to summarize text using different approaches. Here are some examples:

1. **Gensim Summarization:**

   ```python
   from gensim_summarization import summarize_text

   text = """Your input text here..."""
   summary = summarize_text(text)
   print(summary)
   ```

2. **NLTK Summarization:**

   ```python
   from nltk_summarization import nltk_summarizer

   text = """Your input text here..."""
   summary = nltk_summarizer(text)
   print(summary)
   ```

3. **SpaCy Summarization:**

   ```python
   from spacy_summarization import text_summarizer

   text = """Your input text here..."""
   summary = text_summarizer(text)
   print(summary)
   ```

### Overview

Text summarization is a crucial task in NLP, aiming to condense large volumes of text into shorter versions while preserving the key information. This project explores three different methods to achieve this goal:

- **Gensim Summarization:** Leverages the TextRank algorithm, an unsupervised approach, to rank sentences by their significance.
- **NLTK Summarization:** Uses word frequency to score sentences, with the highest-scoring sentences forming the summary.
- **SpaCy Summarization:** Implements a similar approach to NLTK but with SpaCy’s advanced NLP capabilities for better tokenization and sentence segmentation.

### File Descriptions

- **gensim_summarization.py:** Implements text summarization using the Gensim library's built-in summarizer based on the TextRank algorithm.
- **nltk_summarization.py:** Provides a custom text summarizer using NLTK, focusing on word frequency and sentence scoring.
- **spacy_summarization.py:** Uses SpaCy to perform text summarization, with a focus on leveraging SpaCy’s NLP pipeline for better processing and summarization.

### Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
