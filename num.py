savings = 300 # int
burger_price= 17.58

#conversion
new_savings=float(savings)
print(new_savings)

new_burger_price=int(burger_price)
print(new_burger_price)


#controlling decimal number
survival_cost= savings/9

check_one=(f'{survival_cost:0.2f}')
check_two = float(check_one)

print(type(check_one))
print(type(check_two))

#precedence
guess =10+5*2-6*2

print(guess)