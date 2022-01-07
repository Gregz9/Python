from sheep import Sheep 

class Wolf: 

    def __init__ (self, name, position):
        self._name = name
        self._position = position
        self._weight = 20
    
    def eat_a_sheep(self, sheep):
        sheep.is_eaten() 
        self._weight += 5 

    def check_weight(self): 
        return self._weight
    
    def get_name(self): 
        return self._name 
    
    def get_position(self): 
        return self._position

    def move_right(self):
        if(self._position[1] == 10): 
            self._position[1] = 0
        else: 
            self._position[1] += 1 
    
    def move_left(self): 
        if(self._position[1] == 0): 
            self._position[1] = 10
        else:  
            self._position[1] -= 1 

    def move_up(self): 
        if(self._position[0] == 0): 
            self._position[0] = 10
        else: 
            self._position[0] -= 1 
    
    def move_down(self): 
        if(self._position[0] == 10): 
            self._position[0] = 0
        else: 
            self._position[0] += 1 
    


    

    


