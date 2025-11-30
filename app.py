from flask import Flask, render_template, request
import pickle
import re

app = Flask(__name__)

# --- LOAD THE NEW MODELS ---
try:
    print("Loading models...")
    with open("spam_model.pkl", "rb") as f:
        model = pickle.load(f)
    
    with open("vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
    print("Models loaded successfully!")
except FileNotFoundError:
    print("ERROR: Models not found. Make sure spam_model.pkl and vectorizer.pkl are in the folder.")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        message = request.form["message"]
        
        # --- 1. PREDICTION (Using SVM + Vectorizer) ---
        # FIX: We add .toarray() because the SVM model expects a dense array
        vect_message = vectorizer.transform([message]).toarray()
        
        # Then predict
        prediction_class = model.predict(vect_message)[0]
        probabilities = model.predict_proba(vect_message)[0]
        
        ham_score = round(probabilities[0] * 100, 1)
        spam_score = round(probabilities[1] * 100, 1)
        
        if prediction_class == 1 or prediction_class == "spam":
            result_text = "SPAM DETECTED"
            confidence = spam_score
            is_spam = True
        else:
            result_text = "LEGITIMATE MAIL (HAM)"
            confidence = ham_score
            is_spam = False

        # --- 2. INSIGHTS (REGEX ENTITY EXTRACTION) ---
        extracted_data = {
            "Money": [],
            "Dates": [],
            "Numbers": [],
            "Names/Orgs": []
        }

        # A. Extract Money ($500, 500 USD)
        money_matches = re.findall(r'\$\d+(?:,\d+)*(?:\.\d+)?|\d+\s*(?:dollars|usd|eur|pounds)', message, re.IGNORECASE)
        extracted_data["Money"] = list(set(money_matches))

        # B. Extract Numbers (simple digits, IDs)
        all_nums = re.findall(r'\b\d+\b', message)
        extracted_data["Numbers"] = list(set([n for n in all_nums if n not in str(money_matches)]))

        # C. Extract Capitalized Words (Potential Names/Orgs/Locations)
        cap_matches = re.findall(r'(?<!^)(?<!\.\s)\b[A-Z][a-z]+\b', message)
        extracted_data["Names/Orgs"] = list(set(cap_matches))
        
        # D. Simple Date Detection
        date_patterns = r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2},? \d{4}\b|\b\d{1,2}/\d{1,2}/\d{2,4}\b|\b(?:Mon|Tues|Wednes|Thurs|Fri|Satur|Sun)[a-z]*\b'
        date_matches = re.findall(date_patterns, message, re.IGNORECASE)
        extracted_data["Dates"] = list(set(date_matches))

        # Remove empty categories
        extracted_data = {k: v for k, v in extracted_data.items() if v}

        return render_template("index.html", 
                               message=message,
                               prediction=result_text, 
                               confidence=confidence,
                               spam_score=spam_score,
                               ham_score=ham_score,
                               is_spam=is_spam,
                               insights=extracted_data)

if __name__ == "__main__":
    app.run(debug=True, port=5001)