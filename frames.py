import tkinter as tk
from pokemon_data import *

def partial(f, v):
    return lambda: f(v)

class PokemonGame:
    ''' controller for managiging frames '''
    def __init__(self, master):
        self.master = master
        self.frames = {}
        for F in (StartGame,ShowPokemon,PokemonDetail):
            frame = F(parent=master, controller=self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        ''' rais the first frame '''
        self.raise_frame("StartGame")
    def get_page(self, classname):
        '''Returns an instance of a page given it's class name as a string'''
        for page in self.frames.values():
            if str(page.__class__.__name__) == classname:
                return page
        return Non

    def raise_frame(self,page_name):
        ''' raise a frame '''
        frame = self.frames[page_name]
        frame.tkraise()

    def lower_frame(self,page_name):
        ''' lower a frame '''
        frame = self.frames[page_name]
        frame.lower()

class StartGame(tk.Frame):
  ''' introduction screen of the game '''
  def __init__(self, parent, controller):
    super(StartGame,self).__init__(parent)
    self.controller = controller
    tk.Label(self, text="welcome to the world of pokemon").grid(row=0,column=0)
    tk.Label(self, text="You have to beat the water gym").grid(row=1,column=0)
    tk.Label(self, text="the gym choices the following pokemon first: " + gym_pokemon.name).grid(row=2, column=0)
    tk.Button(self, text="next", command=lambda: controller.raise_frame("ShowPokemon")).grid(row=3, column=0)


class ShowPokemon(tk.Frame):
  ''' main frame, overview of all pokemon '''
  def __init__(self, parent, controller):
    super(ShowPokemon,self).__init__(parent)
    self.controller = controller
    for row, pokemon in enumerate(reinier):
      pokemon_label = tk.Label(self, text=pokemon.name + "\nhp: " + str(pokemon.hp) + "/" + str(pokemon.max_hp))
      pokemon_label.grid(row=row,column=0)
      info_button = tk.Button(self, text="view info", command=partial(self.switch,pokemon))
      info_button.grid(row=row,column=1)

  def switch(self, pokemon):
    self.controller.raise_frame("PokemonDetail")

class PokemonDetail(tk.Frame):
    ''' detail view of pokemon '''
    def __init__(self, parent, controller):
        super(PokemonDetail,self).__init__(parent)
        self.controller = controller
        tk.Button(self, text="back", command=lambda: controller.lower_frame("PokemonDetail")).grid()

def main():
    root = tk.Tk()
    app = PokemonGame(root)
    root.mainloop()
main()
