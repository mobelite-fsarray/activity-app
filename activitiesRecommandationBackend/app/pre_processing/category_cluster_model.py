import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict

# Download NLTK resources (comment out if already downloaded)
nltk.download('stopwords')
nltk.download('punkt')  # Download tokenizer for sentence splitting

# import these modules
lemmatizer = WordNetLemmatizer()

# Preprocess the activities
def extract_activity_tags(text):
  text = text.lower()
  stop_words = stopwords.words('english')
  text = [word for word in text.split() if word not in stop_words]
  text = [word for word in text if word.isalpha()]
  text = [lemmatizer.lemmatize(word) for word in text]
  text = [lemmatizer.lemmatize(word, pos='v') for word in text]
  text = [lemmatizer.lemmatize(word, pos='a') for word in text]
  return text


