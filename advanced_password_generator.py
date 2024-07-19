import random
import string

def generate_password(length, use_letters, use_digits, use_special):
    """
    Generate a random password based on specified criteria.
    
    Parameters:
    length (int): Desired length of the password
    use_letters (bool): Include letters in the password
    use_digits (bool): Include digits in the password
    use_special (bool): Include special characters in the password
    
    Returns:
    str: Generated password
    """
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be selected.")

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            raise ValueError("Length should be a positive integer.")
    except ValueError as e:
        print(e)
        return

    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    try:
        password = generate_password(length, use_letters, use_digits, use_special)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()