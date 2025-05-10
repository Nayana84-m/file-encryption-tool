from cryptography.fernet import Fernet

# Generate and save a key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("✅ Key generated and saved as 'secret.key'")

# Load the saved key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt a file
def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(filename, "wb") as encrypted_file:
        encrypted_file.write(encrypted)

    print(f"🔐 Encrypted: {filename}")

# Decrypt a file
def decrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(filename, "wb") as decrypted_file:
        decrypted_file.write(decrypted)

    print(f"🔓 Decrypted: {filename}")

# Main menu
def main():
    print("===== File Encryption Tool =====")
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        generate_key()
    elif choice == '2':
        filename = input("Enter the file name to encrypt: ")
        encrypt_file(filename)
    elif choice == '3':
        filename = input("Enter the file name to decrypt: ")
        decrypt_file(filename)
    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
