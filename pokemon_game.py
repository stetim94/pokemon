import tkinter as tk
from functools import reduce, partial
from operator import mul
from test_pokemon import *
from functools import partial

class start_game:
    def __init__(self,master):
        self.master = master
        self.start_frame = tk.Frame(master)
        start_label = tk.Label(self.start_frame, text="Welkom bij dit pokemon spel\n\n je moet de watergym verslaan.\n\
              de eerste pokemon van de gym is: " + gym_pokemon.name + "\nclick next to choice your pokemon")
        start_label.grid()
        next_button = tk.Button(self.start_frame, text="next", command=self.choice_pokemon)
        next_button.grid()
        self.start_frame.grid()
    def choice_pokemon(self):
        self.start_frame.destroy()
        self.app = show_pokemon(self.master)

class show_pokemon:
    def __init__(self, master):
        self.master = master
        self.pokemon_frame = tk.Frame(master)
        for row,pokemon in enumerate(reinier):
            row *= 2
            pokemon_label = tk.Label(self.pokemon_frame, text=pokemon.name)
            pokemon_label.grid(row=row,column=0)
            hp_label = tk.Label(self.pokemon_frame, text="hp: " + str(pokemon.hp) + "/" + str(pokemon.max_hp))
            hp_label.grid(row=row+1,column=0,pady=(0,10),padx=(0,30))
            info_button = tk.Button(self.pokemon_frame, text="view info", command=partial(self.viewDetailsFrame, pokemon))
            info_button.grid(row=row,column=1, rowspan=2)
            choice_button = tk.Button(self.pokemon_frame, text="choice", command=partial(self.viewBattleFrame, pokemon)) if pokemon.hp > 0 else tk.Button(self.pokemon_frame, text="choice", state="disabled")
            choice_button.grid(row=row,column=2, rowspan=2)
        self.pokemon_frame.grid()

  def viewDetailsFrame(self,pokemon):
      self.pokemon_frame.grid_forget()
      self.app = detail_view(self.master,pokemon)
  def viewBattleFrame(self,pokemon):
      self.pokemon_frame.grid_forget()
      self.app = battle_view(self.master,pokemon)
class detail_view:
    def __init__(self, master,pokemon):
        self.master = master
        self.detail_frame = tk.Frame(master)
        back_button     = tk.Button(self.detail_frame, text="back", command=self.viewShowPokemon)
        name_label      = tk.Label(self.detail_frame, text="name:")
        pokemon_name    = tk.Label(self.detail_frame, text=pokemon.name)
        hp_label        = tk.Label(self.detail_frame, text="hp:")
        pokemon_hp      = tk.Label(self.detail_frame, text=str(pokemon.hp) + "/" + str(pokemon.max_hp))
        attack_label    = tk.Label(self.detail_frame, text="attack:")
        pokemon_attack  = tk.Label(self.detail_frame, text=str(pokemon.attack))
        defense_label   = tk.Label(self.detail_frame, text="defense:")
        pokemon_defense = tk.Label(self.detail_frame, text=str(pokemon.defense))
        back_button.grid(row=0,column=0)
        name_label.grid(row=1, column=0)
        pokemon_name.grid(row=1 ,column=1)
        hp_label.grid(row=2, column=0)
        pokemon_hp.grid(row=2 ,column=1)
        attack_label.grid(row=3, column=0)
        pokemon_attack.grid(row=3, column=1)
        defense_label.grid(row=4,column=0)
        pokemon_defense.grid(row=4, column=1)
        pokemon_type  = tk.Label(self.detail_frame, text="type:")
        pokemon_move  = tk.Label(self.detail_frame, text="move:")
        pokemon_power = tk.Label(self.detail_frame, text="power:")
        pokemon_pp    = tk.Label(self.detail_frame, text="pp:")
        pokemon_acc   = tk.Label(self.detail_frame, text="acc:")
        pokemon_type.grid(row=0,column=2)
        pokemon_move.grid(row=0,column=3)
        pokemon_power.grid(row=0,column=4)
        pokemon_pp.grid(row=0,column=5)
        pokemon_acc.grid(row=0,column=6)
        for x in range(len(pokemon.moves)):
            type_label  = tk.Label(self.detail_frame, text=pokemon.moves[x]["type"])
            move_label  = tk.Label(self.detail_frame, text=pokemon.moves[x]['name'])
            power_label = tk.Label(self.detail_frame, text=pokemon.moves[x]["power"])
            pp_label    = tk.Label(self.detail_frame, text=pokemon.moves[x]["pp"])
            acc_label   = tk.Label(self.detail_frame, text=pokemon.moves[x]["acc"])
            x += 1
            type_label.grid(row=x,column=2)
            move_label.grid(row=x,column=3)
            power_label.grid(row=x,column=4)
            pp_label.grid(row=x,column=5)
            acc_label.grid(row=x,column=6)

      self.detail_frame.grid()
  def viewShowPokemon(self):
      self.detail_frame.destroy()
      self.app = show_pokemon(self.master)

class battle_view:
    def __init__(self, master,trainer_pokemon):
        self.master          = master
        self.battle_frame    = tk.Frame(master)
        self.trainer_pokemon = trainer_pokemon
        self.gym_pokemon     = gym_pokemon
        # gym
        self.gym_label    = tk.Label(self.battle_frame, text=self.gym_pokemon.name)
        self.gym_hp_label = tk.Label(self.battle_frame, text="hp: " + str(self.gym_pokemon.hp) + "/" + str(self.gym_pokemon.max_hp))
        # to grid
        self.gym_label.grid(row=0,column=0)
        self.gym_hp_label.grid(row=0,column=1)

        #trainer
        trainer_label         = tk.Label(self.battle_frame, text=trainer_pokemon.name)
        self.trainer_hp_label = tk.Label(self.battle_frame, text="hp: " + str(self.trainer_pokemon.hp) + "/" + str(self.trainer_pokemon.max_hp))
        self.attack           = tk.Button(self.battle_frame, text="attack", command=self.load_moves, state='normal')
        self.switch           = tk.Button(self.battle_frame, text="switch", command=self.switch_pokemon, state='normal')
        # to grid
        trainer_label.grid(row=1,column=0)
        self.trainer_hp_label.grid(row=1,column=1)
        self.attack.grid(row=2,column=0)
        self.switch.grid(row=2,column=1)
        #frame to grid
        self.battle_frame.grid()
    def switch_pokemon(self):
        self.battle_frame.destroy()
        self.app = show_pokemon(self.master)

    def load_moves(self):
        self.moves_frame = tk.Frame(self.battle_frame)
        pokemon_move     = tk.Label(self.moves_frame, text="move:")
        pokemon_type     = tk.Label(self.moves_frame, text="type:")
        pokemon_power    = tk.Label(self.moves_frame, text="power:")
        pokemon_pp       = tk.Label(self.moves_frame, text="pp:")
        pokemon_acc      = tk.Label(self.moves_frame, text="acc:")
        pokemon_move.grid(row=0,column=0)
        pokemon_type.grid(row=0,column=1)
        pokemon_power.grid(row=0,column=2)
        pokemon_pp.grid(row=0,column=3)
        pokemon_acc.grid(row=0,column=4)
        for x, y in zip(range(len(self.trainer_pokemon.moves)),self.trainer_pokemon.moves):
            move_label  = tk.Button(self.moves_frame, text=self.trainer_pokemon.moves[x]["name"] ,command=partial(self.damage_order, y))
            type_label  = tk.Label(self.moves_frame, text=self.trainer_pokemon.moves[x]["type"])
            power_label = tk.Label(self.moves_frame, text=self.trainer_pokemon.moves[x]["power"])
            pp_label    = tk.Label(self.moves_frame, text=self.trainer_pokemon.moves[x]["pp"])
            acc_label   = tk.Label(self.moves_frame, text=str(self.trainer_pokemon.moves[x]["acc"] * 100) + "%")
            x += 1
            move_label.grid(row=x,column=0)
            type_label.grid(row=x,column=1)
            power_label.grid(row=x,column=2)
            pp_label.grid(row=x,column=3)
            acc_label.grid(row=x,column=4)

        self.moves_frame.grid(row=3,columnspan=2)
    def damage_order(self,trainer_move):
        self.moves_frame.destroy()
        self.attack_frame = tk.Frame(self.battle_frame)
        self.row = 0
        self.attack['state'] = 'disabled'
        self.switch['state'] = 'disabled'
        gym_move = random.choice(self.gym_pokemon.moves)
        while not gym_move["pp"]: gym_move = random.choice(self.gym_pokemon.moves)
        if self.trainer_pokemon.speed >= self.gym_pokemon.speed:
            self.calculate_damage(self.trainer_pokemon,trainer_move,self.gym_pokemon)
            if self.gym_pokemon.hp > 0:
                self.calculate_damage(self.gym_pokemon,gym_move,self.trainer_pokemon)
        else:
            self.calculate_damage(self.gym_pokemon,gym_move,self.trainer_pokemon)
            if self.trainer_pokemon.hp > 0:
                self.calculate_damage(self.trainer_pokemon, trainer_move,self.gym_pokemon)
        self.update_hp_labels()


    def calculate_damage(self,attacking_pokemon,move, defending_pokemon):
        move["pp"] -= 1
        stab = 1.5 if move["type"] in attacking_pokemon.types else 1
        type_effect = reduce(mul,[attack_type[move["type"]].get(k,1) for k in defending_pokemon.types],1)
        crit = 1.5 if random.random() < 0.0625 else 1
        random_change = random.uniform(0.85,1)
        modifier = stab * type_effect * crit * random_change
        damage = floor((((2 * 50 + 10)/250) * (attacking_pokemon.attack/defending_pokemon.defense) * (move['power'])) * modifier) if random.random() < move["acc"] else 0
        if damage:
            damage_label = tk.Label(self.attack_frame, text=move['name']+ " dealt " + str(damage) + " damage")
            damage_label.grid(row=self.row,column=0); self.row += 1
            if type_effect > 1:
                effective = tk.Label(self.attack_frame, text="It's super effective")
                effective.grid(row=self.row,column=0); self.row += 1
            elif type_effect < 1:
                effective = tk.Label(self.attack_frame, text="It's not very effective")
                effective.grid(row=self.row,column=0); self.row += 1
            if crit == 1.5:
                critical_hit = tk.Label(self.attack_frame, text="A critical hit!")
                critical_hit.grid(row=self.row, column=0); self.row += 1
        else:
            damage_label = tk.Label(self.attack_frame, text=move['name'] + " missed")
            damage_label.grid(row=self.row,column=0); self.row += 1


        defending_pokemon.hp -= damage
        if defending_pokemon.hp < 0:
            defending_pokemon.hp = 0
            fainted = tk.Label(self.attack_frame, text=defending_pokemon.name + " fainted")
            fainted.grid(row=self.row,column=0); self.row += 1
        self.attack_frame.grid(row=3,columnspan=2)

    def update_hp_labels(self):
        self.gym_hp_label['text'] = "hp: " + str(self.gym_pokemon.hp) + "/" + str(self.gym_pokemon.max_hp)
        self.trainer_hp_label["text"] = "hp: " + str(self.trainer_pokemon.hp) + "/" + str(self.trainer_pokemon.max_hp)
        button = tk.Button(self.attack_frame, text="continue", command=self.clean)
        button.grid(row=self.row,column=0)
    def clean(self):
        self.attack_frame.destroy()
        self.attack['state'] = 'normal'
        self.switch['state'] = 'normal'
        if self.trainer_pokemon.hp == 0:
            reinier[self.trainer_pokemon] = False
            still_alive = [pokemon for pokemon, alive in reinier.items() if alive == True]
            if len(still_alive) == 0:
                self.battle_frame.destroy()
                self.loser()
            else:
                self.switch_pokemon()
        if self.gym_pokemon.hp == 0:
            gym[self.gym_pokemon] = False
            still_alive = [pokemon for pokemon, alive in gym.items() if alive == True]
            if len(still_alive) == 0:
                self.battle_frame.destroy()
                self.winner()
            else:
                self.gym_pokemon = random.choice(still_alive)
                global gym_pokemon
                gym_pokemon = self.gym_pokemon
                self.gym_label['text'] = self.gym_pokemon.name
                self.gym_hp_label['text'] = "hp: " + str(self.gym_pokemon.hp) + "/" + str(self.gym_pokemon.max_hp)


    def winner(self):
        label = tk.Label(self.master, text="You won")
        label.pack()
    def loser(self):
        label = tk.Label(self.master, text="You lost")
        label.pack()

def main():
    root = tk.Tk()
    app = start_game(root)
    root.mainloop()

if __name__ == '__main__':
    main()
