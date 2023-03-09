class Animal:
    def speak(self):
        print("The animal makes a sound")


class Dog(Animal):
    def speak(self):
        super().speak()
        print("The dog barks")


class Cat(Animal):
    def speak(self):
        super().speak()
        print("The cat meows")