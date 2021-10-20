import pypokedex
import PIL.Image , PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO

pokemon = pypokedex.get(name="wartortle")
print(pokemon.dex)
print(pokemon.name)
print(pokemon.types)
print(type(pokemon.moves))
# print(pokemon.sprites)
# print(pokemon.abilities)
from PIL._imaging import font

# window = tk.Tk()
# window.geometry("600x500")
# window.title("PokeDex")
# window.config(padx=10, pady=10)
#
# title_label = tk.Label(window, text="PokeDex")
# title_label.config(font=("Arial", 32))
# title_label.pack(padx=10, pady=10)
#
# pokemon_img = tk.Label(window)
# pokemon_img.pack(padx=10, pady=10)
#
# pokemon_info = tk.Label(window)
# pokemon_info.config(font=("Arial", 20))
# pokemon_info.pack(padx=10, pady=10)
#
# pokemon_types = tk.Label(window)
# pokemon_types.config(font=("Arial", 20))
# pokemon_types.pack(padx=10, pady=10)
#
# pokemon_moves = tk.Label(window)
# pokemon_moves.config(font=("Arial", 20))
# pokemon_moves.pack(padx=10, pady=10)
#
#
# def load_pokemon():
#     pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))
#
#     http = urllib3.PoolManager()
#     reponse = http.request('GET', pokemon.sprites.front.get('default'))
#     image = PIL.Image.open(BytesIO(reponse.data))
#
#     img = PIL.ImageTk.PhotoImage(image)
#     pokemon_img.config(image=img)
#     pokemon_img.image = img
#
#     pokemon_info.config(text=f"{pokemon.dex} - {pokemon.name}")
#     pokemon_types.config(text=" - ".join(t for t in pokemon.types))
#     pokemon_moves.config(text=" - ".join(t for t in pokemon.moves))
#
# label_id_name = tk.Label(window, text="ID or Name")
# label_id_name.config(font=("Arial", 20))
# label_id_name.pack(padx=10, pady=10)
#
# text_id_name = tk.Text(window, height=1)
# text_id_name.config(font=("Arial", 20))
# text_id_name.pack(padx=10, pady=10)
#
# btn_load =  tk.Button(window, text="Load Pokemon", command=load_pokemon)
# btn_load.config(font=("Arial", 20))
# btn_load.pack(padx=10, pady=10)
#
#
# window.mainloop()
