my_list = [1, 2, 3, 4, 5]

# # # for loop
# total = 0

# for i in my_list:
#     total= total +i

# print(total)

# #total=0
# # i=1, total =0+1, total=1
# # i =2, total =1+2, total=3
# # i = 3, total 3 + 3 = 6

# shortcut
print(sum(my_list))

# using range
# for i in range (0, 101):
 #   print(i)

#using step
# for i in range (0, 101,2):
   # print(i)

# # multiplication table
# for in range(1,13):
#   print(i*12)


# #using range with list index
# shopping_cart=['2KG Rice', 'Bread', 'Egg', 'Bottled water']
# for i in range(0, len(shopping_cart)):
#     print(shopping_cart[i]


# using a forloop for dictionary
bio= {'name':'Edmund','age': 26, 'job':'software developer','location':'joburg'}

for key, value in bio.items():
    print(f'{key}={value}')