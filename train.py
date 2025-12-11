import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, confusion_matrix

def train_model():
    print("⏳ Loading datasets...")
    
    # Load data
    try:
        fake_df = pd.read_csv('data/fake.csv')
        true_df = pd.read_csv('data/true.csv')
    except FileNotFoundError:
        print("❌ Error: Files not found in 'data/' folder.")
        return

    # Label data: Fake = 0, True = 1
    fake_df['label'] = 0
    true_df['label'] = 1

    # Concatenate and shuffle (reset_index prevents index issues)
    df = pd.concat([fake_df, true_df]).sample(frac=1).reset_index(drop=True)
    
    # Check for nulls in text column and drop them
    df.dropna(subset=['text'], inplace=True)

    # Features and Labels
    X = df['text']
    y = df['label']

    # Split: 80% Training, 20% Testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a Pipeline
    # 1. TfidfVectorizer: Converts text to numerical vectors (removes stop words)
    # 2. PassiveAggressiveClassifier: Efficient for large text datasets
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(stop_words='english', max_df=0.7)),
        ('clf', PassiveAggressiveClassifier(max_iter=50))
    ])

    print("⚙️  Training model...")
    pipeline.fit(X_train, y_train)

    # Evaluation
    y_pred = pipeline.predict(X_test)
    score = accuracy_score(y_test, y_pred)
    print(f"✅ Model Trained! Accuracy: {score*100:.2f}%")

    # Save the pipeline
    joblib.dump(pipeline, 'fake_news_model.pkl')
    print("💾 Model saved as 'fake_news_model.pkl'")

if __name__ == "__main__":
    train_model()