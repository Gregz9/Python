

class Sheep: 
    
    def __init__(self, name, position): 
        self._name = name
        self._position = position
        self._alive = True 

    def is_eaten(self): 
        self._alive = False 
    
    def check_if_alive(self): 
        return self._alive
    
    def is_alive(self): 
        return self._alive
    
    def get_name(self): 
        return self._name

    def get_position(self): 
        return self._position
  
