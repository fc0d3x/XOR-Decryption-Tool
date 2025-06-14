XOR Decryption Script

This Python script demonstrates how to decrypt a message that has been encrypted using the XOR cipher. The script can recover the encryption key if a portion of the plaintext is known, making it useful for educational purposes, cryptography challenges, and penetration testing tasks.

Features
Hexadecimal to Bytes Conversion: Converts a hexadecimal string (ciphertext) into bytes for easier processing.

XOR Decryption: Decrypts the ciphertext using a key obtained from the known plaintext.

Key Recovery: Automatically derives the key by XORing known plaintext with the ciphertext.

Plaintext Recovery: Decrypts the full message once the key is found.

Requirements
Python 3.x or higher
