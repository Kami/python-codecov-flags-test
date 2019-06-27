def to_lowercase(value):
    if not value:
        return None
    return value.lower()


def to_uppercase(value):
    if not value:
        return None
    return value.upper()


def repeat(value, times=2):
    if not value:
        return None
    return str(value) * int(times)
