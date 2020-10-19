first_name = 'James'
last_name = 'Bond'

sentence = 'My name is ' + last_name + ', ' + first_name + ' ' + last_name + '.'
print(sentence)

sentence2 = 'My name is {}, {} {}.'.format(last_name, first_name, last_name)
print(sentence2)

sentence3 = 'My name is {1}, {0} {1}.'.format(first_name, last_name)
print(sentence3)

sentence4 = 'My name is {lname}, {fname} {lname}.'.format(fname=first_name, lname=last_name)
print(sentence4)

sentence5 = f'My name is {last_name}, {first_name} {last_name}.'
print(sentence5)

# WARNING!!
# You can concatenate string with format or f strings, however you will have issues
# when adding CSS to your HTML because CSS contains curly braces.
#