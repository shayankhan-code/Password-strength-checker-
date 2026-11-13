import re
from getpass import getpass

# Words that should never appear in a password.
COMMON_WORDS = ["password", "123456", "qwerty", "pakistan"]

# Symbols people use instead of letters: "P@ssw0rd" is really "password".
LOOKALIKES = str.maketrans("@4301$5", "aaeoiss")


def is_common(password):
    """Return True if the password contains a common word, even with symbol swaps."""
    lowered = password.lower()
    unswapped = lowered.translate(LOOKALIKES)
    for word in COMMON_WORDS:
        if word in lowered or word in unswapped:
            return True
    return False


def has_repeated_chars(password):
    """Return True if any character appears 3 or more times in a row (like 'aaa')."""
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            return True
    return False


def password_strength_checker(password):
    """Check length and character types. The message starts with 'weak' or 'strong'."""
    if len(password) < 12:
        return "weak: password must be at least 12 characters long"

    if not re.search(r"[a-z]", password):
        return "weak: password must contain at least one lowercase letter"

    if not re.search(r"[A-Z]", password):
        return "weak: password must contain at least one uppercase letter"

    if not re.search(r"[0-9]", password):
        return "weak: password must contain at least one digit"

    # Any character that is not a letter or a digit counts as special.
    if not re.search(r"[^A-Za-z0-9]", password):
        return "weak: password must contain at least one special character"

    return "strong: password is strong"


def main_checker(password):
    """Return (is_common, has_repeats, strength) for a password."""
    if not password:
        return False, False, "password cannot be empty"

    common_result = is_common(password)
    repeated_result = has_repeated_chars(password)

    if common_result:
        strength_result = "weak: password contains a common word"
    elif repeated_result:
        strength_result = "weak: password contains 3 or more repeated characters in a row"
    else:
        strength_result = password_strength_checker(password)

    return common_result, repeated_result, strength_result


# This part runs only when you start this file directly.
if __name__ == "__main__":
    password = getpass("Enter your password: ")
    common_result, repeated_result, strength_result = main_checker(password)

    print("Common word:", common_result)
    print("Repeated characters:", repeated_result)
    print("Strength:", strength_result)
    
