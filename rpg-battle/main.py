from classes.game import person, bcolors
from classes.magic import Spell
from classes.inventory import item

print("\n\n")
print("NAME             HP                                    MP")
#create black magic 
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("thunder", 10, 100, "black")
blizzard = Spell("blizzard", 10, 100, "black")
meteor = Spell("meteor", 20, 200, "black")
quake = Spell("quake", 14, 140, "black")

#create white magic 
cure = Spell("cure", 12,120, "white")
cureMore = Spell("cureMore", 18,200, "white")


#create some items
potion = item("potion", "potion", "heals 50 HP", 50)
hiPotion = item("high potion", "potion", "heals 100 HP", 100)
superPotion = item("super potion", "potion", "heals 500 HP", 500)
elixir = item("elixir", "elixir", "fully restores HP/MP of current char", 9999)
megaelixir = item("mega elixir", "elixir", "fully restores HP/MP of all char", 9999)
grenade = item("grenade", "attack", "deals 500 damage", 500)

player_magic = [fire, thunder, blizzard, meteor, cure, cureMore]
player_items = [{"item":potion, "quantity":15}, {"item":hiPotion, "quantity":25}, {"item":superPotion, "quantity":5}, {"item":elixir, "quantity":35}, {"item":megaelixir, "quantity":15}, {"item":grenade, "quantity":5}]

#instantiate people
player0 = person("svmihar:",3500, 65, 60, 34, player_magic, player_items)
player1 = person("kezia_mb:", 5500, 65, 60, 34, player_magic, player_items)
player2 = person("robot:", 1000, 65, 60, 34, player_magic, player_items)

players = [player0, player1, player2] 

#instantiate enemy
enemy = person("enemy",1200, 65, 45, 25, [], [])



running = True
i=0

# print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)
# print("this is a normal text")


while running:
    for player in players:
        player.get_stats()
    print("\n")
    for player in players: 
        player.choose_actions()
        choice = input("Choose Actions: ")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print("You attacked for " + str(dmg), "points of damage.")
        elif index ==1:
            player.choose_spell()
            magic_input = int(input("Choose Magic: ")) - 1
            if magic_input == -1:
                continue

            spell = player.magic[magic_input]
            magic_dmg = spell.generate_damage()
            cost = spell.cost 

            
            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print("Not enough MP")
                continue
            player.reduce_mp(spell.cost)

            if spell.type =="white":
                player.heal(magic_dmg)
                print("\n"+spell.name+" heals for ", str(magic_dmg), "HP")
            elif spell.type=="black":
                enemy.take_damage(magic_dmg)
                print("\n", spell.name, "deals", str(magic_dmg), "points of damage")
        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose Item: ")) -1
            
            if item_choice ==-1:
                continue
            
            if player.items[item_choice]["quantity"] == 0:
                print("No " + player.items[item_choice]["item"].name + " left")
                continue
            
            item = player.items[item_choice]["item"]
            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print("\n"+item.name + " heals for", str(item.prop) + " HP" )
            elif item.type == "elixir":
                player.hp = player.maxhp
                player.mp = player.maxmp
                print(item.name + " fully restores HP/MP")
            elif item.type == "attack":
                enemy.take_damage(item.prop)
                print("Enemy take damage by", str(item.prop), "points of damage")


    
    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player1.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg)

    if(enemy.get_hp() == 0):
        print("enemy deaded \nyou won")
        running = False
    elif player.get_hp() == 0:
        print("you dieded")
        running = False

 