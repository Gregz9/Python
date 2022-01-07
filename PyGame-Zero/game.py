
from space_ship import Space_ship
from bullet import Bullet 
from monster import Monster
import random, os
import pygame
import sys 

MONSTER_COUNT = 10

class Game:  

    def __init__(self): 
        self._monsters = []
        self._bullets = []
        self._updates = 0
        self._spaceship = Space_ship()
        self._previous_shots = 0
        self._stage = 1 
        self.status = "Menu"
        self.counter = 0 

    def get_status(self): 
        return self.status
    
    def set_status(self, new_status):
        self.status = new_status 

    def game_init(self): 
        main_manu()


    
       

    def update(self, keyboard): 
        if keyboard.left: 
            if(keyboard.down): 
                self._spaceship.move_left()
                self._spaceship.move_down()
            elif(keyboard.up): 
                self._spaceship.move_left()
                self._spaceship.move_up()
            else: 
                self._spaceship.move_left()

        elif keyboard.right: 
            if(keyboard.down): 
                self._spaceship.move_right()
                self._spaceship.move_down()
            elif(keyboard.up):
                self._spaceship.move_right()
                self._spaceship.move_up()
            else: 
                self._spaceship.move_right()

        elif keyboard.up: 
            self._spaceship.move_up()
        elif keyboard.down: 
            self._spaceship.move_down()
        elif keyboard.up and keyboard.right: 
            self._spaceship.move_right()
            self._spaceship.move_up()
        
        if keyboard.escape: 
            sys.exit()
            
        
        if keyboard.space and self._updates - self._previous_shots > 5: 
            self.shoot()
            self._previous_shots = self._updates
        
        prob = random.randrange(1,50)
        if(self.counter < MONSTER_COUNT): 
            if(prob == 12): 
                string1 = 'monster'
                num = random.randrange(1, 5)
                string1 += (str(num) + '.png')
                monster = Monster(string1, random.randrange(0,900-63), random.randrange(64, 365), 1)
            # monster2 = Monster("lotta_monster.png", random.randrange(0,900-63), random.randrange(64, 365), 1)
                
                self._monsters.append(monster)
                self.counter += 1 
            # self._monsters.append(monster2) 

        self.monsters_move()
        self.check_hit()
        self._updates += 1

        
    

    def dead(self): 
        count = 0 
        for monster in self._monsters: 
            if not monster.alive():
                count += 1 
        
        if count == len(self.monsters): 
            return True 
        return False
           
    
    def shoot(self): 
        bullet = Bullet(self._spaceship)
        self._bullets.append(bullet)
        
    
    #def press_left(key)
    
    def draw(self, screen): 
        screen.fill((0, 0, 0))
        self._spaceship.draw(screen)

        for monster in self._monsters: 
            if monster.alive():
                monster.draw(screen)
                
        
        for bullet in self._bullets: 
            if not bullet.get_stat(): 
                bullet.draw(screen)
                bullet.move_up()
            else: 
                self._bullets.remove(bullet)
        

       
        screen.draw.textbox(f'Score: \n{self._spaceship.get_score()}', (450,10, 100, 50), owidth = 12.0, color = "red", alpha=0.5)


    def monsters_move(self): 
        
        for monster in self._monsters: 
            if monster.alive(): 
                monster.move()
    
    def check_hit(self): 
        for monster in self._monsters: 
            if not monster.alive():
                continue
            
            for bullet in self._bullets: 
                if bullet.get_stat(): 
                    continue
                if (bullet.get_hor_pos() >= monster.get_pos_hor()) and (bullet.get_hor_pos() < monster.get_pos_hor() + 64 - 24):
                    if (bullet.get_vert_pos() > monster.get_pos_top()) and (bullet.get_vert_pos() < monster.get_pos_top() +64): 
                        monster.hit()
                        self._spaceship.add_score()
                        bullet.hit_monster()



    #def main_menu(self):
    
    """def pause(self): 
        text_1 = pygame.font.SysFont("italic", 50)
        TextSurf, TextRect = text_objects("Paused", text_1)
        TextRect.center = ((450, 100))
        gameDisplay.blit(TextSurf, TextRect)

        while True: 
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    pygame.quit() 
                    quit() 
            
            button("Continue",150,450,100,50,green,bright_green,unpause)
            button("Quit",550,450,100,50,red,bright_red,quitgame)

            pygame.display.update()
            clock.tick(15)  """

                



        