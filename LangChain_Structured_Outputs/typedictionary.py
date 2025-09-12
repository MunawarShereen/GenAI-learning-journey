from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    
    
new_person:  Person = Person(name="Alice", age=30)
print(new_person)