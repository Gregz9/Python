import space_world
import space_ship

class Monster: 
    def __init__(self, picture, pos_left, pos_top, num_lives): 
        self._picture = picture
        self._pos_left = pos_left
        self._pos_top = pos_top
        self._num_lives = num_lives
        self._direction = 1 
        self._alive = True
        self._num_hits = 3
    
    def alive(self):
        return self._alive
    
    def move(self): 
        if (self._direction == 1): 
            self._pos_left += 4
            if (self._pos_left >= 900 - 64): 
                #self._pos_top += 64 
                self._direction = -1
        elif(self._direction == -1): 
            self._pos_left -= 4 
            if (self._pos_left <= 0): 
                self._direction = 1
                #self._pos_top += 64

    def draw(self, screen): 
        screen.blit(self._picture, (self._pos_left, self._pos_top))

    def get_pos_hor(self): 
        return self._pos_left

    def get_pos_top(self): 
        return self._pos_top
    
    def get_num_hits_needed(self): 
        return self._num_hits
    
    def hit(self): 
        """Method checks if positions of the bullet and monster are aproximetely the same. 
        One important consideration is to remember that a bullet can gvit on the edges of the monster. 
        Thus the position of the bullet doesn't need to be exactly the center of ant monster."""
        self._num_hits -= 1 
        if(self._num_hits == 0): 
            self._alive = False

        

