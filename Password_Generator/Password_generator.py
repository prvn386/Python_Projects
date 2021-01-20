import random
password_length = int(input('Enter the length of password:'))
s = 'abcdefghijklmnopqrstuvwxyz01234567890!@#$%^&*~ABCDEFGHIJKLMNOPQRSTUVWXYZ'
new_password = ''.join(random.sample(s,password_length))
print(new_password)