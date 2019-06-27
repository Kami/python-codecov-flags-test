def to_lowercase(value):
    if not value:
        return None
    return value.lower()


def to_uppercase(value):
    if not value:
        return None
    return value.upper()


def trim(value):
    if not value:
        return None
    return value.strip()
