from random import randint

import requests


class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.power = randint(1,100)
        self.hp = randint(1,100)
        
        Pokemon.pokemons[pokemon_trainer] = self

        
    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
        else:
            return "https://static.wikia.nocookie.net/pokemon/images/0/0d/025Pikachu.png/revision/latest/scale-to-width-down/1000?cb=20181020165701&path-prefix=ru"

    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покемона И его Статы: {self.name} {self.hp} {self.power}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img

    def attack(self, enemy  ):
        if isinstance(enemy, wizard): # Проверка на то, что enemy является типом данных Wizard (является экземпляром класса Волшебник)
            change = randint(1,5)
            if change == 1:
                return "wizard use shield"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Битва @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            self.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}"

class warior(Pokemon):
    def attack(self,  enemy):
        
        superpower = randint(1,10)
        self.power += superpower
        result = super().attack(enemy)
        self.power -= superpower
        return result + f"\nБоец Применил супер атаку силой:{superpower} "

class wizard(Pokemon):
    pass
        
