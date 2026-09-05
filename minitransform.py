with open("tans.txt","r",encoding="utf-8") as file:
    for line in file:
        line=line.strip()

        name,city,amount=line.split(",")
        amount=int(amount)
        if city=="delhi" and amount>=1000:
            print(name,amount)

# with open("task.txt","r",encoding="utf-8") as input_file:
#     with open("filtered_task.txt","w",encoding="utf-8") as output_file:

#         for line in input_file:

#            line=line.split()

#            name,city,amount=line.split(",")
  
#            amount=int(amount)
        
#         try:
#            if amount>=800:
#             print("work success")
#             output_file.write(
#             f"{name},{city},{amount}\n"
#              )
#         except FileNotFoundError:
#                 print("no file ")


# with open("employ.txt","r",encoding="utf-8") as input_file:
#      with open("selected_employee.txt","w",encoding="utf-8") as output_file:

#         for line in input_file:
   
#          try:
#             line=line.strip()

#             name,domain,salary=line.split(",")

#             salary=int(salary)
            
#             if domain=="data engineering" and salary>=20000:
#                     print("work done succesfully")
#                     output_file.write(

#                         f"{name},{domain},{salary}\n"
#                     )  
                    
#          except ValueError:
#                 print("Invalid record:",line)    


with open("record.txt","r",encoding="utf-8") as input_file:
    with open("bad_record.txt","w",encoding="utf-8") as error_file:

     for line in input_file:

        try:

          line=line.strip()
          name,role,salary=line.split(",")
        #   salary=-5000
        #   if salary<0:
        #    raise ValueError("Salary cannot be nagative")
          salary=int(salary)

          print(name,role,salary)

        except ValueError:
          error_file.write(line+"\n")

        