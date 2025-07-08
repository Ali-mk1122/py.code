import pygame
import random

# ابتدا ابعاد صفحه را تعریف می‌کنیم
width = 600
height = 400

class Apple:
    def __init__(self):
        self.r = 8
        self.x = random.randint(16, width - 16)
        self.y = random.randint(16, height - 16)
        self.color = (255, 0, 0)

    def show(self):
        pygame.draw.circle(display, self.color, [self.x, self.y], self.r)


class Apple_1:
    def __init__(self):
        self.r = 8
        self.x = random.randint(16, width - 16)
        self.y = random.randint(16, height - 16)
        self.color = (255, 255, 255)

    def show(self):
        pygame.draw.circle(display, self.color, [self.x, self.y], self.r)


class Snak:
    def __init__(self):
        self.w = 15
        self.h = 15
        self.x = width // 2
        self.y = height // 2
        self.color = (0, 0, 0)
        self.speed = 4
        self.score = 0
        self.x_change = 0
        self.y_change = 0
        self.body = []

    def eat(self):
        if (apple.x - apple.r <= self.x <= apple.x + apple.r) and (apple.y - apple.r <= self.y <= apple.y + apple.r):
            self.score += 1
            return True
        return False

    def eat_2(self):
        if (apple_a.x - apple_a.r <= self.x <= apple_a.x + apple_a.r) and (apple_a.y - apple_a.r <= self.y <= apple_a.y + apple_a.r):
            self.score -= 1
            return True
        return False

    def show(self):
        pygame.draw.rect(display, self.color, [self.x, self.y, self.w, self.h])
        for item in self.body:
            pygame.draw.rect(display, self.color, [item["x"], item["y"], self.w, self.h])

    def move(self):
        # اضافه کردن موقعیت فعلی به بدنه مار
        self.body.append({"x": self.x, "y": self.y})
        
        # اگر طول بدنه بیشتر از نمره باشد، اولین عنصر را حذف کن
        if len(self.body) > self.score:
            del self.body[0]

        # حرکت مار بر اساس تغییرات x و y
        if self.x_change == -1:
            self.x -= self.speed
        elif self.x_change == 1:
            self.x += self.speed
        elif self.y_change == -1:
            self.y -= self.speed
        elif self.y_change == 1:
            self.y += self.speed

        # بررسی برخورد با دیوار
        if (self.x < 0 or self.x >= width or self.y < 0 or self.y >= height):
            return True
        return False


class Score_borde:
    def __init__(self):
        self.color = (255, 0, 0)

    def show(self):
        font = pygame.font.SysFont("comicsansms", 35)
        score_text = font.render(f"Score: {snak.score}", True, self.color)
        display.blit(score_text, [10, 10])


if __name__ == "__main__":
    pygame.init()
    display = pygame.display.set_mode((width, height))

    clock = pygame.time.Clock()
    snak = Snak()
    apple = Apple()
    apple_a = Apple_1()
    score_borde = Score_borde()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snak.y_change != 1:
                    snak.y_change = -1
                    snak.x_change = 0
                elif event.key == pygame.K_DOWN and snak.y_change != -1:
                    snak.y_change = 1
                    snak.x_change = 0
                elif event.key == pygame.K_LEFT and snak.x_change != 1:
                    snak.y_change = 0
                    snak.x_change = -1
                elif event.key == pygame.K_RIGHT and snak.x_change != -1:
                    snak.y_change = 0
                    snak.x_change = 1

        display.fill((0, 255, 0))
        
        if snak.move():
            print("Game Over!")
            pygame.quit()
            exit()

        if snak.eat():
            apple = Apple()

        if snak.eat_2():
            apple_a = Apple_1()

        snak.show()
        apple.show()
        apple_a.show()
        score_borde.show()

        pygame.display.update()
        clock.tick(15)
