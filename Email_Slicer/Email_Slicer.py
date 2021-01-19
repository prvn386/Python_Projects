email = input("Enter user email address:").strip() # this will eliminate the blank spaces in the input
#print(email)
user_name = email[:email.index('@')]
domain_name = email[email.index('@')+1:]
print('Your username is {0} and your domain name is {1}'.format(user_name,domain_name))