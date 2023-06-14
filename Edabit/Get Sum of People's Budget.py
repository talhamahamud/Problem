def get_budgets(list1):
    f=0
    for i in list1:
        f=f+i["budget"]

    print(f)

get_budgets([
  { "name": "John",  "age": 21, "budget": 29000 },
  { "name": "Steve",  "age": 32, "budget": 32000 },
  { "name": "Martin",  "age": 16, "budget": 1600 }
])