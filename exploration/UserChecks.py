username = '(*&)'
username_errors = []
# Run the tests
if not username[0].isupper():
    username_errors.append('Your username did not start with a capital letter')
if not any(i.islower() for i in username):
    username_errors.append('Your username did not contain a little letter')
if not username[-1].isdigit():
    username_errors.append('Your username did not end in a digit')
if username_errors == []:
    username_errors.append('There were no errors')
print(username_errors)
