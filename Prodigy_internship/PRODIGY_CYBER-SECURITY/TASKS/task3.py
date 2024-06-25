import re

def password_strength(password):
    """
    Assess the strength of a password based on the following criteria:
    1. Length: at least 12 characters
    2. Presence of:
        * Uppercase letters
        * Lowercase letters
        * Numbers
        * Special characters
    Returns a score from 0 to 4, where:
    0: Very weak
    1: Weak
    2: Medium
    3: Strong
    4: Very strong
    """
    score = 0

    # Check length
    if len(password) >= 12:
        score += 1

    # Check for presence of uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1

    # Check for presence of lowercase letters
    if re.search(r"[a-z]", password):
        score += 1

    # Check for presence of numbers
    if re.search(r"\d", password):
        score += 1

    # Check for presence of special characters
    if re.search(r"[!@#$%^&*()_+=-{};:'<>,./?]", password):
        score += 1

    # Map score to strength level
    strength_levels = {
        0: "Very weak",
        1: "Weak",
        2: "Medium",
        3: "Strong",
        4: "Very strong"
    }
    return strength_levels[score]

def main():
    password = input("Enter a password: ")
    strength = password_strength(password)
    print(f"Password strength: {strength}")

if __name__ == "__main__":
    main()