enemies = 1

def increase_enemies():
    enemies = 2
    print (f"enemies inside function: {enemies}")#output = 2

increase_enemies()
print(f"enemies outside function: {enemies}")#output = 1

#Local Scope
#def drink_potion():
    #potion_strength = 2
    #print(potion_strength)

#drink_potion()
#print(potion_strength)#error occurs saying name is not defined due to local scope. variable only accessible inside the function

#Global Scope
player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()
print(player_health)