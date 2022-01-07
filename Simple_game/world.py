from sheep import Sheep 
from wolf import Wolf
import random

class World: 

    def __init__ (self): 
        self._sheep = []
        self._wolves = []

    def create_animal(self, type, name, position): 

        """Position for each animal created has to be a list with two coordinates [x, y].
        This is so we can easily update both variables when animals are to move around the world . 
        To create an animal, we have to pass the type of animal as an argument in the place of parameter
        type, writing in lower case."""

        if(type == 'sheep'): 
            sheep = Sheep(name, position)
            self._sheep.append(sheep) 
        elif(type == 'wolf'): 
            wolf = Wolf(name, position)
            self._wolves.append(wolf)
    
    def description(self):
        i = 1 
        j = 1
        for wolf in self._wolves: 
            x, y = wolf.get_position()
            print(f'Wolf nr.{i} has name {wolf.get_name()} and is at position {x, y}', end="\n")
            i += 1 
        
        for sheep in self._sheep: 
            x, y = sheep.get_position()
            print(f'Sheep nr.{j} has name {sheep.get_name()} and is at position {x, y}, and has status alive: {sheep.check_if_alive()}', end="\n")
            j += 1
    
    def count_living_sheep(self): 
        count = 0
        for sheep in self._sheep: 
            if(sheep.is_alive()):
                count += 1
        
        return count 
    
    def count_wolves(self): 
        return len(self._wolves)

    def update(self):

        user_input1 = str(input('Do you want to start a simple simulation: y/n ?'))
        while(user_input1 != 'n'): 
            instruction = random.randrange(1,5)
            wolf_num =  random.randrange(0,len(self._wolves))
            wolf = self._wolves[wolf_num]

            if(instruction == 1): 
                wolf.move_right()
            elif(instruction == 2):
                wolf.move_left()
            elif(instruction == 3):
                wolf.move_up()
            elif(instruction == 4): 
                wolf.move_down()

            for sheep in self._sheep: 
                if wolf.get_position() == sheep.get_position(): 
                    wolf.eat_a_sheep(sheep)
                    x, y = wolf.get_position()
                    print(f'Wolf {wolf._name} has just eaten sheep {sheep._name} at spot {x, y}') 
            user_input1 = str(input('Do you want to simulate again: y/n ?'))
        
    def find_biggest_wolf(self):

        biggest_wolf = self._wolves[0]

        for i in range(1, len(self._wolves)): 
            if(self._wolves[i].check_weight() > biggest_wolf.check_weight()): 
                biggest_wolf = self._wolves[i]
        
        return f'{biggest_wolf.get_name()} is the biggest wolf after this hunt, and has a weight of {biggest_wolf.check_weight()}'


    



    