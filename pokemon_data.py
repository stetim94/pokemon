from math import floor
import random
attack_type = {
        "normal":  {"rock": 0.5,"ghost": 0},
        "fire":    {"fire": 0.5, "water": 0.5, "grass": 2, "bug": 2, "rock": 0.5, "dragon": 0.5},
        "water":   {"fire": 2, "water": 0.5, "grass": 0.5,"ground": 2, "rock": 2, "dragon": 0.5},
        "electric":{"water": 2, "electric": 0.5, "grass": 0.5, "ground": 0, "flying": 2, "dragon": 0.5},
        "grass":   {"fire": 0.5, "water": 2, "grass": 0.5, "poison": 0.5, "ground": 2, "flying": 0.5, "bug": 0.5, "rock": 2, "dragon": 0.5},
        "ice":     {"water": 0.5, "grass": 2, "ice": 0.5, "ground": 2, "flying": 2, "dragon": 2},
        "fighting":{"normal": 2, "ice": 2, "poison": 0.5, "flying": 0.5, "psychic": 0.5, "bug": 0.5, "rock": 2, "ghost": 0},
        "poison":  {"grass": 2, "poison": 0.5, "ground": 0.5, "bug": 2, "rock": 0.5, "ghost": 0.5},
        "ground":  {"fire": 2, "electric": 2, "grass": 0.5, "posion": 2, "flying": 0, "bug": 0.5, "rock": 2},
        "flying":  {"electric": 0.5, "grass": 2, "fighting": 2, "bug": 2, "rock": 0.5},
        "psychic": {"fighting": 2,"poison": 2, "psychic": 0.5},
        "bug":     {"fire": 0.5, "grass": 2, "fighting": 0.5, "poison": 2,"flying": 0.5, "psychic": 2},
        "rock":    {"fire": 2, "ice": 2,"fighting": 0.5, "ground": 0.5, "flying": 2, "bug": 2},
        "ghost":   {"normal": 0, "psychic": 0, "ghost": 2},
        "dragon":  {"dragon": 2}
}



thundershock = { "type" : "electric", "power":    40 , "acc": 1 ,     "pp" :   30   , "name": "thundershock"}
slam         = { "type" : "normal"  , "power":    80 , "acc": 0.75 ,  "pp" :   20   , "name": "slam"}
thunderbolt  = { "type" : "electric", "power":    95 , "acc": 1 ,     "pp" :   15   , "name": "thunderbolt"}
thunder      = { "type" : "electric", "power":    120, "acc": 0.7  ,  "pp" :   10   , "name": "thunder"}
horn_attack  = {  "type": "normal"  , "power":  65, "acc": 1,     "pp":  25         , "name": "horn_attack"}
poison_sting = {  "type": "poison"  , "power":  15, "acc": 1,     "pp":  35         , "name": "poison_sting"}
thrash       = {  "type": "normal"  , "power":  90, "acc": 1,     "pp":  20         , "name": "thrash"}
double_kick  = {  "type": "fighting", "power":  30, "acc": 1,     "pp":  30         , "name": "double_kick"}
confusion    = { "type" : "psychic" , "power" :  50 , "acc" : 1 , "pp" : 25         , "name": "confusion"}
psybeam      = { "type" : "psychic" , "power" :  65 , "acc" : 1 , "pp" : 20         , "name": "psybeam"}
psychic      = { "type" : "psychic" , "power" :  90 , "acc" : 1 , "pp" : 10         , "name": "psychic"}
doubleslap   = { "type" : "normal"  , "power" : 15  , "acc" : 0.85 , "pp" : 10      , "name": "doubleslap"}
body_slam    = { "type" : "normal"  , "power" : 85  , "acc" : 1    , "pp" : 15      , "name": "body_slam"}
double_edge  = { "type" : "normal"  , "power" : 100 , "acc" : 1    , "pp" : 15      , "name": "double_edge"}
ember        = { "type" : "fire"    , "power": 40 , "acc" : 1    , "pp" :  25       , "name": "ember"}
flamethrower = { "type" : "fire"    , "power": 95 , "acc" : 1    , "pp" :  15       , "name": "flamethrower"}
pound        = { "type" : "normal"  , "power" : 40 , "acc" :  1    , "pp" : 35      , "name": "pound"}
mega_punch   = { "type" : "normal"  , "power" : 80 , "acc" :  0.85 , "pp" : 20      , "name": "mega_punch"}
headbutt     = { "type" : "normal"  , "power" : 70 ,"acc" : 1     , "pp" : 15       , "name": "headbutt"}
aurora_beam  = { "type" : "ice"     , "power" : 65 ,"acc" : 1     , "pp" : 20       , "name": "aurora_beam"}
take_down    = { "type" : "normal"  , "power" : 90 ,"acc" : 0.85  , "pp" : 20       , "name": "take_down"}
ice_beam     = { "type" : "ice"     , "power" : 95 ,"acc" : 1     , "pp" : 10       , "name": "ice_beam"}
tackle       = { "type" : "normal"  , "power" : 35  , "acc": 0.95  , "pp" :  35     , "name": "tackle"}
swift        = { "type" : "normal"  , "power" : 60  , "acc": 1     , "pp" :  20     , "name": "swift"}
hydro_pump   = { "type" : "water"   , "power" : 120 , "acc": 0.8   , "pp" :  5      , "name": "hydro_pump"}
bubble       = { "type" : "water"   , "power": 20,  "acc": 1,     "pp":   30        , "name": "bubble"}
water_gun    = { "type" : "water"   , "power": 40 , "acc": 1,     "pp":   25        , "name": "water_gun"}
bite         = { "type" : "normal"  , "power": 60 , "acc": 1,     "pp":   25        , "name": "bite"}
skull_bash   = { "type" : "normal"  , "power": 100, "acc": 1,     "pp":   15        , "name": "skull_bash"}

pikachu_moves = [thundershock, slam, thunderbolt, thunder]
nidoking_moves = [horn_attack, poison_sting, thrash, double_kick]
alakazam_moves = [confusion, psybeam, psychic]
jigglypuff_moves = [pound, doubleslap, body_slam, double_edge]
growlithe_moves = [bite, ember, take_down, flamethrower]
mew_moves = [pound, mega_punch, psychic]
seel_moves = [headbutt, aurora_beam, take_down, ice_beam]
gyarados_moves = [bite, hydro_pump, tackle]
staryu_moves = [tackle, water_gun, swift, hydro_pump]
blastoise_moves = [bubble, water_gun, bite, skull_bash]


class Pokemon(object):
    def __init__(self,name, base_hp, base_attack, base_defense, base_speed, base_special, types, moves):
        self.name = name
        self.base_hp = base_hp
        self.base_attack = base_attack
        self.base_defense = base_defense
        self.base_speed = base_speed
        self.base_special = base_special
        self.types = types
        self.moves = moves
        self.stats()
    def stats(self):
        self.level = 50
        I = 0
        if self.base_attack % 2: I += 8
        if self.base_defense % 2: I += 4
        if self.base_speed % 2: I += 2
        if self.base_special % 2: I += 1
        self.attack = floor((2 * self.base_attack + I ) * self.level / 100 + 5)
        self.speed = floor((2 * self.base_speed + I ) * self.level / 100 + 5)
        self.defense = floor((2 * self.base_defense + I ) * self.level / 100 + 5)
        self.max_hp = floor((2 * self.base_hp + I) * self.level / 100 + self.level + 10)
        self.hp = self.max_hp
'''  
class Move:
   def __init__(self, move):
      self.move = move
      self.typen = move["type"]
      self.power = move["power"]
      self.acc = move["acc"]
      self.pp = move["pp"]
      self.name = move["name"]
'''
pikachu    =  Pokemon ("pikachu", 35,  55,  30,  90,  50, ["electric"],pikachu_moves)
nidoking   =  Pokemon ("nidoking", 81,  92,  77,  85,  75, ["poison","ground"],nidoking_moves )
alakazam   =  Pokemon ("alakazam", 55 ,  50,  45,  120,  135, ["psychic"],alakazam_moves)
jigglypuff =  Pokemon ("jigglypuff", 115,  45,  20,  20,  25, ["normal"],jigglypuff_moves )
growlithe  =  Pokemon ("growlithe", 55,  70,  45,  60,  50, ["fire"],growlithe_moves)
mew        =  Pokemon ("mew", 100,  100,  100 ,  100, 100, ["psychic"],mew_moves)
seel       =  Pokemon ("seel", 65,  45,  55,  45,  70, ["water"],seel_moves) 
gyarados   =  Pokemon ("gyarados", 95,  125,  79,  81,  100, ["water","flying"],gyarados_moves) 
staryu     =  Pokemon ("staryu", 30,  45,  55,  85,  70, ["water"],staryu_moves)
blastoise  =  Pokemon ("blastoise", 79,  83,  100,  78,   85, ["water"],blastoise_moves)

reinier = {pikachu : True, nidoking : True,alakazam : True,jigglypuff : True,growlithe : True,mew : True}
gym = {seel: True,gyarados: True,staryu: True,blastoise: True}

gym_pokemon = random.choice(list(gym.keys()))

def enumerate2(xs, start=0, step=1):
    for x in xs:
        yield (start, x)
        start += step