# app/utils/formatter.py
def extract_quotes(text, max_length=280):
    quotes = []
    sentences = text.split('.')
    current = ''

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue

        if len(current) + len(sentence) + 1 <= max_length:
            current += (sentence + '. ')
        else:
            quotes.append(current.strip())
            current = sentence + '. '

    if current:
        quotes.append(current.strip())

    return quotes[:20]  # Limit to 20 quotes for MVP simplicity
