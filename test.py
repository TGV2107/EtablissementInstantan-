import bcrypt as bc
def verify(password):
    password = password.encode("utf-8")
    hashedpassword = bc.hashpw(password,bc.gensalt(10))
    return hashedpassword
    
print(verify("J'adorelesmaths"))