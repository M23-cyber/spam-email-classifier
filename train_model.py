from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import joblib

# Load your dataset
data = pd.read_csv('your_dataset.csv')  # Replace with actual path
X = data['text']
y = data['label']

# Create pipeline
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Train the model
model.fit(X, y)

# Save the whole pipeline
joblib.dump(model, 'spam_classifier.pkl')

print("✅ Model trained and saved successfully.")
