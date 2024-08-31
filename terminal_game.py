#A classic mini-RPG (role-playing game) with hp health points,
# character moves like attack/block/health, 
# and NPCs (non-player characters) that attacks based on a random number generator.
# The game ends when the player or the NPC dies.
# In each step of the adventure, the player should be presented with 2 or more options on where to go next.

import random

# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack = 10
        self.block = random.randint(1, 5)

# NPC base class
class NPC:
    def __init__(self, hp, attack, block):
        self.hp = hp
        self.attack = attack
        self.block = block

# Goblin class (inherits from NPC)
class Goblin(NPC):
    def __init__(self):
        super().__init__(hp=50, attack=random.randint(5, 10), block=random.randint(1, 3))

# Orc class (inherits from NPC)
class Orc(NPC):
    def __init__(self):
        super().__init__(hp=60, attack=random.randint(7, 10), block=random.randint(2, 5))

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
        choice = input('Make your choice: ')
        if choice == '1':
            print('You tried to swim across the river...')
            if random.randint(1, 2) == 1:
                print('You made it across the river')
                break
            else:
                print('You drowned in the river')
                player.hp = 0
                break
        elif choice == '2':
            print('You went around the river and found a chest')
            print('You opened the chest and found a sword')
            player.attack += 5
            print('Your attack increased by 5')
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
        
       

def main_game_loop(player):
    while player.hp > 0:
        #Game Logic
        game_area1(player)

        if player.hp <= 0:
            print(f"{player.name} has been defeated!")
            break
        else:
            print("You survived the encounter! Prepare for the next battle.\n")

if __name__ == "__main__":
    player_name = input("Enter your player's name: ")
    player = Player(player_name)
    print(f"Welcome, {player.name}!")
    main_game_loop(player)