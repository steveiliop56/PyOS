import bcrypt
 
def hash(password):
    bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()  
    hash = bcrypt.hashpw(bytes, salt)
    hash = hash.decode("utf-8")
    return hash