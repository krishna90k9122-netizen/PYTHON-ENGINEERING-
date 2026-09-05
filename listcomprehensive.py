
numbers=[1,2,3,4,5,6,7,8]

square=[n*n for n in numbers]

print(square)

temperature=[20,25,30,35,40]

fahrenhiet=[(temp*9/5)+32 for temp in temperature]
print(fahrenhiet)

transaction=[500,1200,300,2500,800]

large_transaction=[
    amount for amount in transaction
    if amount>=1000
]
print(large_transaction)

numbers=[1,2,3,4,5,6,7,8,9]

result=[
    "even" if n%2==0 else "odd"
    for n in numbers
]

print(result)


names=[
    "krusha",
    "rahul",
    "priya",
    "pooja",
    "sneha"
]
clean_name=[
    name.strip().title()
    for name in names
]
print(clean_name)
