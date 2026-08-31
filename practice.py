student={
    "name":"krishna",
    "age":20,   
    "courses":["Math","Science","History"],
    "marks":{
        "maths":90,
        "science":85,   
       "python":95,

    }
}

print("Name:", student["name"])
print("Age:", student["age"])
print("Courses:", student["courses"])
print("Maths Marks:", student["marks"]["maths"])
print("Science Marks:", student["marks"]["science"])
print("Python Marks:", student["marks"]["python"])

student["marks"]["python"]=90

print("Updated Marks:", student["marks"]["python"])


number={1,2,3,4,5,6,7}

square={n:n*n for n in number}

print(square)

