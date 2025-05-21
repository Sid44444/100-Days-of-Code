#Modifying Global Scope

enemies = 1

def increase_enemies(enemy):
    #global enemies #Dont do this very often as it is confusing
    print (f"enemies inside function: {enemies}")#output = 2
    return enemy + 1

enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")#output = 1