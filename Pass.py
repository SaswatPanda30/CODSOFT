import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4.")
        return None
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = [random.choice(string.ascii_lowercase), random.choice(string.ascii_uppercase), random.choice(string.digits),random.choice(string.punctuation)]
    password += random.choices(characters, k=length - 4)
    random.shuffle(password)
    return ''.join(password)

def main():
    try:
        length = int(input("Enter password length (minimum 4): "))
        if length < 4:
            print("Password length should be at least 4.")
            return
    except ValueError:
        print("Enter a valid number.")
        return

    password = generate_password(length)
    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
