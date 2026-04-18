class Animal: 
    def speak(self):
        print("Animal Makes a Sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

dog1= Dog()
dog1.speak()