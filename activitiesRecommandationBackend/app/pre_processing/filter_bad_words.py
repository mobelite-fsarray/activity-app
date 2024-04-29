import nltk

bad_words = ["bad", "swear"]
bad_activities = ["smoking", "procrastinate"]

def filter_bad_words(text):
# Tokenize the text
    tokens = nltk.word_tokenize(text.lower())

# Filter bad words
    filtered_tokens = [token for token in tokens if token not in bad_words]

# Check for bad activities (simple matching)
    bad_activity_count = 0
    for i in range(len(tokens) - 1):  # Check bigrams (two consecutive words)
      if tokens[i] + " " + tokens[i + 1] in bad_activities:
        bad_activity_count += 1

# Option 1: Remove bad words (replace with '-') and flag bad activities
    filtered_text = " ".join(filtered_tokens).replace(" ", "-")
    if bad_activity_count > 0:
      filtered_text += " (WARNING: Bad Activities)"
    print(filtered_text)

# Option 2: Flag text with details
    if bad_words or bad_activity_count:
      print("Text contains issues:")
      if bad_words:
        print("  - Bad words found")
      if bad_activity_count:
        print("  - Bad activities detected:", bad_activity_count)
    else:
      print("Text seems clean")
