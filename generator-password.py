import secrets
import string


def generateSecorePassword(length:int):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(chars) for i in range(length))
    return password



secore_password = generateSecorePassword(15)
print(secore_password)