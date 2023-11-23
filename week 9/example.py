
'''
# human.py
class Human:
    MAX_ENERGY = 100

    def __init__(self, name="Human", age=0):
        self.name = name
        self.age = age
        self.energy = self.MAX_ENERGY

    def display(self):
        print(f"I am {self.name}")

# robot.py
class Robot:
    MAX_ENERGY = 100

    def __init__(self, name="Robot", age=0):
        self.name = name
        self.age = age
        self.energy = 0  # Default energy set to 0 for robots

    def display(self):
        print(f"I am {self.name}")

# main.py
if __name__ == "__main__":
    from human import Human
    from robot import Robot

    human = Human()
    human.display()

    robot = Robot()
    robot.display()
'''
'''
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        # Formal string representation for the object
        return f'Human(name={self.name}, age={self.age})'

    def __str__(self):
        # Informal string representation for display
        return f'{self.name} is {self.age} years old.'

class Robot:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        # Formal string representation for the object
        return f'Robot(name={self.name}, age={self.age})'

    def __str__(self):
        # Informal string representation for display
        return f'Robot {self.name} is {self.age} years old.'

# Example usage:
human = Human("Alice", 25)
robot = Robot("Bender", 30)

# Using __str__
print(human)  # Output: Alice is 25 years old.
print(robot)  # Output: Robot Bender is 30 years old.

# Using __repr__
print(repr(human))  # Output: Human(name=Alice, age=25)
print(repr(robot))  # Output: Robot(name=Bender, age=30)
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        # Formal string representation for the object
        return f'Human(name={self.name}, age={self.age})'

    def __str__(self):
        # Informal string representation for display
        return f'{self.name} is {self.age} years old.'

class Robot:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        # Formal string representation for the object
        return f'Robot(name={self.name}, age={self.age})'

    def __str__(self):
        # Informal string representation for display
        return f'Robot {self.name} is {self.age} years old.'

# Example usage:
human = Human("Alice", 25)
robot = Robot("Bender", 30)

# Using __str__
print(human)  # Output: Alice is 25 years old.
print(robot)  # Output: Robot Bender is 30 years old.

# Using __repr__
print(repr(human))  # Output: Human(name=Alice, age=25)
print(repr(robot))  # Output: Robot(name=Bender, age=30)
'''
'''
class Human:
    MAX_ENERGY = 100

    def __init__(self, name, age, energy):
        self.name = name
        self.age = age
        self.energy = energy

    def grow(self):
        """Increase the age of the human by 1."""
        self.age += 1

    def eat(self, amount):
        """
        Increase the energy of the human by the given amount.
        Note: Energy should not exceed MAX_ENERGY.
        """
        self.energy += amount
        self.energy = min(self.energy, self.MAX_ENERGY)

    def move(self, distance):
        """
        Reduce the energy of the human by the given distance.
        Note: Energy should not fall below 0.
        """
        self.energy -= distance
        self.energy = max(self.energy, 0)


class Robot:
    MAX_ENERGY = 100

    def __init__(self, name, age, energy):
        self.name = name
        self.age = age
        self.energy = energy

    def grow(self):
        """Increase the age of the robot by 1."""
        self.age += 1

    def eat(self, amount):
        """
        Increase the energy of the robot by the given amount.
        Note: Energy should not exceed MAX_ENERGY.
        """
        self.energy += amount
        self.energy = min(self.energy, self.MAX_ENERGY)

    def move(self, distance):
        """
        Reduce the energy of the robot by the given distance.
        Note: Energy should not fall below 0.
        """
        self.energy -= distance
        self.energy = max(self.energy, 0)

# Example usage:
human = Human("Alice", 25, 80)
robot = Robot("Robo", 2, 90)

human.grow()
robot.grow()

human.eat(20)
robot.eat(30)

human.move(10)
robot.move(15)

print(f"{human.name} - Age: {human.age}, Energy: {human.energy}")
print(f"{robot.name} - Age: {robot.age}, Energy: {robot.energy}")
'''


class Human:
    def __init__(self, name):
        self.name = name

class Robot:
    def __init__(self, model):
        self.model = model

class Planet:
    def __init__(self, name):
        # Initialize the instance variables
        self.humans = []  # List to store human objects
        self.robots = []  # List to store robot objects
        self.name = name  # String representing the name of the planet

    def add_human(self, human):
        # Adds a human object to the list of humans
        self.humans.append(human)

    def remove_human(self, human):
        # Removes a human object from the list of humans
        if human in self.humans:
            self.humans.remove(human)
        else:
            print(f"{human} not found on {self.name}.")

    def add_robot(self, robot):
        # Adds a robot object to the list of robots
        self.robots.append(robot)

    def remove_robot(self, robot):
        # Removes a robot object from the list of robots
        if robot in self.robots:
            self.robots.remove(robot)
        else:
            print(f"{robot} not found on {self.name}.")

    def __repr__(self):
        # Returns a formal representation of a planet object
        return f"Planet(name='{self.name}', humans={self.humans}, robots={self.robots})"

    def __str__(self):
        # Returns an informal representation of a planet object
        return f"Planet: {self.name}\nHumans: {', '.join([human.name for human in self.humans])}\nRobots: {', '.join([robot.model for robot in self.robots])}"

# Example usage and testing
if __name__ == "__main__":
    # Create human and robot objects
    alice = Human("Alice")
    bob = Human("Bob")
    r2d2 = Robot("R2-D2")
    c3po = Robot("C-3PO")

    # Create a planet object
    earth = Planet("Earth")

    # Add humans and robots to the planet
    earth.add_human(alice)
    earth.add_human(bob)
    earth.add_robot(r2d2)
    earth.add_robot(c3po)

    # Display the informal representation of the planet
    print(str(earth))

    # Remove a human and a robot from the planet
    earth.remove_human(alice)
    earth.remove_robot(c3po)

    # Display the formal representation of the planet
    print(repr(earth))



