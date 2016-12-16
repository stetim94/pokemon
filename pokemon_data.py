from math import floor
import random

# effectivines of attack against defending pokemon
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
        "dragon":  {"dragon": 2},
        "dark":    {"fighting": 0.5, "psychic": 2, "ghost": 2, "dark": 0.5}
}

# possible moves/attacks
absorb         = { "type": "grass"   , "category": "special" , "acc": 1   ,"power": 20 ,"pp": 25, "name": "absorb"}
acid           = { "type": "poison"  , "category": "special" , "acc": 1   ,"power": 40 ,"pp": 30, "name": "acid"}
acid_armor     = { "type": "poison"  , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 20, "name": "acid armor"}
agility        = { "type": "psychic" , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 30, "name": "agility"}
amnesia        = { "type": "psychic" , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 20, "name": "amnesia"}
aurora_beam    = { "type": "ice"     , "category": "special" , "acc": 1   ,"power": 65 ,"pp": 20, "name": "aurora beam"}
barrage        = { "type": "normal"  , "category": "physical", "acc": 0.85,"power": 15 ,"pp": 20, "name": "barrage"}
barrier        = { "type": "psychic" , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 20, "name": "barrier"}
bide           = { "type": "normal"  , "category": "physical", "acc": 1   ,"power": 0  ,"pp": 10, "name": "bide"}
bind           = { "type": "normal"  , "category": "physical", "acc": 0.85,"power": 15 ,"pp": 20, "name": "bind"}
bite           = { "type": "dark"    , "category": "physical", "acc": 1   ,"power": 60 ,"pp": 25, "name": "bite"}
blizzard       = { "type": "ice"     , "category": "special" , "acc": 0.7 ,"power": 110,"pp": 5 , "name": "blizzard"}
body_slam      = { "type": "normal"  , "category": "physical", "acc": 1   ,"power": 85 ,"pp": 15, "name": "body slam"}
bone_club      = { "type": "ground"  , "category": "physical", "acc": 0.85,"power": 65 ,"pp": 20, "name": "bone club"}
bonemerang     = { "type": "ground"  , "category": "physical", "acc": 0.9 ,"power": 50 ,"pp": 10, "name": "bonemerang"}
bubble         = { "type": "water"   , "category": "special" , "acc": 1   ,"power": 40 ,"pp": 30, "name": "bubble"}
bubble_beam    = { "type": "water"   , "category": "special" , "acc": 1   ,"power": 65 ,"pp": 20, "name": "bubble beam"}
clamp          = { "type": "water"   , "category": "physical", "acc": 0.85,"power": 35 ,"pp": 10, "name": "clamp"}
comet_punch    = { "type": "normal"  , "category": "physical", "acc": 0.85,"power": 18 ,"pp": 15, "name": "comet punch"}
confuse_ray    = { "type": "ghost"   , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 10, "name": "confuse ray"}
confusion      = { "type": "psychic" , "category": "special" , "acc": 1   ,"power": 50 ,"pp": 25, "name": "confusion"}
constrict      = { "type": "normal"  , "category": "physical", "acc": 1   ,"power": 10 ,"pp": 35, "name": "constrict"}
conversion     = { "type": "normal"  , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 30, "name": "conversion"}
counter        = { "type": "fighting", "category": "physical", "acc": 1   ,"power": 0  ,"pp": 20, "name": "counter"}
crabhammer     = { "type": "water"   , "category": "physical", "acc": 0.9 ,"power": 100,"pp": 10, "name": "crabhammer"}
cut            = { "type": "normal"  , "category": "physical", "acc": 0.95,"power": 50 ,"pp": 30, "name": "cut"}
defense_curl   = { "type": "normal"  , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 40, "name": "defense curl"}
dig            = { "type": "ground"  , "category": "physical", "acc": 1   ,"power": 80 ,"pp": 10, "name": "dig"}
disable        = { "type": "normal"  , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 20, "name": "disable"}
dizzy_punch    = { "type": "normal"  , "category": "physical", "acc": 1   ,"power": 70 ,"pp": 10, "name": "dizzy punch"}
double_kick    = { "type": "fighting", "category": "physical", "acc": 1   ,"power": 30 ,"pp": 30, "name": "double kick"}
double_slap    = { "type": "normal"  , "category": "physical", "acc": 0.85,"power": 15 ,"pp": 10, "name": "double slap"}
double_team    = { "type": "normal"  , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 15, "name": "double team"}
double_edge    = { "type": "normal"  , "category": "physical", "acc": 1   ,"power": 120,"pp": 15, "name": "double_edge"}
dragon_rage    = { "type": "dragon"  , "category": "special" , "acc": 1   ,"power": 0  ,"pp": 10, "name": "dragon rage"}
dream_eater    = { "type": "psychic" , "category": "special" , "acc": 1   ,"power": 100,"pp": 15, "name": "dream eater"}
drill_peck     = { "type": "flying"  , "category": "physical", "acc": 1   ,"power": 80 ,"pp": 20, "name": "drill peck"}
earthquake     = { "type": "ground"  , "category": "physical", "acc": 1   ,"power": 100,"pp": 10, "name": "earthquake"}
egg_bomb       = { "type": "normal"  , "category": "physical", "acc": 0.75,"power": 100,"pp": 10, "name": "egg bomb"}
ember          = { "type": "fire"    , "category": "special" , "acc": 1   ,"power": 40 ,"pp": 25, "name": "ember"}
explosion      = { "type": "normal"  , "category": "physical", "acc": 1   ,"power": 250,"pp": 5 , "name": "explosion"}
fire_blast     = { "type": "fire"    , "category": "special" , "acc": 0.85,"power": 110,"pp": 5 , "name": "fire blast"}
fire_punch     = { "type": "fire"    , "category": "physical", "acc": 1   ,"power": 75 ,"pp": 15, "name": "fire punch"}
fire_spin      = { "type": "fire"    , "category": "special" , "acc": 0.85,"power": 35 ,"pp": 15, "name": "fire spin"}
fissure        = { "type": "ground"  , "category": "physical", "acc": 1   ,"power": 0  ,"pp": 5 , "name": "fissure"}
flamethrower   = { "type": "fire"    , "category": "special" , "acc": 1   ,"power": 90 ,"pp": 15, "name": "flamethrower"}
flash          = { "type": "normal"  , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 20, "name": "flash"}
fly            = { "type": "flying"  , "category": "physical", "acc": 0.95,"power": 90 ,"pp": 15, "name": "fly"}
focus_energy   = { "type": "normal"  , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 30, "name": "focus energy"}
fury_attack    = { "type": "normal"  , "category": "physical", "acc": 0.85,"power": 15 ,"pp": 20, "name": "fury attack"}
fury_swipes    = { "type": "normal"  , "category": "physical", "acc": 0.8 ,"power": 18 ,"pp": 15, "name": "fury swipes"}
glare          = { "type": "normal"  , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 30, "name": "glare"}
growl          = { "type": "normal"  , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 40, "name": "growl"}
growth         = { "type": "normal"  , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 40, "name": "growth"}
guillotine     = { "type": "normal"  , "category": "physical", "acc": 1   ,"power": 0  ,"pp": 5 , "name": "guillotine"}
gust           = { "type": "flying"  , "category": "special" , "acc": 1   ,"power": 40 ,"pp": 35, "name": "gust"}
harden         = { "type": "normal"  , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 30, "name": "harden"}
haze           = { "type": "ice"     , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 30, "name": "haze"}
headbutt       = { "type": "normal"  , "category": "physical", "acc": 1   ,"power": 70 ,"pp": 15, "name": "headbutt"}
high_jump_kick = { "type": "fighting", "category": "physical", "acc": 0.9 ,"power": 130,"pp": 10, "name": "high jump kick"}
horn_attack    = { "type": "normal"  , "category": "physical", "acc": 1   ,"power": 65 ,"pp": 25, "name": "horn attack"}
horn_drill     = { "type": "normal"  , "category": "physical", "acc": 1   ,"power": 0  ,"pp": 5 , "name": "horn drill"}
hydro_pump     = { "type": "water"   , "category": "special" , "acc": 0.8 ,"power": 110,"pp": 5 , "name": "hydro pump"}
hyper_beam     = { "type": "normal"  , "category": "special" , "acc": 0.9 ,"power": 150,"pp": 5 , "name": "hyper beam"}
hyper_fang     = { "type": "normal"  , "category": "physical", "acc": 0.9 ,"power": 80 ,"pp": 15, "name": "hyper fang"}
hypnosis       = { "type": "psychic" , "category": "status"  , "acc": 0.6 ,"power": 0  ,"pp": 20, "name": "hypnosis"}
ice_beam       = { "type": "ice"     , "category": "special" , "acc": 1   ,"power": 90 ,"pp": 10, "name": "ice beam"}
ice_punch      = { "type": "ice"     , "category": "physical", "acc": 1   ,"power": 75 ,"pp": 15, "name": "ice punch"}
jump_kick      = { "type": "fighting", "category": "physical", "acc": 0.95,"power": 100,"pp": 10, "name": "jump kick"}
karate_chop    = { "type": "fighting", "category": "physical", "acc": 1   ,"power": 50 ,"pp": 25, "name": "karate chop"}
kinesis        = { "type": "psychic" , "category": "status"  , "acc": 0.8 ,"power": 0  ,"pp": 15, "name": "kinesis"}
leech_life     = { "type": "bug"     , "category": "physical", "acc": 1   ,"power": 20 ,"pp": 15, "name": "leech life"}
leech_seed     = { "type": "grass"   , "category": "status"  , "acc": 0.9 ,"power": 0  ,"pp": 10, "name": "leech seed"}
leer           = { "type": "normal"  , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 30, "name": "leer"}
lick           = { "type": "ghost"   , "category": "physical", "acc": 1   ,"power": 30 ,"pp": 30, "name": "lick"}
light_screen   = { "type": "psychic" , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 30, "name": "light screen"}
lovely_kiss    = { "type": "normal"  , "category": "status"  , "acc": 0.75,"power": 0  ,"pp": 10, "name": "lovely kiss"}
low_kick       = { "type": "fighting", "category": "physical", "acc": 1   ,"power": 0  ,"pp": 20, "name": "low kick"}
meditate       = { "type": "psychic" , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 40, "name": "meditate"}
mega_drain     = { "type": "grass"   , "category": "special" , "acc": 1   ,"power": 40 ,"pp": 15, "name": "mega drain"}
mega_kick      = { "type": "normal"  , "category": "physical", "acc": 0.75,"power": 120,"pp": 5 , "name": "mega kick"}
mega_punch     = { "type": "normal"  , "category": "physical", "acc": 0.85,"power": 80 ,"pp": 20, "name": "mega punch"}
metronome      = { "type": "normal"  , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 10, "name": "metronome"}
mimic          = { "type": "normal"  , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 10, "name": "mimic"}
minimize       = { "type": "normal"  , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 10, "name": "minimize"}
mirror_move    = { "type": "flying"  , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 20, "name": "mirror move"}
mist           = { "type": "ice"     , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 30, "name": "mist"}
night_shade    = { "type": "ghost"   , "category": "special" , "acc": 1   ,"power": 0  ,"pp": 15, "name": "night shade"}
pay_day        = { "type": "normal"  , "category": "physical", "acc": 1   ,"power": 40 ,"pp": 20, "name": "pay day"}
peck           = { "type": "flying"  , "category": "physical", "acc": 1   ,"power": 35 ,"pp": 35, "name": "peck"}
petal_dance    = { "type": "grass"   , "category": "special" , "acc": 1   ,"power": 120,"pp": 10, "name": "petal dance"}
pin_missile    = { "type": "bug"     , "category": "physical", "acc": 0.95,"power": 25 ,"pp": 20, "name": "pin missile"}
poison_gas     = { "type": "poison"  , "category": "status"  , "acc": 0.9 ,"power": 0  ,"pp": 40, "name": "poison gas"}
poison_powder  = { "type": "poison"  , "category": "status"  , "acc": 0.75,"power": 0  ,"pp": 35, "name": "poison powder"}
poison_sting   = { "type": "poison"  , "category": "physical", "acc": 1   ,"power": 15 ,"pp": 35, "name": "poison sting"}
pound          = { "type": "normal"  , "category": "physical", "acc": 1   ,"power": 40 ,"pp": 35, "name": "pound"}
psybeam        = { "type": "psychic" , "category": "special" , "acc": 1   ,"power": 65 ,"pp": 20, "name": "psybeam"}
psychic        = { "type": "psychic" , "category": "special" , "acc": 1   ,"power": 90 ,"pp": 10, "name": "psychic"}
psywave        = { "type": "psychic" , "category": "special" , "acc": 0.8 ,"power": 0  ,"pp": 15, "name": "psywave"}
quick_attack   = { "type": "normal"  , "category": "physical", "acc": 1   ,"power": 40 ,"pp": 30, "name": "quick attack"}
rage           = { "type": "normal"  , "category": "physical", "acc": 1   ,"power": 20 ,"pp": 20, "name": "rage"}
razor_leaf     = { "type": "grass"   , "category": "physical", "acc": 0.95,"power": 55 ,"pp": 25, "name": "razor leaf"}
razor_wind     = { "type": "normal"  , "category": "special" , "acc": 1   ,"power": 80 ,"pp": 10, "name": "razor wind"}
recover        = { "type": "normal"  , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 10, "name": "recover"}
reflect        = { "type": "psychic" , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 20, "name": "reflect"}
rest           = { "type": "psychic" , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 10, "name": "rest"}
roar           = { "type": "normal"  , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 20, "name": "roar"}
rock_slide     = { "type": "rock"    , "category": "physical", "acc": 0.9 ,"power": 75 ,"pp": 10, "name": "rock slide"}
rock_throw     = { "type": "rock"    , "category": "physical", "acc": 0.9 ,"power": 50 ,"pp": 15, "name": "rock throw"}
rolling_kick   = { "type": "fighting", "category": "physical", "acc": 0.85,"power": 60 ,"pp": 15, "name": "rolling kick"}
sand_attack    = { "type": "ground"  , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 15, "name": "sand attack"}
scratch        = { "type": "normal"  , "category": "physical", "acc": 1   ,"power": 40 ,"pp": 35, "name": "scratch"}
screech        = { "type": "normal"  , "category": "status"  , "acc": 0.85,"power": 0  ,"pp": 40, "name": "screech"}
seismic_toss   = { "type": "fighting", "category": "physical", "acc": 1   ,"power": 0  ,"pp": 20, "name": "seismic toss"}
self_destruct  = { "type": "normal"  , "category": "physical", "acc": 1   ,"power": 200,"pp": 5 , "name": "self_destruct"}
sharpen        = { "type": "normal"  , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 30, "name": "sharpen"}
sing           = { "type": "normal"  , "category": "status"  , "acc": 0.55,"power": 0  ,"pp": 15, "name": "sing"}
skull_bash     = { "type": "normal"  , "category": "physical", "acc": 1   ,"power": 130,"pp": 10, "name": "skull bash"}
sky_attack     = { "type": "flying"  , "category": "physical", "acc": 0.9 ,"power": 140,"pp": 5 , "name": "sky attack"}
slam           = { "type": "normal"  , "category": "physical", "acc": 0.75,"power": 80 ,"pp": 20, "name": "slam"}
slash          = { "type": "normal"  , "category": "physical", "acc": 1   ,"power": 70 ,"pp": 20, "name": "slash"}
sleep_powder   = { "type": "grass"   , "category": "status"  , "acc": 0.75,"power": 0  ,"pp": 15, "name": "sleep powder"}
sludge         = { "type": "poison"  , "category": "special" , "acc": 1   ,"power": 65 ,"pp": 20, "name": "sludge"}
smog           = { "type": "poison"  , "category": "special" , "acc": 0.7 ,"power": 30 ,"pp": 20, "name": "smog"}
smokescreen    = { "type": "normal"  , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 20, "name": "smokescreen"}
soft_boiled    = { "type": "normal"  , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 10, "name": "soft_boiled"}
solar_beam     = { "type": "grass"   , "category": "special" , "acc": 1   ,"power": 120,"pp": 10, "name": "solar beam"}
sonic_boom     = { "type": "normal"  , "category": "special" , "acc": 0.9 ,"power": 0  ,"pp": 20, "name": "sonic boom"}
spike_cannon   = { "type": "normal"  , "category": "physical", "acc": 1   ,"power": 20 ,"pp": 15, "name": "spike cannon"}
splash         = { "type": "normal"  , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 40, "name": "splash"}
spore          = { "type": "grass"   , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 15, "name": "spore"}
stomp          = { "type": "normal"  , "category": "physical", "acc": 1   ,"power": 65 ,"pp": 20, "name": "stomp"}
strength       = { "type": "normal"  , "category": "physical", "acc": 1   ,"power": 80 ,"pp": 15, "name": "strength"}
string_shot    = { "type": "bug"     , "category": "status"  , "acc": 0.95,"power": 0  ,"pp": 40, "name": "string shot"}
struggle       = { "type": "normal"  , "category": "physical", "acc": 1   ,"power": 50 ,"pp": 0 , "name": "struggle"}
stun_spore     = { "type": "grass"   , "category": "status"  , "acc": 0.75,"power": 0  ,"pp": 30, "name": "stun spore"}
submission     = { "type": "fighting", "category": "physical", "acc": 0.8 ,"power": 80 ,"pp": 25, "name": "submission"}
substitute     = { "type": "normal"  , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 10, "name": "substitute"}
super_fang     = { "type": "normal"  , "category": "physical", "acc": 0.9 ,"power": 0  ,"pp": 10, "name": "super fang"}
supersonic     = { "type": "normal"  , "category": "status"  , "acc": 0.55,"power": 0  ,"pp": 20, "name": "supersonic"}
surf           = { "type": "water"   , "category": "special" , "acc": 1   ,"power": 90 ,"pp": 15, "name": "surf"}
swift          = { "type": "normal"  , "category": "special" , "acc": 1   ,"power": 60 ,"pp": 20, "name": "swift"}
swords_dance   = { "type": "normal"  , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 20, "name": "swords dance"}
tackle         = { "type": "normal"  , "category": "physical", "acc": 1   ,"power": 50 ,"pp": 35, "name": "tackle"}
tail_whip      = { "type": "normal"  , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 30, "name": "tail whip"}
take_down      = { "type": "normal"  , "category": "physical", "acc": 0.85,"power": 90 ,"pp": 20, "name": "take down"}
teleport       = { "type": "psychic" , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 20, "name": "teleport"}
thrash         = { "type": "normal"  , "category": "physical", "acc": 1   ,"power": 120,"pp": 10, "name": "thrash"}
thunder        = { "type": "electric", "category": "special" , "acc": 0.7 ,"power": 110,"pp": 10, "name": "thunder"}
thunder_punch  = { "type": "electric", "category": "physical", "acc": 1   ,"power": 75 ,"pp": 15, "name": "thunder punch"}
thunder_shock  = { "type": "electric", "category": "special" , "acc": 1   ,"power": 40 ,"pp": 30, "name": "thunder shock"}
thunder_wave   = { "type": "electric", "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 20, "name": "thunder wave"}
thunderbolt    = { "type": "electric", "category": "special" , "acc": 1   ,"power": 90 ,"pp": 15, "name": "thunderbolt"}
toxic          = { "type": "poison"  , "category": "status"  , "acc": 0.9 ,"power": 0  ,"pp": 10, "name": "toxic"}
transform      = { "type": "normal"  , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 10, "name": "transform"}
tri_attack     = { "type": "normal"  , "category": "special" , "acc": 1   ,"power": 80 ,"pp": 10, "name": "tri attack"}
twineedle      = { "type": "bug"     , "category": "physical", "acc": 1   ,"power": 25 ,"pp": 20, "name": "twineedle"}
vice_grip      = { "type": "normal"  , "category": "physical", "acc": 1   ,"power": 55 ,"pp": 30, "name": "vice grip"}
vine_whip      = { "type": "grass"   , "category": "physical", "acc": 1   ,"power": 45 ,"pp": 25, "name": "vine whip"}
water_gun      = { "type": "water"   , "category": "special" , "acc": 1   ,"power": 40 ,"pp": 25, "name": "water gun"}
waterfall      = { "type": "water"   , "category": "physical", "acc": 1   ,"power": 80 ,"pp": 15, "name": "waterfall"}
whirlwind      = { "type": "normal"  , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 20, "name": "whirlwind"}
wing_attack    = { "type": "flying"  , "category": "physical", "acc": 1   ,"power": 60 ,"pp": 35, "name": "wing attack"}
withdraw       = { "type": "water"   , "category": "status"  , "acc": 1   ,"power": 0  ,"pp": 40, "name": "withdraw"}
wrap           = { "type": "normal"  , "category": "physical", "acc": 0.9 ,"power": 15 ,"pp": 20, "name": "wrap"}

# moves the pokemon have
pikachu_moves    = [thunder_shock, slam, thunderbolt, thunder]
nidoking_moves   = [horn_attack, poison_sting, thrash, double_kick]
alakazam_moves   = [confusion, psybeam, psychic]
jigglypuff_moves = [pound, double_slap, body_slam, double_edge]
growlithe_moves  = [bite, ember, take_down, flamethrower]
mew_moves        = [pound, mega_punch, psychic]
seel_moves       = [headbutt, aurora_beam, take_down, ice_beam]
gyarados_moves   = [bite, hydro_pump, tackle]
staryu_moves     = [tackle, water_gun, swift, hydro_pump]
blastoise_moves  = [bubble, water_gun, bite, skull_bash]


class Pokemon(object):
    def __init__(self,name, base_hp, base_attack, base_defense, base_speed, base_special_attack, base_special_defense, types, moves):
        self.name = name
        self.base_hp = base_hp
        self.base_attack = base_attack
        self.base_defense = base_defense
        self.base_speed = base_speed
        self.base_special_attack = base_special_attack
        self.base_special_defense = base_special_defense
        self.types = types
        self.moves = moves
        self.stats()
    def stats(self):
        self.level = 50
        I = 0
        if self.base_attack % 2: I += 8
        if self.base_defense % 2: I += 4
        if self.base_speed % 2: I += 2
        if self.base_special_attack % 2: I += 1
        self.attack = floor((2 * self.base_attack + I ) * self.level / 100 + 5)
        self.speed = floor((2 * self.base_speed + I ) * self.level / 100 + 5)
        self.defense = floor((2 * self.base_defense + I ) * self.level / 100 + 5)
        self.max_hp = floor((2 * self.base_hp + I) * self.level / 100 + self.level + 10)
        self.special_attack = floor((2 * self.base_special_attack + I ) * self.level / 100 + 5)
        self.special_defense = floor((2 * self.base_special_defense + I ) * self.level / 100 + 5)
        self.hp = self.max_hp

pikachu    =  Pokemon ("pikachu", 35,  55,  30,  90,  50, 40, ["electric"],pikachu_moves)
nidoking   =  Pokemon ("nidoking", 81,  92,  77,  85, 85, 75, ["poison","ground"],nidoking_moves )
alakazam   =  Pokemon ("alakazam", 55 ,  50,  45,  120,  135, 85, ["psychic"],alakazam_moves)
jigglypuff =  Pokemon ("jigglypuff", 115,  45,  20,  20, 45, 25, ["normal"],jigglypuff_moves )
growlithe  =  Pokemon ("growlithe", 55,  70,  45,  60, 70, 50, ["fire"],growlithe_moves)
mew        =  Pokemon ("mew", 100,  100,  100 ,  100, 100, 100, ["psychic"],mew_moves)
seel       =  Pokemon ("seel", 65,  45,  55,  45, 45, 70, ["water"],seel_moves) 
gyarados   =  Pokemon ("gyarados", 95,  125,  79,  81, 60, 100, ["water","flying"],gyarados_moves) 
staryu     =  Pokemon ("staryu", 30,  45,  55,  85,  70, 55, ["water"],staryu_moves)
blastoise  =  Pokemon ("blastoise", 79,  83,  100,  78,   85, 105, ["water"],blastoise_moves)

reinier = {pikachu : True, nidoking : True,alakazam : True,jigglypuff : True,growlithe : True,mew : True}
gym = {seel: True,gyarados: True,staryu: True,blastoise: True}

gym_pokemon = random.choice(list(gym.keys()))