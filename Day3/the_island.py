
print('''
     ___   ____
        /' --;^/ ,-_\     \ | /
       / / --o\ o-\ \\   --(_)--
      /-/-/|o|-|\-\\|\\   / | \
       '`  ` |-|   `` '
             |-|
             |-|O
             |-(\,__
          ...|-|\--,\_....
      ,;;;;;;;;;;;;;;;;;;;;;;;;,.
~~,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,  ______   ---------   _____     ------
''')
print ("Welcome to this stunning island, somewhere in the Pacific.")
print("Your mission is to stay alive until help arrives.")
print("You wake up on a beach having been washed ashore. "
      "You seem to have lost your memory and have no idea how you "
      "arrived here.")
food_shelter=input("Do you look for food and water or build a shelter"
                   " ('f' or 's'?): ").lower()
if food_shelter == "s":
    print("You somehow find the energy to build a shelter against some "
          "rocks a little way inland from the beach. The shelter protects"
          " you from the heat of the sun in the day and the tropical "
          "storms that frequently arrive at the island. You plan to find "
          "food and water after you rest. ")
    print("Feeling refreshed from your sleep you are motivated to find water.")

    cup_or_dive = input("As you walk from your shelter, you begin to hear the "
                        "sound of running water. You trace the sound to a "
                        "waterfall and lake. Do you cup your hands together "
                        "and sip the water from the waterfall or dive into the"
                        " lake and take huge gulps? ('c' or 'd'):").lower()

    if cup_or_dive == "c":
        print("You sip the cool refreshing water and enjoy the feeling of "
              "satisfying your thirst.")
        print("Now hydrated, your thoughts become clearer and you "
              "investigate the "
              "fruits hanging from nearby bushes as your tummy rumbles.")
        print("You focus your attention on food. After locating edible "
              "fruit, you consider your next move. ")

        raft_island_or_fire = input(
            "Do you make a raft to escape the island, live on the island "
            "for the rest of your life,"
            " or start a fire to attract passing vessels."
            "Type 'raft', 'island' or 'fire': ")

        if raft_island_or_fire == "fire":
            print("After some time you create bow to aid rubbing two sticks "
                  "together. With the use of coconut husk you manage to create "
                  "a flame. Success!")
            print("You think you see a ship in the distance and create smoke by"
                  " placing green foliage onto the fire")
            print("Upon spotting the smoke, the ship sends out a smaller "
                  "vessel to your island and you are rescued!")

        elif raft_island_or_fire == "raft":
            print("You make a raft from the branches of trees but as you "
                  "embark on "
                  "your seaward journey your tree branches come apart and "
                  "your "
                  "raft collapses. You are too far out to sea to swim back "
                  "to the island and drown.")
        # use \ backslash to escape a useful symbol, eg print('You\'re blue, type "B"')
        else:
            print(
                "You remain on the island and live a contented life until"
                " a bite from an angry trout turns septic and you die a "
                "painful death.")

    else:
        print("As you dive into the lake you strike your head on a huge rock, "
              " loose consciousness and drown")

else:

    print("You spend most of the day searching for and collecting food"
          " and water. Exhausted, you return to the beach. A tropical "
          "storm washes you and all of your hard work into the sea. "
          "It looks like your luck ran out! You are never seen again!")



