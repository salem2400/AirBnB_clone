#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89

print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")

my_model_json = my_model.to_dict()
print(my_model_json)

print("JSON of my_model:")
for key, value in my_model_json.items():
    print(f"\t{key}: ({type(value)}) - {value}")

print("--")

my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")

print(my_model is my_new_model)
