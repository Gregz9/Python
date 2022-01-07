from sheep import Sheep 
import random 

WIDTH = 900 
HEIGHT = 700 

sheep = Sheep("sheep", 100, 200)

def draw(): 
    screen.fill((128, 81, 9))
    sheep.draw(screen)

def update(num_of_updates): 
        #choice = random.randrange(1,3)
        #if(choice == 1): 
        sheep.move_right()
        #lif(choice == 2): 
         #   sheep.move_left()
        #elif(choice == 3): 
         #   sheep.move_up()
        #elif(choice == 2): 
        sheep.move_down()
       

update(100)