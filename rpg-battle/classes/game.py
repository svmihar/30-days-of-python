import random
from .magic import Spell
import pprint 

class bcolors:
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'

class person():
	def __init__(self, name, hp, mp, attack, defense, magic, items):
		self.maxhp = hp #biar gak over restore
		self.hp = hp
		self.maxmp = mp
		self.mp = mp
		self.attack_low = attack - 10
		self.attack_high = attack + 10
		self.defense = defense
		self.magic = magic
		self.items = items
		self.actions = ["Attack", "Magic", "Items"]
		self.name = name

	def generate_damage(self): 
		return random.randrange(self.attack_low, self.attack_high)

	def take_damage(self, damage):
		self.hp -= damage
		if self.hp < 0:
			self.hp = 0
		return self.hp

	def get_hp(self):
		return self.hp
	
	def get_max_hp(self):
		return self.maxhp

	def get_mp(self):
		return self.mp
	
	def get_max_mp(self):
		return self.maxmp

	def reduce_mp(self, cost):
		self.mp -= cost
	
	def get_spell_name(self, i):
		return self.magic[i]["name"]

	def get_spell_mp_cost(self, i):
		return self.magic[i]["cost"]


	def heal(self, damage):
		self.hp += damage
		if self.hp > self.maxhp:
			self.hp = self.maxhp
	
	def choose_actions(self): 
		i = 1
		print("---------------------")
		print("ACTIONS")
		print("---------------------")
		for item in self.actions:
			print("\t" + str(i) + ":", item)
			i += 1
			
	def choose_spell(self):
		i=1
		print("---------------------")
		print("MAGIC")
		print("---------------------")
		for spell in self.magic:
			print("\t" + str(i) + ":", spell.name, "(cost:", str(spell.cost) + ")")
			i+=1
	def choose_item(self): 
		i = 1
		print("---------------------")
		print("ITEMS")
		print("---------------------")
		for item in self.items:
			print("\t" + str(i), ":", item["item"].name + ":", item["item"].desc +"\t", " (x" + str(item["quantity"]) + ")")
			i+=1

			
	def get_stats(self):
		print("                 _________________________             __________")
		print(self.name + "  " + str(self.hp) + "/" + str(self.maxhp) + "|█████████████████████████|      "+str(self.mp) +"/" + str(self.maxmp) + "|██████████|")
