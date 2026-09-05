try:
  with open("monu.txt","r",encoding="utf-8") as input_file:
     with open("selected_monu.txt","w",encoding="utf-8") as output_file:

        for line in input_file:
             try:
                line=line.strip()
                name,role,salary=line.split(",")
                salary=int(salary)

                if salary<0:
                  raise ValueError("nagative value")

                if role=="data engineer" and salary>=50000:

                    output_file.write(
                        f"{name},{role},{salary}\n"
                    )  

             except ValueError:
                print("bad error:",line)

except FileNotFoundError:
        print("input the not found")    