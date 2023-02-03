from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    """verifies hashed password with provided password"""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """hash passwords recieved by the user on signup
    Args:
        password: user provided password
    Return:
        hashed password
    """

    return pwd_context.hash(password)


def findOne(email):
    """Finds a single user from the database"""
     SQL_STRING = "SELECT * FROM user where email = (%s)"
     
    #get user from the database
    
    #find user that satisfies the condition given
    found_user = filter(lambda x:x==condition,usernames)
    #return the user data if found else return None
    return filter(lambda x : x.get("username") == found_user,database) \
        if found_user is not None else None

def 
if __name__ == "__main__":
    response = findOne([{"username":"michael",
        "passsword":"2344"},
        {"username":"Kofi",
        "password":"kofidsdf"}],condition= "michael")
    print(list(response))

