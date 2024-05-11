import time, pyotp, qrcode, os
def crear():
    if os.path.exists("key.txt"):
        with open("key.txt", "r") as file:
            secret_key = file.read()
    else:
        with open("key.txt", "w") as files:
            secret_key = pyotp.random_base32()
            files.write(secret_key)

    return secret_key

key = crear()

uri = pyotp.totp.TOTP(key).provisioning_uri(name="filenomber", issuer_name="farelian app")
print(uri)
qrcode.make(uri).save("totp.png")