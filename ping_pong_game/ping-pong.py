import pygame
pygame.init()

class Color:
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    green = (0, 50, 0)

class Game:
    width = 700
    height = 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Ping-Pong")
    clock = pygame.time.Clock()
    fps = 60
    font = pygame.font.SysFont("Arial", 30)

class Racket:
    def __init__(self):
        self.x = 30
        self.y = Game.height // 2 - 40
        self.w = 10
        self.h = 80
        self.speed = 5
        self.color = Color.red

    def show(self):
        pygame.draw.rect(Game.screen, self.color, [self.x, self.y, self.w, self.h])

    def move(self, keys):
        if keys[pygame.K_w] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_s] and self.y + self.h < Game.height:
            self.y += self.speed

class RacketTwo:
    def __init__(self):
        self.x = Game.width - 40
        self.y = Game.height // 2 - 40
        self.w = 10
        self.h = 80
        self.speed = 4
        self.color = Color.blue

    def show(self):
        pygame.draw.rect(Game.screen, self.color, [self.x, self.y, self.w, self.h])

    def move_ai(self, ball_y):
        
        if self.y + self.h // 2 < ball_y and self.y + self.h < Game.height:
            self.y += self.speed
        elif self.y + self.h // 2 > ball_y and self.y > 0:
            self.y -= self.speed

class Ball:
    def __init__(self):
        self.r = 10
        self.x = Game.width // 2
        self.y = Game.height // 2
        self.speed = 4
        self.color = Color.yellow
        self.x_direction = 1
        self.y_direction = -1

    def show(self):
        pygame.draw.circle(Game.screen, self.color, [int(self.x), int(self.y)], self.r)

    def move(self, racket1, racket2, score):
        self.x += self.speed * self.x_direction
        self.y += self.speed * self.y_direction

        
        if self.y <= 0 or self.y >= Game.height:
            self.y_direction *= -1

        
        if (self.x - self.r <= racket1.x + racket1.w and racket1.y < self.y < racket1.y + racket1.h):
            self.x_direction = 1
        elif (self.x + self.r >= racket2.x and racket2.y < self.y < racket2.y + racket2.h):
            self.x_direction = -1

        
        if self.x < 0:
            score['player2'] += 1
            self.reset()
        elif self.x > Game.width:
            score['player1'] += 1
            self.reset()

    def reset(self):
        self.x = Game.width // 2
        self.y = Game.height // 2
        self.x_direction *= -1

def draw_score(score):
    text = Game.font.render(f"{score['player1']}  :  {score['player2']}", True, Color.white)
    Game.screen.blit(text, (Game.width//2 - text.get_width()//2, 20))

def main():
    ball = Ball()
    racket1 = Racket()
    racket2 = RacketTwo()
    score = {'player1': 0, 'player2': 0}

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        racket1.move(keys)
        racket2.move_ai(ball.y)
        ball.move(racket1, racket2, score)

        Game.screen.fill(Color.green)
        pygame.draw.rect(Game.screen, Color.white, [0, 0, Game.width, Game.height], 10)
        pygame.draw.aaline(Game.screen, Color.white, [Game.width / 2, 0], [Game.width / 2, Game.height])

        racket1.show()
        racket2.show()
        ball.show()
        draw_score(score)

        pygame.display.update()
        Game.clock.tick(Game.fps)

if __name__ == "__main__":
    main()
                    
        
    