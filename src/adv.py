from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("outside", "Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("foyer", "Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("overlook", "Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("narrow", "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("treasure", "Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Items 

items = {
    'flashlight': Item("flashlight", """Lights up the room."""),
    'rock': Item("rock", """A rock."""),
    "rope": Item("rope", """A rope.""")
}

room['outside'].items.append(items['flashlight'])
room['foyer'].items.append(items['rock'])
room['treasure'].items.append(items['rope'])


def room_item_remover(command):
    for i in room[player.location].items:
        counter = -1
        counter = counter + 1
        if i.name == command:
            del(room[player.location].items[counter])

def player_item_remover(command):
    for i in player.items:
        counter = -1
        counter = counter + 1
        if i == command:
            del(player.items[counter])



#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('outside')

# Write a loop that:
while True:
    #
    # * Prints the current room name
    print(player.location)
    # * Prints the current description (the textwrap module might be useful here).
    # * Waits for user input and decides what to do.
    print(room[player.location].description)
    #
    room[player.location].print_items()
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.
    command = input("> ").split(',')

    if command[0] == 'q':
        break
    elif command[0] == 'n':
        # check if the player can move to the north
        if player.location != 'outside' and player.location != 'foyer' and player.location != 'narrow':
            print("Invalid entry")
        else:
            player.location = room[player.location].n_to.key
        # if there is, set that north room as the player's location 
    elif command[0] == 's':
        if player.location != 'overlook' and player.location != 'foyer' and player.location != 'treasure':
            print("Invalid entry")
        else:
            player.location = room[player.location].s_to.key
    elif command[0] == 'e':
        if player.location != 'foyer':
            print("Invalid entry")
        else:
            player.location = room[player.location].e_to.key
    elif command[0] == 'w':
        if player.location != 'narrow':
            print("Invalid entry")
        else:
            player.location = room[player.location].w_to.key
    elif command[0][:3] == 'get':
        player.items.append(items[command[0][4:]])
        room_item_remover(command[0][4:])
    elif command[0][:4] == 'drop':
        player_item_remover(command[0][5:])
        room[player.location].items.append(items[command[0][5:]])
    else:
        print("Invalid entry")