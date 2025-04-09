# train_model.py
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Example training dataset
emails = [
    "Congratulations! You've won a $1000 gift card",
    "Click here to claim your prize",
    "Hi, are we still meeting today?",
    "Please find attached the report",
    "Earn money fast with this trick",
    "Hello friend, long time no see!"
]
labels = [1, 1, 0, 0, 1, 0]  # 1 = spam, 0 = not spam

# Convert text to feature vectors
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)

# Train the spam classifier
clf = MultinomialNB()
clf.fit(X, labels)

# Save model + vectorizer into one file
with open("spam_classifier.pkl", "wb") as f:
    pickle.dump((vectorizer, clf), f)

print("✅ Model trained and saved as spam_classifier.pkl")
