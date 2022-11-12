import hashlib
 
def hash(password):
    hasher = hashlib.sha512()
    hasher.update(password.encode())
    password = hasher.hexdigest()
    return password