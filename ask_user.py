name= input('please enter your name: \n')
new_name= name.strip()

print(new_name) 

age=input('Enter your age')

if int(age)>=18 and int(age) < 21:
    print('Welcome to a Diploma Degree')
elif int(age) >=21:
    print('Welcome to Uni Degree')
else:
    print('Not allowed to register')



#conditional statement
#Or, and
#