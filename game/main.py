# main.py will be the main file where the game logic will be written 
# game will be two player game so, make sure to work on alternative moves 
# As user input is required, but we are not allowed to use libraries other than 
# String random and math. The implementation will be simplistic and fun as user point of view 
from commander import Commander
from night import Knight
from soldier import Soldier
from archer import Archer
from wizard import Wizard
from seige_equipment import Seige


def show_intro():
    print("\t\t\t\t***** THE COMBAT GAME *****")
    print("*"*100)
    print("\tThis is a two player game where each player is a commander of an army.")
    print("\tEach commander has to choose his Units and is given $10 to choose his troops")
    print("\tEach unit(troop Example: knight, archer, soldier etc) will cost $1.")
    print("\tUnits shall fight in the order they were purchased")

def choose_units(commander):
    print("\t\t\t\t***** Instructions *****")
    print("\n")
    print("""Press the option to buy the unit :\n
        1. Knight \n
        2. Archer \n
        3. Soldier \n
        4. Seige \n
        5. Wizard \n
        6. Stop \n
        Example: Press 1 to buy knight""")
    while(commander.money_spent < commander.total_money):
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
            if choice == 1:
                commander.buy_units(Knight())
                print("knight added")
            elif choice == 2:
                commander.buy_units(Archer()) 
                print("archer added")
            elif choice == 3:
                commander.buy_units(Soldier())
                print("soldier added")    
            elif choice == 4:
                commander.buy_units(Seige())
                print("seige added")   
            elif choice == 5:
                commander.buy_units(Wizard())
                print("wizard added")                 
            elif choice == 6:
                print("Money left : {}".format(commander.total_money - commander.money_spent))
                break
            else:
                print("Enter only numbers from 1-6")
            print("Money left : {}".format(commander.total_money - commander.money_spent))
        except ValueError:
            print("Enter only numbers from 1-6")

    print("Remaining money will be used to buy medics")
    commander.buy_medics()

    print("{} medics bought".format(commander.medics))
    print("Commander {} you have units in order".format(commander))
    for i in commander.units:
        print(i)
    
    print(" ")
    
 
def name_for_commander(commander, number):
    print("\t\t\t***** It's time to choose name for commander *****")
    name = input("Enter name for commander {}: [default: commander{}]".format(number, number) )
    if len(name) != 0:
        commander.name = name 
    else:
        commander.name = '{}{}'.format(commander, number)

def fight(c1, c2):
    while(len(c1.units)>0 and len(c2.units) > 0):
        print("{} is fighting {}".format(str(c1.units[0]), str(c2.units[0])))
        if type(c1.units[0]) == type(c2.units[0]):
            c1.units.pop(0)
            c2.units.pop(0)
        else:
            if c1.units[0].stronger_than(c2.units[0].id):
                if c2.medics > 0:
                    unit = c2.units[0]
                    c2.units.append(unit)
                    c2.medics -=1
                c2.units.pop(0)
                
            else:
                if c1.medics > 0:
                    unit = c1.units[0]
                    c1.units.append(unit)
                    c1.medics -=1
                c1.units.pop(0)
    if len(c1.units) > len(c2.units):
        print("\t\t\t\t***** Congrats commander {}. You won the game. *****".format(c1.name))
    elif len(c1.units) == len(c2.units):
        print("\t\t\t\t****** No one won the game ******")
    else:
        print("\t\t\t\t***** Congrats commander {}. You won the game. *****".format(c2.name))

    print("Thankyou for playing")


def main():
    show_intro()

    # create a commander object for player one and two 
    print("It's time to choose name for your commander: ")
    c1 = Commander()
    c2 = Commander()
    name_for_commander(commander = c1, number = 1)

    name_for_commander(commander = c2, number = 2)
    choose_units(c1)
    choose_units(c2)
    fight(c1, c2)


if __name__ =="__main__":
    main()