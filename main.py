from secret import username, password
from decouple import config

print("hello world")
print(username,password)

user1 = config('username')
password1 = config('pasword')

# USER1=config('user1')
# PASSWORD1=config('password1')

print(user1)
print(password1)

# from secret import username, password
# from decouple import config

# print("hello world")
# print(username,password)

# USER1=config('user1')
# PASSWORD1=config('password1')

# print(USER1)
# print(PASSWORD1)
