from random import randint
dice_images = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
dice_num = randint (1, 6)#change to (0, 5)
print(dice_images[dice_num])

#bug due to randint not being (0, 5) image in position 0 and position 6 do not exist