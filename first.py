# name ="Oluwadamilola" #string
# age = 20 #integer
# change = 25.75 #float
# is_married =True # boolean


# print (type(is_married))

name, age, change, is_married = "Oluwadamilola", 20, 25.75, True

print ("my name is " + name + " i am " + str(age) + " years old")

print ("my name is {username}.I am {userage} years old". format(username=name, userage=str(age)) )

print (f"my name is {name}. I am {age} years old")

#
print ("my name is {} {}".format(name, age))