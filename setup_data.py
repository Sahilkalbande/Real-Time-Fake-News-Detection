# File: src/setup_data.py
import pandas as pd
import os
import requests
from io import BytesIO

# 1. Configuration
DATA_URL = "https://raw.githubusercontent.com/lutzhamel/fake-news/master/data/fake_or_real_news.csv"
SAVE_PATH = "dataset/news.csv"

def load_data():
    print(f"🚀 Downloading dataset from: {DATA_URL}...")
    
    try:
        # Request the file from the internet
        response = requests.get(DATA_URL)
        response.raise_for_status() # Check for download errors
        
        # Load into Pandas directly from memory
        print("✅ Download complete. Processing data...")
        df = pd.read_csv(BytesIO(response.content))
        
        # 2. Clean and Format
        # The raw dataset has columns: 'id', 'title', 'text', 'label'
        # We only need 'text' and 'label'
        df = df[['text', 'label']]
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(SAVE_PATH), exist_ok=True)
        
        # 3. Save to local disk
        df.to_csv(SAVE_PATH, index=False)
        print(f"💾 Success! Dataset saved to: {SAVE_PATH}")
        print(f"📊 Rows: {len(df)} | Columns: {df.columns.tolist()}")
        print("-" * 30)
        print(df.head(3)) # Show a preview

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    load_data()