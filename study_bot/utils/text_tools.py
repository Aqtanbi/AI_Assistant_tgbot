import re


def clean_text(text: str) -> str:
    cleaned = re.sub(r"\s+", " ", text).strip()
    return cleaned


def is_valid_study_text(text: str) -> bool:
    return bool(text) and len(text) >= 3 and not text.isspace()


def find_keywords(text: str) -> set[str]:
    words = re.findall(r"[A-Za-zА-Яа-я0-9]+", text.lower())
    return {word for word in words if len(word) > 3}


def summarize_keywords(text: str) -> str:
    keywords = list(find_keywords(text))
    long_keywords = filter(lambda word: len(word) >= 5, keywords)
    title_keywords = map(lambda word: word.title(), long_keywords)
    return ", ".join(title_keywords)


def chunk_text(text: str, size: int = 3500):
    for start in range(0, len(text), size):
        yield text[start : start + size]
