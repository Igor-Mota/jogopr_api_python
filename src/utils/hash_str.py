import hashlib


def hash_str(string):

    text = string.strip()
    text = hashlib.sha256(str(string).encode('utf-8'))
    text = text.hexdigest()

    return text
