#class person
class Person:
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender
    
    # Implement a method called introduce that prints a message introducing the person with their name, age, and gender
    def introduce(self):
        print(f"My name is {self.name}, i am {self.age} year old and am a {self.gender}")
        
#instance of the Person class and call the introduce method to display the person's information      
info=Person("Linus",36,"Male")
info.introduce()