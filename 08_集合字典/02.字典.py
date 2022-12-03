my_dict = {
    "brand": "mitsubishi",
    "model": "EVO",
    "price": 500000,
    "???":"???"
}
print(my_dict)
print(my_dict.get('price'))
my_dict.pop("???")
print(my_dict)
my_dict.update({"price": 1000000})
print(my_dict)

print(my_dict.keys())
print(my_dict.values())