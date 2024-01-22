from hashlib import sha256
import pandas
import string
import random
import re


def validate_password(password):
    # Check if the password has at least 8 characters
    if len(password) < 8:
        return False

    # Check if the password contains at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False

    # Check if the password contains at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False

    # Check if the password contains at least one digit
    if not re.search(r'\d', password):
        return False

    # Check if the password contains at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False

    # If all the conditions are met, the password is valid
    return True


def attack(dictionary_word, target_hash):
    pass_bytes = str(dictionary_word).encode('utf-8')
    pass_hash = sha256(pass_bytes)
    digest = pass_hash.hexdigest()
    if digest == target_hash:
        return True


def create_hash(passwd):
    pass_bytes = passwd.encode('utf-8')
    pass_hash = sha256(pass_bytes)
    hashed_pass = pass_hash.hexdigest()
    return hashed_pass


def salted_hash(salt, password):
    salt = salt.encode('utf-8')
    password = password.encode('utf-8')
    hashed_password = sha256(salt+password).hexdigest()
    return hashed_password


if __name__ == "__main__":
    # Read username and password
    username = input("Enter your username: ")
    passwd = input("Enter your password: ")
    is_valid = validate_password(passwd)
    if is_valid:
        print("That's a strong Password!\n")
    else:
        print("Consider a stronger Password with at least 1 uppercase letter, 1 special character and 1 digit. ---> This one could be bruteforced! <---\n")
    print('Creating a SHA256 hash for your password')
    # Use the create_hash function to create a hash
    hashed_pass = create_hash(passwd)
    print('SHA256 hash: ' + hashed_pass)
    # Create a salt of 8 characters
    N = 8
    salt = ''.join(random.choices(string.ascii_lowercase + string.digits, k=N))
    print('Generated Salt: ' + str(salt))
    salted_passwd = salted_hash(salt, passwd)
    print('SHA256 Salted_hash: ' + salted_passwd)
    # read the dictionary using pandas.read_csv
    dictionary = pandas.read_csv("password_dictionary", names=['passwords'])
    print('\nAttempting bruteforce with the Salted_hash password')
    # match all words from the dictionary until it matches/ends
    for test_word in dictionary["passwords"]:
        if attack(test_word, salted_passwd):
            print('Salted Hash Matched for user', username, ': ', test_word)
            break
    else:
        print('Could not match Salted Hash\n')
    print('Attempting bruteforce with just the Hashed password')
    # match all words from the dictionary until it matches/ends
    for test_word in dictionary["passwords"]:
        if attack(test_word, hashed_pass):
            print('Password Hash Matched for user', username, ': ', test_word)
            break
    else:
        print('Could not match Password Hash')
