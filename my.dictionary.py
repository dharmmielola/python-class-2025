bio= {'name':'Edmund','age': 26, 'job':'software developer','location':'joburg'}

#accessing a value

print(bio['name'])

#print all the keys
print(bio.keys())

#print all values
print(bio.values())

#add to it
bio['Degree']= 'Data Science'

print(bio.values())

#update a record
bio['name']= 'Edmund Rotimi'


new_tuple=bio.popitem()
print(bio)
print(new_tuple)
