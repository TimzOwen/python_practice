from unicodedata import name


my_dictionary = {"name":"Timz","age":22,"Role":"Developer"}
my_dictionary2 = dict(user="Owen",staff="Engineer",laptop="HP")

my_dictionary.update(my_dictionary2)
print(my_dictionary)

for x in my_dictionary2.items():
    print(x)
