# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, key, name, description):
        self.key = key
        self.name = name
        self.description = description
        self.items = []

    def print_items(self):
        if len(self.items) > 0:
            for i in self.items:
                print(i.name)