def xor_encrypt(data, key):
    return bytes(a ^ b for a, b in zip(data, key))

key = b"secretkey"
file_to_encrypt = "test.txt"

with open(file_to_encrypt, "rb") as f:
    data = f.read()

encrypted = xor_encrypt(data, key)
with open(file_to_encrypt + ".enc", "wb") as f:
    f.write(encrypted)

print(f"File {file_to_encrypt} encrypted to {file_to_encrypt}.enc")
