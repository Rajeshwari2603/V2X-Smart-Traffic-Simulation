from Crypto.Cipher import AES
import base64
import os

class SecureV2XCommunication:
    def __init__(self, key=None):
        """Initialize AES encryption with a secure key."""
        self.key = key if key else os.urandom(16)  # 16-byte AES key

    def encrypt_message(self, message):
        """Encrypts a message using AES encryption."""
        cipher = AES.new(self.key, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(message.encode('utf-8'))
        return base64.b64encode(nonce + ciphertext).decode('utf-8')

    def decrypt_message(self, encrypted_message):
        """Decrypts an AES encrypted message."""
        encrypted_data = base64.b64decode(encrypted_message)
        nonce = encrypted_data[:16]
        ciphertext = encrypted_data[16:]
        cipher = AES.new(self.key, AES.MODE_EAX, nonce=nonce)
        decrypted_message = cipher.decrypt(ciphertext).decode('utf-8')
        return decrypted_message

# Test the security implementation
if __name__ == "__main__":
    secure_comm = SecureV2XCommunication()

    # Example V2X message
    original_message = "Emergency vehicle detected at intersection!"
    print(f" Original Message: {original_message}")

    # Encrypt the message
    encrypted_msg = secure_comm.encrypt_message(original_message)
    print(f" Encrypted Message: {encrypted_msg}")

    # Decrypt the message
    decrypted_msg = secure_comm.decrypt_message(encrypted_msg)
    print(f" Decrypted Message: {decrypted_msg}")
