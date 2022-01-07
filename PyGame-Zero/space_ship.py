import space_world
from monster import Monster

XP_needed = 1500

class Space_ship: 

    def __init__(self): 
        self._pos_left = 450
        self._pos_top = 620
        self._picture = ('galaga8.png')
        self._level = 1 
        self._experiance = 0
        self._score =  0

    def move_right(self): 
        if(self._pos_left == space_world.WIDTH-65): 
            self._pos_left = space_world.WIDTH-65
        else: 
            self._pos_left += 5
            
    
    def move_left(self): 
        if(self._pos_left == 0): 
            self._pos_left = 0 
        else: 
            self._pos_left -= 5
    
    def move_up(self): 
        if(self._pos_top == 0): 
            self._pos_top = 0 
        else: 
            self._pos_top -= 5
    
    def move_down(self): 
        if(self._pos_top == space_world.HEIGHT-65): 
            self._pos_top = space_world.HEIGHT-65 
        else: 
            self._pos_top += 5
    
    def get_vert_pos(self): 
        return self._pos_top
    
    def get_hor_pos(self):
        return self._pos_left
    
    def draw(self, screen): 
        screen.blit(self._picture, (self._pos_left, self._pos_top)) 
    
    def get_score(self): 
        return self._score
    
    def add_score(self): 
        self._score += 1

    def update_xp_needed(self): 
        global XP_needed 
        XP_needed = 2.5 * XP_needed
        return XP_needed
    
    def add_xp(self): 
        self._experiance += Monster.get_num_hits_needed() 
        if (self._experiance >= XP_needed): 
            self._level += 1 
            self._experiance = 0 
            self.update_xp_needed()



    
