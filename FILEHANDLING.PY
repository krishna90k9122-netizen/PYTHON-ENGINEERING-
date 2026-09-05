# file=open("data.txt","r")

# data=file.read()
# print(data)

# file.close()


# with open("data.txt","r") as file:

#    data=file.read()
# print(data)

# with open("data.txt" , "w") as file:

#     data=file.write("python is the best langauge kkkkk  ")
# print(data)


# with open("data.txt", "a") as file:
#     data=file.write("spark")

# with open("data.txt2","r") as file:
#     data=file.readlines()
# print(data)

# data=["krishuu","Buggu","pachii","motiii","भगवान श्रीकृष्ण हिन्दू धर्म में भगवान विष्णु के आठवें अवतार माने जाते हैं।"]

# with open("data.txt3","r",encoding="utf-8") as file:
#     data=file.read()
# print(data)

# with open("data.txt3","w" ,encoding="utf-8") as file:
#     file.write("भगवान श्रीकृष्ण हिन्दू धर्म में भगवान विष्णु के आठवें अवतार माने जाते हैं।")


# with open("data.txt3","r",encoding="utf-8") as file:
#     print(file.read())


with open("sales.txt","r",encoding="utf-8") as file:
    
    for line in file:
        line=line.strip()
        name,city,amount=line.split(",")
      
amount=int(amount)

if amount>=500:
    print(name,city,amount)
    