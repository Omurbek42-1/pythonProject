class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        def info(self):
            return (f'{self.name} is {self.age} years old.
                    f'Birth year is {2024 - self.age}')


some_animal = Animal(name='Anim', age=2)
some_animal.age = -3
print(some_animal.info())