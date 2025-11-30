# ♠️ SPADE: Intelligent Email Spam Detection System

**SPADE** (Spam Analysis & Detection Engine) is a machine learning-powered web application designed to identify and classify spam communications with high precision. Beyond simple classification, SPADE provides granular insights by extracting critical entities (financial figures, dates, and organizations) to help users understand *why* a message might be suspicious.

---

## 🚀 Project Overview

In the era of digital communication, phishing and spam remain significant threats. SPADE addresses this by combining **Natural Language Processing (NLP)** for text analysis with a **Support Vector Machine (SVM)** classifier.

The system features a modern, responsive web interface that delivers:
1.  **Binary Classification:** Instantly categorizes messages as "Legitimate" (Ham) or "Spam."
2.  **Confidence Scoring:** Displays the probability percentage of the prediction.
3.  **Smart Insights:** Uses Regex logic to extract actionable data points (e.g., urgent dates, large money requests) often found in social engineering attacks.

---

## 🛠️ Tech Stack

### Core & Backend
* **Python 3.11+**: Primary programming language.
* **Flask**: Web framework for serving the application and API endpoints.
* **Pickle**: For model serialization and loading.

### Machine Learning & NLP
* **Scikit-Learn**: Implements the SVM algorithm and TF-IDF vectorization.
* **NLTK**: Handles text preprocessing (tokenization, stemming, stopword removal).
* **Pandas & NumPy**: Data manipulation and numerical operations.
* **Re (Regex)**: Pattern matching for entity extraction.

### Frontend
* **HTML5 / CSS3**: Responsive dashboard design.
* **Jinja2**: Templating engine for dynamic content rendering.

---

## 📊 Dataset & Preprocessing

The model was trained on the **SMS Spam Collection dataset** (`spam.csv`).

### Data Pipeline
1.  **Cleaning**: Removal of noise (URLs, punctuation, special characters).
2.  **Normalization**: Lowercasing and handling mixed-case variations (e.g., "Free" vs "FREE").
3.  **Tokenization & Stopwords**: Breaking text into tokens and removing non-contributive words (e.g., "the", "is").
4.  **Stemming**: reducing words to their root forms (e.g., "running" $\rightarrow$ "run").
5.  **Vectorization**: Utilizing **TF-IDF (Term Frequency-Inverse Document Frequency)** to convert text into numerical vectors, capped at the top 5,000 features.

---

## 🧠 Model Architecture

We selected a **Support Vector Machine (SVM)** for the final deployment due to its superior performance in high-dimensional spaces (text data).

* **Algorithm**: SVM (Support Vector Classifier).
* **Kernel**: `Linear` (Optimized for speed and text accuracy).
* **Probability**: Enabled (Allows for confidence score calculation).
* **Performance**: The model achieves **~98% Accuracy** on unseen test data, minimizing false positives.

---

## 📂 Directory Structure

```text
SPADE-Spam-Detection/
│
├── static/              # CSS files and assets
├── templates/           # HTML files (index.html)
├── venv/                # Virtual environment
├── app.py               # Main Flask application
├── spam_model.pkl       # Trained SVM Model
├── vectorizer.pkl       # TF-IDF Vectorizer
├── spam.csv             # Dataset
├── requirements.txt     # Python dependencies
└── README.md            # Documentation
