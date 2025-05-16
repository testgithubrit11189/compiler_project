# nlp_suggestion.py
import spacy
from difflib import get_close_matches

nlp = spacy.load("en_core_web_lg")

VALID_KEYWORDS = {
    "start", "assign", "allot", "define", "if", "then", "else", "endif",
    "for", "from", "to", "repetition", "endfor", "read", "display", "print", "end"
}

def suggest_keyword(word, valid_keywords=VALID_KEYWORDS, cutoff=0.7):
    word_doc = nlp(word)
    best_match = None
    best_score = 0

    for keyword in valid_keywords:
        keyword_doc = nlp(keyword)
        score = word_doc.similarity(keyword_doc)
        if score > best_score and score >= cutoff:
            best_score = score
            best_match = keyword

    if not best_match:
        fallback = get_close_matches(word, valid_keywords, n=1, cutoff=0.6)
        best_match = fallback[0] if fallback else None

    return best_match

