# sample text-based game with simple conditional statement
import random
import time
chr_attack = random.randint(25, 30)
g_slime_attack = random.randint(6, 20)
shadow_assassin_attack = random.randint(15, 25)
character_health = 100
item = ""


name = input("Username: ")
print("You're awake adventurer [" + name +"]")

while character_health > 0:
    if character_health != 100 and item == "Fish":
        n = input("You have taken some damage to heal select |1| to Heal, |0| to Ignore\nInput: ")
        if n == "1":
            character_health += 10
            print("Your character [" + name +"] health is back to " + str(character_health))
        else:
            print("Your character [" + name +"] health is back to " + str(character_health))

    v = int(input("Enter |1| to Cross the River\nEnter |2| to Jump into the Ravine\nEnter |3| to fight the Monster in the Dungeon \nInput: "))

    # Start of Journey
    if v == 1:
        choice = input("Do you want to go Fishing? Enter |1| if YES & |0| if NO\nInput: ")
        if choice == "1":
            # Fishing minigame
            print("You have chosen Fishing! ")
            chance = random.randint(0, 9)
            if chance > 6:
                item = "Fish"
                print("You caught a Fish!")
            else:
                print("There is no fish to catch")

        elif choice == "0":
            print("You [" + name +"] have crossed the river")


    elif v == 2:
        # damages the player
        print("You [" + name +"] have jumped into the Ravine")
        print("Your Character [" + name +"] has taken 10 Damage")
        character_health = character_health - 10

    elif v == 3:
        # damages the player
        print("You [" + name +"] have entered the Dungeon")
        print("You [" + name +"] have arrived at a Forked Cave")
        dungeon = input("What path will you take |L|eft, |M|iddle, |R|ight \n"
              "Input: ")
        if dungeon == "L":
            slime_hp = 50
            shadow_assassin_hp = 92
            print("You [" + name +"] have encountered a Green Slime" + " HP:" + str(slime_hp))
            time.sleep(2)
            left = input("Enter |A| to Attack, |E| to Escape \nInput: ")
            if left == "A":
                print("You [" + name +"] have chosen to attack the Green Slime")
                slime_hp = slime_hp - chr_attack
                if chr_attack >= 28:
                    print("Green Slime received " + str(chr_attack) + " [Critical] damage" + " HP:" + str(slime_hp))
                else:
                   print("Green Slime received " + str(chr_attack) + " damage" + " HP:" + str(slime_hp))

                #EnemyMobFightBack
                print("The Green Slime attacked")
                time.sleep(2)
                character_health = character_health - g_slime_attack
                print("You [" + name +"] have taken " + str(g_slime_attack) + " Damage from the Green Slime")
                print("Your character's Health: " + str(character_health))

            if left == "E":
                print("You've chosen to escape\nThe Green Slime chase you down")

            left = input("Enter |A| to Attack, |E| to Escape\nInput: ")
            if left == "A":
                    print("You [" + name +"] have chosen to attack the Green Slime")
                    slime_hp = slime_hp - chr_attack
                    if chr_attack >= 28:
                        print("Green Slime received " + str(chr_attack) + " [Critical] damage" + " HP:" + str(slime_hp))
                    else:
                        print("Green Slime received " + str(chr_attack) + " damage" + " HP:" + str(slime_hp))
                    time.sleep(2)
                    print("You [" + name +"] have defeated the Green Slime")
                    print("The Green Slime dropped Green Goo - used to make a lesser potion")
                    time.sleep(2)
                    print("You [" + name +"] have leveled up! \nYour Health has been restored")
                    character_health = 100

            if left == "E":
                print("You Escape Successfully")

            second_level = input("Do you want to continue to the 2nd Level [" + name +"] ? |Y|es or |N|o \nInput: ")
            if second_level == "Y":
                        print("You have arrived at the Second Level")
                        time.sleep(2)
                        print("A Shadow Assassin used sneak attack on you")
                        character_health = character_health - shadow_assassin_attack
                        print("You [" + name +"] received " + str(shadow_assassin_attack) + " Damage")
                        print("Your character's Health: " + str(character_health))
                        left_2 = input("Enter |A| to Attack, |E| to Escape \nInput: ")
                        if left_2 == "E":
                            print("You've chosen to escape\nYou Escape Successfully")
                        if left_2 == "A":
                            print("You [" + name +"] have chosen to attack the Shadow Assassin")
                            shadow_assassin_hp = shadow_assassin_hp - chr_attack
                            time.sleep(2)
                            if chr_attack >= 28:
                                print("Shadow Assassin received " + str(chr_attack) + " [Critical] damage" + " HP:" + str(shadow_assassin_hp))
                            else:
                                print("Shadow Assassin received " + str(chr_attack) + " damage" + " HP:" + str(shadow_assassin_hp))
                            time.sleep(2)
                            print("Shadow Assassin fought back")
                            character_health = character_health - shadow_assassin_attack
                            print("You [" + name +"] received " + str(shadow_assassin_attack) + " Damage")
                            print("Your character's Health: " + str(character_health))
                            left_3 = input("Enter |A| to Attack, |E| to Escape \nInput: ")
                            if left_3 == "E":
                                print("You've chosen to escape\nYou Escape Successfully")

                            if left_3 == "A":
                                print("You [" + name +"] have chosen to attack the Shadow Assassin")
                                shadow_assassin_hp = shadow_assassin_hp - chr_attack
                                time.sleep(2)
                                if chr_attack >= 28:
                                    print("Shadow Assassin received " + str(
                                        chr_attack) + " [Critical] damage" + " HP:" + str(shadow_assassin_hp))
                                else:
                                    print("Shadow Assassin received " + str(chr_attack) + " damage" + " HP:" + str(shadow_assassin_hp))
                                time.sleep(2)
                                print("Shadow Assassin fought back")
                                character_health = character_health - shadow_assassin_attack
                                print("You [" + name +"] received " + str(shadow_assassin_attack) + " Damage")
                                print("Your character's Health: " + str(character_health))
                                if left_3 == "E":
                                    print("You've chosen to escape\nYou Escape Successfully")
                                if left_3 == "A":
                                    print("You [" + name +"] have chosen to attack the Shadow Assassin")
                                    shadow_assassin_hp = shadow_assassin_hp - chr_attack
                                    time.sleep(2)
                                    if chr_attack >= 28:
                                        print("Shadow Assassin received " + str(
                                            chr_attack) + " [Critical] damage" + " HP:" + str(shadow_assassin_hp))
                                    else:
                                        print("Shadow Assassin received " + str(chr_attack) + " damage" + " HP:" + str(
                                            shadow_assassin_hp))
                                    time.sleep(2)
                                    print("Shadow Assassin fought back")
                                    character_health = character_health - shadow_assassin_attack
                                    print("You  [" + name +"] received " + str(shadow_assassin_attack) + " Damage")
                                    print("Your character's Health: " + str(character_health))
                                    if shadow_assassin_hp <= 0:
                                        print("You [" + name + "] have defeated the Shadow Assassin\nThe Shadow Assassin dropped Ninja Stars - a hidden weapon used by Shadow Assassin to attack")
                                        time.sleep(2)
                                        print("You [" + name +"] have leveled up! \nYour Health has been restored")
                                        character_health = 100
                                    left_3 = input("Enter |A| to Attack, |E| to Escape \nInput: ")
                                    if left_3 == "E":
                                        print("You've chosen to escape\nYou Escape Successfully")
                                    if left_3 == "A":
                                        print("You [" + name +"] have chosen to attack the Shadow Assassin")
                                        shadow_assassin_hp = shadow_assassin_hp - chr_attack
                                        time.sleep(2)
                                        if chr_attack >= 28:
                                            print("Shadow Assassin received " + str(
                                                chr_attack) + " [Critical] damage" + " HP:" + str(shadow_assassin_hp))
                                        else:
                                            print("Shadow Assassin received " + str(
                                                chr_attack) + " damage" + " HP:" + str(shadow_assassin_hp))
                                        time.sleep(2)
                                        print("Shadow Assassin fought back")
                                        character_health = character_health - shadow_assassin_attack
                                        print("You [" + name +"] received " + str(shadow_assassin_attack) + " Damage")
                                        print("Your character's Health: " + str(character_health))
                                        if shadow_assassin_hp <= 0:
                                            print("You have defeated the Shadow Assassin\nThe Shadow Assassin dropped Ninja Stars - a hidden weapon used by Shadow Assassin to attack")
                                            time.sleep(2)
                                            print("You [" + name +"] have leveled up! \nYour Health has been restored")
                                            character_health = 100


        elif dungeon == "M":
            print("You [" + name +"] found a Treasure chest")
            middle = input("|O| to Open the chest, |D| to Destroy the chest \n"
                           "Input: ")
            if middle == "O":
                print("You [" + name +"] have acquired the Greater Potion ")
                m1 = input("Do you want to Drink or Donate it? Enter |GLUP| to Drink |DONO| to Donate\nInput: ")
                if m1 == "GLUP":
                    print("Greater Potion - A potion that restore your health back to full")
                    character_health = 100
                elif m1 == "DONO":
                    print("The Greater Potion has been donated to the Orphanage lmao")
                else:
                    print("Invalid Input")
            elif middle == "D":
                print("The chest have been destroyed")

        elif dungeon == "R":
            print("You [" + name +"] have fallen through the Dungeon hole")
            print("You [" + name +"] have taken 50 damage")
            character_health = character_health - 50
            time.sleep(2)
            gsauce_attack = 1000
            print("A wild Gsauce appeared\nGsauce used Holy Spank")
            character_health = character_health - gsauce_attack
            print("Your character's Health: " + str(character_health))
            if character_health <= 0:
                print("you ded lmao\nGAME OVER")

    else:
        print("Invalid input")

    print("Your character's Health: " + str(character_health))
if character_health > 0:
    print("Your Character [" + name +"] is dead lmao")