#A classic mini-RPG (role-playing game) with hp health points,
# character moves like attack/block/health, 
# and NPCs (non-player characters) that attacks based on a random number generator.
# The game ends when the player or the NPC dies.
# In each step of the adventure, the player should be presented with 2 or more options on where to go next.

import random
import sys

# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack = 10
        self.block = random.randint(1, 5) # --> Check if the random values are working

# NPC base class
class NPC:
    def __init__(self, hp, attack, block, class_name):
        self.hp = hp
        self.attack = attack
        self.block = block
        self.class_name = class_name

# Goblin class (inherits from NPC)
class Goblin(NPC):
    def __init__(self):
        super().__init__(hp=50, attack=random.randint(3, 7), block=random.randint(1, 3), class_name = 'Goblin') # --> Check if the random values are working

#Spider class (inherits from NPC)
class Spider(NPC):
    def __init__(self):
        super().__init__(hp=60, attack=random.randint(5, 10), block=random.randint(3, 4), class_name = 'Spider') # --> Check if the random values are working

#Wolf class (inherits from NPC)
class Wolf(NPC):
    def __init__(self):
        super().__init__(hp=65, attack=random.randint(6, 10), block=random.randint(2, 5), class_name = 'Wolf') # --> Check if the random values are working

# Orc class (inherits from NPC)
class Orc(NPC):
    def __init__(self):
        super().__init__(hp=60, attack=random.randint(4, 7), block=random.randint(2, 5), class_name = 'Orc') # --> Check if the random values are working

#Dragon class (inherits from NPC)
class Dragon(NPC):
    def __init__(self):
        super().__init__(hp=100, attack=random.randint(10, 15), block=random.randint(4, 7), class_name = 'Dragon') # --> Check if the random values are working

# Attack function
def attack(player, npc):
    if player.attack > npc.block:
        player_damage = player.attack
        
    else:
        player_damage = 0
        print(f'The {npc.class_name} blocked your attack')
        
    if npc.attack > player.block:
        npc_damage = npc.attack
        
    else:
        npc_damage = 0
        print(f'You blocked the {npc.class_name} attack')

    player.hp -= npc_damage
    npc.hp -= player_damage
    print(f'{player.name} received {npc_damage} damage and dealt {player_damage} damage')
    print(f'Your HP: {player.hp}')
    print(f'{npc.class_name} HP: {npc.hp}')
    
    if player.hp <= 0:
        print('You died')
        return False
    elif npc.hp <= 0:
        print(f'You killed the {npc.class_name}')
        return False
    
    return True

# Game Area1
def game_area1(player):
    while True:
        print('You are in the forest')
        print('Your path is blocked by a river and you have 3 options:')
        print('1. Swim across the river')
        print('2. Go around the river')
        print('3. Build a bridge')
        choice = input('\nMake your choice: ')
        if choice == '1':
            print('You tried to swim across the river...')
            if random.randint(1, 2) == 1:
                print('You made it across the river!\n')
                game_area2()
                continue
            else:
                print('You drowned in the river!')
                player.hp = 0
                break
        elif choice == '2':
            print('You went around the river and found a chest')
            print('You opened the chest and found a sword')
            player.attack += 5
            print(f'Your attack increased by 5\nYou cant go futher, {player.name} checks the sword and goes back to the forest')
            break
        elif choice == '3':
            print('You try to build a bridge...')
            print('You see a creature approaching...')
            npc_type = random.choice(['Goblin', 'Orc'])
    
            if npc_type == 'Goblin':
                npc = Goblin()
                print('A Goblin appeared!')
            else:
                npc = Orc()
                print('An Orc appeared!')

            while True:
                print('What do you want to do?')
                print('1. Attack')
                print('2. Run')
                choice = input('Choose 1 or 2: ')
                if choice == '1':
                    if not attack(player, npc):
                        break  # End combat if either the player or NPC dies
                elif choice == '2':
                    print('You ran away')
                    break  # End combat and the player runs away
                else:
                    print('Invalid choice')
                    break
        else:
            print('Invalid choice')

#Game Area2
def game_area2():
    while True:
        print('You are now entering a cave')
        print('You can go to the left or right')
        print('Choose (1)to go left or (2) right')
        choice = input('Make your choice: ')
        if choice == '1':
            print('A strange creature appears from the shadows')
            npc_type = random.choice(['Spider', 'Wolf'])
    
            if npc_type == 'Spider':
                npc = Spider()
                print('A Spider appeared!')
            else:
                npc = Wolf()
                print('A Wolf appeared!')
            while True:
                print('What do you want to do?')
                print('1. Attack')
                print('2. Run')
                choice = input('Choose 1 or 2: ')
                if choice == '1':
                    if not attack(player, npc):
                        break  # End combat if either the player or NPC dies
                elif choice == '2':
                    print('You ran away')
                    break  # End combat and the player runs away
                else:
                    print('Invalid choice')
                    break
        elif choice == '2':
            print('You see a tabern with a merchant and some good folks gathered around drinking and eating')
            print('What do you want to do?')
            print('1. Aproach the tabern')
            print('2. Go back to the forest')
            choice = input('Choose 1 or 2: ')
            if choice == '1':
                print('You aproach the tabern and see a merchant')
                print('What do you want to do?')
                print('1. Buy a potion')
                print('2. Talk to the merchant')
                choice = input('Choose 1 or 2: ')
                if choice == '1':
                    print('You bought a potion')
                    if player.hp <= 90:
                        player.hp += 10
                        continue
                    elif player.hp > 90:
                        player.hp = 100
                        continue
                    print('Your HP:', player.hp)
                elif choice == '2':
                    print('The merchant tells you a story...')
                    continue
                else:
                    print('Invalid choice')
                    break
            elif choice == '2':
                game_area1()
                break
            else:
                print('Invalid choice')
                break
        else:
            print('Invalid choice')
            break    
       

def main_game_loop(player):
    while player.hp > 0:
        #Game Logic
        game_area1(player)

        if player.hp <= 0:
            print(f"{player.name} has been defeated!")
            break
        else:
            print("")
            continue

if __name__ == "__main__":
    start = input("Press (1) to start the game or (2) to exit: \n")
    if start == '1':
        print("Welcome to the game!")
        print("You are about to embark on a dangerous adventure.\n")
        player_name = input("Enter your player's name: ")
        player = Player(player_name)
        print(f"Welcome, {player.name}!\n")
        main_game_loop(player)
    else:
        print("Goodbye!")
        sys.exit()