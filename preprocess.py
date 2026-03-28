import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# ✅ Fix (add this)
nltk.download('punkt')
nltk.download('punkt_tab')   # <-- ye line ADD karo
nltk.download('stopwords')

def clean_text(text):
    words = word_tokenize(text.lower())
    filtered = [w for w in words if w.isalnum() and w not in stopwords.words('english')]
    return " ".join(filtered)