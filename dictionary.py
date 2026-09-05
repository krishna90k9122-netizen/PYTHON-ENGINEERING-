from listcomprehensive import names
numbers=[2,3,4,5,6]
square={
    n:n*n 
    for n in numbers
}
print(square)

# employees=[
#     employee["name"]
#     for employee in employees
# ]
# print(names)

try:
    with open("tasks.txt","r",encoding="utf-8") as file:
        data=file.read()
        print(data)

except FileNotFoundError:
    print("file not found error")        