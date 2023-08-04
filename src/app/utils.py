import hashlib


def hashing_password(password: str):
    return hashlib.sha256(password.encode()).hexdigest()
