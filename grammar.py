import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.parse import ChartParser
from nltk.tree import ParentedTree

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('averaged_perceptron_tagger')

def preprocess_text(text):
    # Tokenize text into sentences and words
    sentences = sent_tokenize(text)
    words = [word_tokenize(sent) for sent in sentences]

    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    filtered_words = [[word.lower() for word in sent if word.lower() not in stop_words] for sent in words]

    return filtered_words

def check_subject_verb_agreement(tags):
    errors = []
    for i in range(1, len(tags)):
        prev_word, prev_tag = tags[i-1]
        current_word, current_tag = tags[i]
        if prev_tag.startswith('NN') and current_tag.startswith('VB'):
            # Check if singular noun is followed by a plural verb
            if prev_word != "I" and not current_word.endswith("s"):
                errors.append(f"Subject-Verb Agreement Error: '{prev_word} {current_word}'")
    return errors

def check_verb_tense(tags):
    errors = []
    for i in range(1, len(tags)):
        prev_word, prev_tag = tags[i-1]
        current_word, current_tag = tags[i]
        if prev_tag.startswith('VB') and current_tag.startswith('V'):
            # Check if the verb tense is consistent within a sentence
            if prev_word != current_word:
                errors.append(f"Verb Tense Error: '{prev_word} {current_word}'")
    return errors

def check_capitalization(text):
    errors = []
    # Check if the first word of each sentence is capitalized
    sentences = sent_tokenize(text)
    for sent in sentences:
        if not sent[0].isupper():
            errors.append(f"Capitalization Error: '{sent[0]}' should be capitalized.")
    return errors

def check_pronoun_consistency(text):
    errors = []
    pronouns = {'he', 'him', 'his', 'she', 'her', 'hers', 'it', 'its', 'they', 'them', 'their', 'theirs'}
    sentences = sent_tokenize(text)
    for sent in sentences:
        words = word_tokenize(sent.lower())
        for i, word in enumerate(words):
            if word in pronouns:
                if i > 0 and words[i-1] not in {'i', 'you', 'we', 'they', 'he', 'she', 'it'}:
                    errors.append(f"Pronoun Consistency Error: '{word}' is used without a proper antecedent.")
    return errors

def check_sentence_structure(text):
    errors = []
    grammar = """
        S -> DT? JJ* <NN.*>+ <VB.*> .*
    """
    cp = ChartParser(nltk.CFG.fromstring(grammar))

    sentences = sent_tokenize(text)
    for sent in sentences:
        words = word_tokenize(sent)
        tagged_words = pos_tag(words)
        tree = list(cp.parse(tagged_words))

        if not tree:
            errors.append(f"Sentence Structure Error: '{sent}' contains a suboptimal sentence structure.")
    return errors

def grammar_check(text):
    words = preprocess_text(text)
    errors = check_subject_verb_agreement(pos_tag(word_tokenize(text))) + \
             check_verb_tense(pos_tag(word_tokenize(text))) + \
             check_capitalization(text) + \
             check_pronoun_consistency(text) + \
             check_sentence_structure(text)
    return errors

if __name__ == "__main__":
    sample_essay = """
    Technology has significantly impacted our lives. It has transformed the way we communicate, work, and even entertain ourselves. However, some argue that excessive reliance on technology can have negative consequences on our mental and social well-being. In this essay, I will discuss the advantages and disadvantages of technology and present my opinion on its overall impact.

    on one hand, technology has made our lives more convenient and efficient. the internet, for instance, has enabled us to access vast amounts of information at our fingertips. this has facilitated learning and research, making education more accessible to people around the world. additionally, technological advancements in the healthcare sector have led to improved medical treatments and enhanced quality of life for many individuals.

    on the other hand, the overuse of technology has raised concerns about its impact on mental health. excessive screen time, especially among young people, has been linked to issues such as anxiety and depression. moreover, the rise of social media has altered the way we interact with others. many individuals now prioritize virtual connections over face-to-face interactions, potentially leading to feelings of isolation and disconnection from the real world.

    in conclusion, technology is a double-edged sword. while it has undoubtedly brought numerous benefits to society, we must be cautious about its potential negative effects. to harness the power of technology for the greater good, we should strive to strike a balance between its usage and our well-being. only by doing so can we truly maximize the advantages of technology while mitigating its drawbacks.
    """

    essay_errors = grammar_check(sample_essay)
    if len(essay_errors) == 0:
        print("No grammar errors found.")
    else:
        print("Grammar errors:")
        for error in essay_errors:
            print(error)