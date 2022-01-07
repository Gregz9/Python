from space_ship import Space_ship

class Bullet: 

    def __init__(self, space_ship): 
        self._picture = 'kule1.png'
        self._pos_left = space_ship.get_hor_pos()+20 
        self._pos_top = space_ship.get_vert_pos()-25
        self._hit_status = False
        self._score = 0
    
    def move_up(self): 
        self._pos_top -= 12

    def draw(self, screen): 
        screen.blit(self._picture, (self._pos_left, self._pos_top)) 
    
    def get_vert_pos(self): 
        return self._pos_top
    
    def get_hor_pos(self):
        return self._pos_left
    
    def hit_monster(self): 
        self._hit_status = True
    
    def get_stat(self): 
        return self._hit_status 

    
