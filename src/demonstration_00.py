"""
Below, you'll find a class definition for animals. Create two new animals `cat`
and `dog`. Set `cat` to have a name of "Purrfect", kind of "cat",
and color of "brown". Set `dog` to have a name of "Fido",
kind of "dog", and color of "black".
"""
class Animal:
    # Class variables if same for all instances. Instance variables if each instance can define these differently
    # name = ""
    # kind = ""
    # color = ""

    def __init__(self, name, kind, color):
        self.name = name
        self.kind = kind
        self.color = color

    def description(self):
        # Class method - all instances of the Animal class can do this
        # return "%s is a %s %s." % (self.name, self.color, self.kind)
        return f'{self.name} is a {self.color} {self.kind}.' # Equivalent to above line. Just like template string literals in javascript using backticks ``

# Create instances of Animal here and modify the instance attributes
# as described above.

# YOUR CODE HERE
coolCat = Animal("Joshcat", "very cool cat", "black")
cuteDog = Animal("Joshdog", "bernadoodlde", "brown and white")

# Should print Purrfect is a brown cat.
print(coolCat.description())
# Should print Fido is a black dog.
print(cuteDog.description())