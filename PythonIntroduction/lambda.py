
people = [
    {"name":"harry", "house":"grffindor"},
{"name":"cho", "house": "ravenclaw"},
{"name":"draco", "house":"slytherin"}
]

# def f(person):
#     return  person["house"]
#
# people.sort(key=f)
# print(people)

# or we can sort by using the function lambda that is condesed
# function of upper form

people.sort(key=lambda person: person["name"])

print(people)
