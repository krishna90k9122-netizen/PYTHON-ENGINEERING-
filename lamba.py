# salaries=[25000,5000,7000,9800,6500]

# new_salaries=list(map(lambda salary:salary*1.10,salaries))
# print(new_salaries)

# transaction=[500,1000,4000,800,900,600]
# large_transaction=list(
#     filter(lambda amount:amount>1000,transaction)
# )
# print(large_transaction)

# names=["krishna","sonu","nomu"]

# cleanname=list(map(lambda name:name.strip().upper(),names))

# print(cleanname)

transaction=[100,600,300,800,900,1100,8900]

valid_transaction=list(filter(lambda amout:amout>=1000,transaction))
print(valid_transaction)

with_tax=list(filter(lambda x:x>200, map(lambda salary:salary*1.18,transaction)))
print(with_tax)

rows=["krishna,delhi,50000",
      "rahul,gomoh,4000",
      "ganki,gomoh,30000"

      ]

names=list(map(lambda row: row.split(",")[0], rows))
print(names)

delhi_rows=list(filter(lambda rows:rows.split(",")[1]=="gomoh",rows))

print(delhi_rows)

