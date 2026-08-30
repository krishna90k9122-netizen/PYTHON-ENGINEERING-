number=[1,2,3,4,5,6,7,8,9,10]

print(number)


number.append(12)
number.remove(5)
print(number)


student_a={"John", "Doe", "monu","sonu"}
student_b={"Jane", "Smith", "Ravi","Anu","sonu"}

print(student_a.union(student_b))  # Output: ['John', 'Doe', 'monu', 'sonu', 'Jane', 'Smith', 'Ravi', 'Anu']
print(student_a.intersection(student_b))  # Output: ['sonu']