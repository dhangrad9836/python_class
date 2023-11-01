
# we use the asterick to send multiple arguments as a ie: dictionary with keys inside the print
# statement
def my_function(**kid):
    print('His name is ' + kid['lname'] + " " + kid['fname'])
    # note: you need to use double quotation marks for dictionary keys as listed below
    # single quotes will not work
    print(f'His name is {kid["fname"]} {kid["lname"]}')

my_function(fname='Mark', lname='Tailor')