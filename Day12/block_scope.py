#Python does not have block scope like some other programming languages
#Variables nested in blocks like: loops, if statements, while loops etc. dont get
#local scope
#athey are given function scope if within a function, or global scope if not.

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]


#def create_enemy():
if game_level < 5:
    new_enemy = enemies[0] #prints skeleton but if put in a function new_enemy cannot be printed as local scope

print(new_enemy)