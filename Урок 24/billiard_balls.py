import pygame
import random
import time

pygame.font.init()


class Ball:
    def __init__(self, display):
        self.display = display
        self.color = pygame.Color('red')
        self.center_x = 100
        self.center_y = 100
        self.radius = 30
        self.isDD = False

        self.vx = 3
        self.vy = 3

    def show(self):
        pygame.draw.circle(self.display, self.color,
                           (self.center_x,
                            self.center_y), self.radius)

    def go(self):
        self.center_x += self.vx
        self.center_y += self.vy

    def clear(self):
        pygame.draw.circle(self.display,
                           pygame.Color('white'),
                           (self.center_x, self.center_y),
                           self.radius)

    def move(self):
        self.clear()
        self.go()
        self.show()

    def stop(self):
        self.vx = 0
        self.vy = 0

    def is_touch_border(self, width, height):
        if self.center_x - self.radius < 0:
            return True
        if self.center_x + self.radius > width:
            return True
        if self.center_y - self.radius < 0:
            return True
        if self.center_y + self.radius > height:
            return True
        return False

    def is_arrow_target(self, x2, y2):
        x1 = self.center_x
        y1 = self.center_y

        if ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) < (self.radius * self.radius):
            return True
        return False

    def is_offside(self, width, height):
        if self.center_x + self.radius < 0:
            return True
        if self.center_x - self.radius > width:
            return True
        if self.center_y + self.radius < 0:
            return True
        if self.center_y - self.radius > height:
            return True
        return False


class RandomPointBall(Ball):
    def __init__(self, display):
        super().__init__(display)

        self.color = pygame.Color('green')

        width, height = display.get_size()
        self.center_x = random.randint(self.radius, width - self.radius)
        self.center_y = random.randint(self.radius, height - self.radius)


class PointBall(Ball):
    def __init__(self, display, x, y):
        super().__init__(display)

        self.color = pygame.Color('yellow')

        self.center_x = x
        self.center_y = y


class RandomPointMoveBall(RandomPointBall):
    def __init__(self, display):
        super().__init__(display)

        while True:
            self.vx = random.randint(-3, 3)
            self.vy = random.randint(-3, 3)

            if self.vx != 0 or self.vy != 0:
                break



class BilliardBall(RandomPointMoveBall):
    def __init__(self, display):
        super().__init__(display)
        self.color = pygame.Color('red')

    def go(self):
        super().go()

        width, height = self.display.get_size()
        if self.center_x <= self.radius or self.center_x >= width - self.radius:
            self.vx = -self.vx
        if self.center_y <= self.radius or self.center_y >= height - self.radius:
            self.vy = -self.vy

    def counter_touch(self, count_left, count_right, count_top, count_buttom):
        width, height = self.display.get_size()
        if self.center_x <= self.radius:
            count_left += 1
        if self.center_x >= width - self.radius:
            count_right += 1
        if self.center_y <= self.radius:
            count_top += 1
        if self.center_y >= height - self.radius:
            count_buttom += 1
        return count_left, count_right, count_top, count_buttom
class Report:
    def __init__(self, font, center_x, center_y):
        self.font = font
        self.xy = center_x
        self.yx = center_y

    def set_text(self, display, str):
        green = (0, 255, 0)
        blue = (0, 0, 128)

        text = font.render(str, True, green, blue)
        textRect = text.get_rect()
        textRect.center = (self.xy, self.yx)
        display.blit(text, textRect)


pygame.init()
pygame.display.set_caption("Безумные шарики")
width, height = 700, 400
display = pygame.display.set_mode((width, height))
display.fill(pygame.Color('white'))

balls = []

for i in range(5):
    ball = BilliardBall(display)
    ball.show()
    balls.append(ball)

font = pygame.font.Font('freesansbold.ttf', 16)
report = Report(font, width // 2, 25)
# report.set_text(display,"")
pygame.display.flip()

"""         GAME ZONE         """
"""---------------------------"""

time.sleep(.5)
clock = pygame.time.Clock()
status = 0
count_left, count_right, count_top, count_buttom = 0,0,0,0
while True:

    event_list = pygame.event.get()
    for event in event_list:
        x_maus, y_maus = pygame.mouse.get_pos()

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     for ball in balls:
        #         if not ball.is_arrow_target(x_maus, y_maus):
        #             continue
        #         if ball.is_touch_border(width, height):
        #             continue
        #         ball.color = pygame.Color(0, 0, 0)
        #         ball.isDD = True
        #         ball.stop()
    # count_l = 0
    # count_r = 0
    # count_t = 0
    # count_b = 0

    for ball in balls:
        count_left, count_right, count_top, count_buttom = ball.counter_touch(
            count_left, count_right, count_top, count_buttom)
    report.set_text(display, f'л = {count_left}  П = {count_right}  в = {count_top}  н = {count_buttom}')

    for ball in balls:
        ball.move()
    pygame.display.flip()
    clock.tick(60)

    for event in event_list:
        if event.type == pygame.QUIT:
            pygame.quit()
            break
