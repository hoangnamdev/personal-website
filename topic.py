import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def preprocess_text(text):
    # Tokenize and remove stopwords
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text.lower())
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]

    return " ".join(filtered_words)

def calculate_cosine_similarity(topic, essay):
    # Preprocess the topic and essay
    processed_topic = preprocess_text(topic)
    processed_essay = preprocess_text(essay)

    # Vectorize the topic and essay
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([processed_topic, processed_essay])

    # Calculate cosine similarity between the topic and essay
    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
    return similarity

def evaluate_essay(topic, essay):
    similarity_score = calculate_cosine_similarity(topic, essay)
    return similarity_score

if __name__ == "__main__":
    # Sample topic and essay for evaluation
    essay_topic = "Do you think humans need to die?"
    essay_text = """Hello, how are you?"""

    similarity_score = evaluate_essay(essay_topic, essay_text)
    print(f"Essay Similarity Score: {similarity_score:.2f}")