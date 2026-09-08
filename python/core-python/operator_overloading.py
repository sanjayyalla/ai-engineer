class Animal:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def __gt__(self,other):
        return self.age > other.age

cat = Animal("cat", 2)
dog = Animal("dog", 9)

print(cat > dog)