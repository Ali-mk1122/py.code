import pygame
import random

pygame.init()


class Scoreboard:
    def __init__(self, gun):
        self.width = 80
        self.height = 50
        self.color = (10, 10, 10)
        self.font = pygame.font.Font(None, 36)
        self.gun = gun

    def show(self, display):
        score_text = self.font.render(f"Score: {self.gun.score}", True, self.color)
        display.blit(score_text, (10, 10))


class Drone:
    def __init__(self, game):
        self.x = -50
        self.y = random.randint(0, game.height // 2)
        self.image = pygame.image.load("first drone image.png")
        self.scaled_image = pygame.transform.scale(self.image, (80, 80))
        self.speed = 2
        self.rect = self.scaled_image.get_rect(topleft=(self.x, self.y))

    def show(self, display):
        display.blit(self.scaled_image, (self.x, self.y))

    def fly(self):
        self.x += self.speed
        self.rect.x = self.x

    def check_collision(self, gun_rect):
        return self.rect.colliderect(gun_rect)


class DroneTwo:
    def __init__(self, game):
        self.x = 1050
        self.y = random.randint(0, game.height // 2)
        self.image = pygame.image.load("secend drone image.png")
        self.scaled_image = pygame.transform.scale(self.image, (100, 100))
        self.speed = 2
        self.rect = self.scaled_image.get_rect(topright=(self.x, self.y))

    def show(self, display):
        display.blit(self.scaled_image, (self.x, self.y))

    def fly(self):
        self.x -= self.speed
        self.rect.x = self.x

    def check_collision(self, gun_rect):
        return self.rect.colliderect(gun_rect)

class Gun:
    def __init__(self, game):
        self.x = game.width // 2
        self.y = game.height // 2
        self.image = pygame.image.load("gun aim image .png")
        self.scaled_image = pygame.transform.scale(self.image, (80, 80))
        self.score = 0
        self.sound = pygame.mixer.Sound("gun sound .mp3")
        self.rect = self.scaled_image.get_rect(center=(self.x, self.y))

    def show(self, display):
        display.blit(self.scaled_image, (self.x, self.y))

    def update_position(self, mouse_pos):
        self.x, self.y = mouse_pos
        self.rect.center = (self.x, self.y)

class Game:
    def __init__(self):
        self.width = 1000
        self.height = 600
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Bird Shooting Game")
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load("background image .jpg")
        self.fps = 30

    def play(self):
        pygame.mouse.set_visible(False)
        my_gun = Gun(self)
        scoreboard = Scoreboard(my_gun)
        drones = []
        dronets = []

        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEMOTION:
                    my_gun.update_position(event.pos)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    my_gun.sound.play()
                    for drone in drones[:]:
                        if drone.check_collision(my_gun.rect):
                            drones.remove(drone)
                            my_gun.score += 1
                            print("Score:", my_gun.score)
                    for dronet in dronets[:]:
                        if dronet.check_collision(my_gun.rect):
                            dronets.remove(dronet)
                            my_gun.score += 2
                            print("Score:", my_gun.score)

               
            if random.random() < 0.02:
                drones.append(Drone(self))
            if random.random() < 0.02:
                dronets.append(DroneTwo(self))

            
            for drone in drones[:]:
                drone.fly()
                if drone.x > self.width:
                    drones.remove(drone)

            for dronet in dronets[:]:
                dronet.fly()
                if dronet.x < -100:
                    dronets.remove(dronet)

            
            self.display.blit(self.background, (0, 0))

            for drone in drones:
                drone.show(self.display)

            for dronet in dronets:
                dronet.show(self.display)

            my_gun.show(self.display)
            scoreboard.show(self.display)

            pygame.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    game = Game()
    game.play()