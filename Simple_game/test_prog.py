
from sheep import Sheep
from wolf import Wolf 
from world import World

game_world = World()

game_world.create_animal('wolf', 'Stefan', [1, 2])
game_world.create_animal('wolf', 'Alexander', [1, 2])
game_world.create_animal('wolf', 'Viktor', [1, 2])


game_world.create_animal('sheep', 'Vladimir', [2, 2])
game_world.create_animal('sheep', 'Pieter', [5, 7])
game_world.create_animal('sheep', 'Nikolai', [3, 10])
game_world.create_animal('sheep', 'Aleksei', [7, 4])
game_world.create_animal('sheep', 'Mieshko', [0, 1])
game_world.create_animal('sheep', 'Roman', [10, 10])
game_world.create_animal('sheep', 'Henrik', [5, 5])


game_world.description()

game_world.update()

print(game_world.description())

print(game_world.find_biggest_wolf())








