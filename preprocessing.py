import re
import string

def clean_text(text):
    """
    Cleans raw news text for the model.
    1. Lowercase
    2. Remove square brackets
    3. Remove links/URLs
    4. Remove punctuation
    """
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    return text