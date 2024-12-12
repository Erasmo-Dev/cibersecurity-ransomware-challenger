import os
import pyaes

# Decryption key
decryption_key = b"testeransomwares"

# Encrypted file details
encrypted_file_name = "example.txt.ransomwaretroll"

# Read encrypted file
with open(encrypted_file_name, "rb") as encrypted_file:
    encrypted_content = encrypted_file.read()

# Perform decryption
aes_cipher = pyaes.AESModeOfOperationCTR(decryption_key)
decrypted_content = aes_cipher.decrypt(encrypted_content)

# Delete the encrypted file
os.remove(encrypted_file_name)

# Write the decrypted file
decrypted_file_name = "example.txt"
with open(decrypted_file_name, "wb") as decrypted_file:
    decrypted_file.write(decrypted_content)

