#from secret import username, password
from decouple import config

print("hello world")
#print(username,password)

user= config('user1')
password = config('password1')

# USER1=config('user1')
# PASSWORD1=config('password1')

print(user)
print(password)
print("hello")
# from secret import username, password
# from decouple import config

# print("hello world")
# print(username,password)

# USER1=config('user1')
# PASSWORD1=config('password1')

# print(USER1)
# print(PASSWORD1)
