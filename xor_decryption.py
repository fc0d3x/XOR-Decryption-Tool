def hex_to_bytes(hex_string):
    return bytes.fromhex(hex_string)

def xor_bytes(data, key):
    # Extend the key to match the length of data
    extended_key = key * (len(data) // len(key) + 1)
    extended_key = extended_key[:len(data)]
    
    # Perform XOR operation
    return bytes(a ^ b for a, b in zip(data, extended_key))

def find_key(ciphertext, known_plaintext):
    # Convert known plaintext to bytes
    known_bytes = known_plaintext.encode()
    
    # Find the key by XORing the first bytes of ciphertext with known plaintext
    key = bytes(a ^ b for a, b in zip(ciphertext[:len(known_bytes)], known_bytes))
    return key

def main():
    # The encrypted message (combined both parts)
    encrypted_hex = "1c1c01041963730f31352a3a386e24356b3d32392b6f6b0d323c22243f63731a0d0c302d3b2b1a292a3a38282c2f222d2a112d282c31202d2d2e24352e60"
    
    # Convert hex to bytes
    ciphertext = hex_to_bytes(encrypted_hex)
    
    # Known plaintext at the start of the message
    known_plaintext = "ORDER:"
    
    # Find the key
    key = find_key(ciphertext, known_plaintext)
    print(f"Found key: {key.hex()}")
    
    # Decrypt the entire message
    decrypted = xor_bytes(ciphertext, key)
    print("\nDecrypted message:")
    print(decrypted.decode('ascii'))

if __name__ == "__main__":
    main()