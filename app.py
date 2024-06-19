import rsa

publicKey, privateKey = rsa.newkeys(512)

message = "Hello, RSA!"

cipher = rsa.encrypt(message.encode(), publicKey)

print("Original String: ", message)
print("Encrypted String: ", cipher)

decodedMessage = rsa.decrypt(cipher, privateKey).decode()
print("Decrypted String: ", decodedMessage)
