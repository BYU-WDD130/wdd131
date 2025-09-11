# passwords.py

# Constants for character types
LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
         "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
         "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]",
           "{", "}", "|", ";", ":", "\"", "'", ",", ".", "<", ">", "?", "/", "`", "~"]

TOP_PASSWORDS_FILE = "toppasswords.txt"
DICTIONARY_FILE = "wordlist.txt"

# Function to check if a word exists in a file
def word_in_file(word, filename, case_sensitive=False):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                file_word = line.strip()
                if not case_sensitive:
                    if word.lower() == file_word.lower():
                        return True
                else:
                    if word == file_word:
                        return True
        return False
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return False

# Function to check if a word contains any character from a list
def word_has_character(word, character_list):
    for char in word:
        if char in character_list:
            return True
    return False

# Function to calculate the complexity of a word
def word_complexity(word):
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity

# Function to calculate the strength of a password
def password_strength(password, min_length=10, strong_length=16):
    # Check dictionary words
    if word_in_file(password, DICTIONARY_FILE, case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0

    # Check top passwords
    if word_in_file(password, TOP_PASSWORDS_FILE, case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0

    # Check minimum length
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    # Check strong length
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    # Otherwise, calculate complexity-based strength
    complexity = word_complexity(password)
    strength = 1 + complexity  # base score 1 + complexity score
    print(f"Password complexity score: {complexity}, total strength: {strength}")
    return strength

# Main loop function
def main():
    print("Welcome to the Password Strength Checker!")
    while True:
        user_input = input("Enter a password to check (or 'q' to quit): ")
        if user_input.lower() == 'q':
            print("Exiting the Password Strength Checker. Stay secure!")
            break
        else:
            strength = password_strength(user_input)
            print(f"Password strength: {strength}/5\n")

# Ensures main() runs only when script is executed directly
if __name__ == "__main__":
    main()