name='damilola'
print(name)

#string operation
print(name.capitalize())

print(name.upper())

new_name ='Femi Edmund'
print(new_name.startswith('zem'))
print(new_name.endswith('und'))

print(new_name.count('d'))

#
student_number ='123.4567'
print(student_number.isdecimal())

#
school='UJ UJ UJ'
print(school.replace('UJ', 'UP'))
new_school=school.replace('UJ','UP', -1)
print(new_school)

introduction='my name is Oluwadamilola and I am 24 years  old'
print(introduction.rfind('u'))

print(introduction.title())