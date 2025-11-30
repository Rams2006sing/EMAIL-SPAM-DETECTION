SPADE: Intelligent Email Spam Detection System
1. Project Overview
This project is a Machine Learning-based web application designed to detect spam emails. It uses Natural Language Processing (NLP) to analyze text patterns and a Support Vector Machine (SVM) algorithm to classify messages as "Spam" or "Legitimate (Ham)." The system includes a modern web interface that provides Confidence Scores and extracts key insights (Money, Dates, Entities) using Regex.

7. Implementation
7.1 Environment Setup
To run this project, specific tools and libraries are required to handle data processing, machine learning, and web development.

Tools:

Python 3.11+: The core programming language.

VS Code / Jupyter Notebook: For coding and model training.

Terminal: For executing commands.

Libraries Used:

pandas: For loading and manipulating the dataset.

numpy: For numerical array operations.

scikit-learn: For the SVM algorithm, TF-IDF vectorization, and evaluation metrics.

nltk: For text cleaning (stopwords, stemming, tokenization).

flask: To create the web server and connect the model to the UI.

pickle: To save and load the trained models (.pkl files).

re: (Built-in) For Regular Expressions used in preprocessing and entity extraction.

7.2 Importing and Loading Data
The project uses the SMS Spam Collection dataset (spam.csv).

The data is loaded using pandas.read_csv() with latin-1 encoding.

The dataset initially contains unnecessary columns (Unnamed: 2, etc.), which are dropped.

The relevant columns are renamed:

v1 → label (Target: Spam/Ham)

v2 → text (The email content)

Labels are encoded: Ham becomes 0, and Spam becomes 1.

7.3 Preprocessing Implementation
Raw text cannot be understood by machines, so we apply a cleaning pipeline:

Lowercasing: "Free" and "FREE" are treated as the same word.

Noise Removal: Using Regex to remove special characters, URLs, and punctuation.

Tokenization: Breaking sentences into individual words (tokens).

Stopword Removal: Removing common words (is, the, are) that add no value to classification.

Stemming: Converting words to their root form (e.g., "running" → "run").

Feature Extraction (Vectorization):

We use TF-IDF (Term Frequency-Inverse Document Frequency).

It converts text into numerical vectors, giving less weight to common words and more weight to unique/important words.

Limit: We restrict the model to the top 5000 most frequent features.

7.4 Model Building
We experimented with multiple algorithms (Naive Bayes, Logistic Regression), but selected Support Vector Machine (SVM) for the final deployment.

Why SVM? SVM works exceptionally well for high-dimensional data (text) by finding the optimal "hyperplane" that separates Spam and Ham with the widest margin.

7.5 Model Compilation (Configuration)
In Scikit-Learn, "compilation" refers to setting the hyperparameters before training.

Kernel: linear. Linear kernels are faster and often more accurate for text classification than complex kernels like RBF.

Probability: True. This is crucial. Standard SVM only gives a binary output (0 or 1). We enabled probability estimates to calculate the Confidence Score % (e.g., "98.5% sure this is Spam") shown in the UI.

7.6 Training the Model
Splitting: The data is split into 80% Training and 20% Testing sets using train_test_split.

Fitting: The SVM model is trained (.fit()) on the training data (X_train, y_train).

Saving: The trained model and the TF-IDF vectorizer are saved as spam_model.pkl and vectorizer.pkl using pickle. This allows the web app to load the "brain" without retraining every time.

7.7 Testing the Model
After training, the model is evaluated on unseen data (X_test).

Accuracy: Achieved ~98% accuracy on test data.

Confusion Matrix: Checked to minimize "False Positives" (marking a real email as spam).

ROC-AUC Curve: Used to visualize the trade-off between sensitivity and specificity.

7.8 User Input Interface
The system features a complete web interface:

Backend (Flask): app.py loads the saved .pkl models. It receives text from the website, transforms it using the vectorizer (.toarray()), and predicts the result.

Frontend (HTML/CSS): index.html provides a modern dashboard.

Text Area: For user input.

Progress Bars: Visualizes the confidence probability.

Entity Extraction (Insights): A custom Regex Logic scans the text to extract:

Money (e.g., $5,000)

Dates (e.g., Nov 29, 2025)

Organizations/Names (Capitalized words)

These entities are displayed in expandable cards to help users understand why a message looks suspicious.

8. Results
Accuracy: The model successfully classifies emails with high precision.

Visual Output:

Spam Messages trigger a Red Warning with high spam probability bars.

Legitimate Messages trigger a Green Safe Badge with high ham probability bars.

Insight Generation: The system successfully highlights critical entities (like huge money amounts or urgent dates) often found in phishing scams, providing users with context beyond just a simple label.