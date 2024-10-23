import pygame
import random

class Apple:
    def __init__(self):
        self.r = 8
        self.x = random.randint(16, width )
        self.y = random.randint(16, height )
        self.color = (255,0,0)

    def show(self):
        pygame.draw.circle(display, self.color, [self.x, self.y] , self.r)

       
class Apple_1:
    def __init__(self):
        self.r = 8
        self.x = random.randint(16, width)
        self.y = random.randint(16, height)
        self.color = (255,255,255)
    def show(self):
        pygame.draw.circle(display, self.color, [self.x, self.y] , self.r)    
  


class Snak:
    def __init__(self):
        self.w = 15
        self.h = 15
        # self.ww = width[10:590]
        # self.hh = height[10:390]
        self.x = width//2
        self.y = height//2
        self.color = (0,0,0)
        self.speed = 3 
        self.score = 0
        self.x_change = 0
        self.y_change = 0
        self.body = []
        
    def eat(self):
        if (apple.x-apple.r<= self.x<=apple.x+ apple.r) and (apple.y-apple.r <= self.y<=apple.y+apple.r):
           self.score+=1
           return True
        else:
            return False
    def eat_2(self):
        if (apple_a.x-apple_a.r <= self.x<=apple_a.x+ apple_a.r) and (apple_a.y-apple_a.r <= self.y<=apple_a.y+apple_a.r):
           self.score-=1
           return True
        else:
            return False   
        
    def show(self):
        pygame.draw.rect(display, self.color, [self.x , self.y, self.w,self.h])
        
        for item in self.body:
            pygame.draw.rect(display, self.color, [item["x"], item["y"], self.w, self.h])    
    
    def move(self):
        self.body.append({"x":self.x, "y":self.y})
        if len(self.body)> self.score:
            self.body.remove(self.body[0])
        # if self.body == len(self.hh):    #محدودیت حرکت 
        #     return Ture
        # else :
        #     self.body.remove(self.body[0])
        
        # if self.body == len(self.ww):    #محدودیت حرکت 
        #     return Ture
        # else :
        #     self.body.remove(self.body[0])

        if self.x_change == -1:
            self.x-=self.speed 
        elif self.x_change ==1:
            self.x+=self.speed
        elif self.y_change == -1:
            self.y-=self.speed
        elif self.y_change == 1:
            self.y += self.speed      
    
# class Score_borde:
#     def __init__(self): 
#         self.width_score = width[20:120]
#         self.height_score = height[5:20]
#         self.color = (255,0,0)
#     def show(self):
#         pygame.draw.rect(display,self.color, [self.height_score, self.width_score ])

if __name__ == "__main__":
    pygame.init()
    width = 600
    height = 400
    display = pygame.display.set_mode((width, height))
    
    clock = pygame.time.Clock()
    snak = Snak()
    apple = Apple()
    apple_a = Apple_1()
    # score_borde= Score_borde()
    while True:
        for event in pygame.event.get():
            print(event)
            
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                snak.speed += 2
            if event .type == pygame.KEYUP:
                snak.speed -= 2
                if event.key == pygame.K_UP:
                    snak.y_change = -1
                    snak.x_change = 0
                elif event.key == pygame.K_DOWN:
                    snak.y_change = 1
                    snak.x_change =0
                elif event.key == pygame.K_LEFT:
                    snak.y_change = 0
                    snak.x_change = -1
                elif event.key == pygame.K_RIGHT:
                    snak.y_change = 0
                    snak.x_change = 1
               
        
        display.fill((0, 255, 0)) 
        snak.show()
        snak.move()
        result = snak.eat() 
        if result == True:
           apple =  Apple()
        result_1 = snak.eat_2()
        if result_1 == True:
            apple_a == Apple_1()
        apple.show()
        apple_a.show()
        # score_borde.show() 
        pygame.display.update()
        clock.tick(15)
