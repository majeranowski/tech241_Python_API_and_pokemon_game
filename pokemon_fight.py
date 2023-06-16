import requests
import random

def get_pokemon(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        return None

def get_random_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        print(pokemon_data)
        pokemon_list = pokemon_data['results']
        print(pokemon_list)
        random_pokemon = random.choice(pokemon_list)
        return random_pokemon
    else:
        return None
get_random_pokemon()



def battle():
    print("Welcome to the Pokémon Fighting Game!")
    player1_name = input("Player 1, enter your Pokémon's name: ")
    random_pokemon = get_random_pokemon()
    random_pokemon = random_pokemon['name']
    print(f"CPU's pokemon is: {random_pokemon}")


    player1_pokemon = get_pokemon(player1_name)
    cpu_pokemon = get_pokemon(random_pokemon)

    if player1_pokemon and cpu_pokemon:
        print("Let the battle begin, Pokemon with more HP wins!")
        player1_hp = player1_pokemon['stats'][0]['base_stat']
        cpu_hp = cpu_pokemon['stats'][0]['base_stat']
        print(f"{player1_name}'s HP: {player1_hp}")
        print(f"{random_pokemon}'s HP: {cpu_hp}")
        if player1_hp > cpu_hp:
            print(f"{player1_name} wins")
        elif player1_hp == cpu_hp:
            print("It is a tie!")
        else:
            print(f"{random_pokemon} wins")

    else:
        print("Invalid Pokémon name. Please try again.")

battle()
