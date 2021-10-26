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

        self.vx = 2
        self.xy = 2

    def show(self):
        pygame.draw.circle(self.display, self.color,
                           (self.center_x,
                            self.center_y), self.radius)

    def go(self):
        self.center_x += self.vx
        self.center_y += self.xy

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
        self.xy = 0

    def is_touch_border(self, width, height):
        if self.center_x - self.radius < 0: return True
        if self.center_x + self.radius > width: return True
        if self.center_y - self.radius < 0: return True
        if self.center_y + self.radius > height: return True
        return False

    #
    def is_iid(self, x2, y2):
        x1 = self.center_x
        y1 = self.center_y

        if ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) < (
                self.radius * self.radius): return True
        return False

    def is_offside(self, width, height):
        if self.center_x + self.radius < 0: return True
        if self.center_x - self.radius > width: return True
        if self.center_y + self.radius < 0: return True
        if self.center_y - self.radius > height: return True
        return False


class RandomPointBall(Ball):
    def __init__(self, display):
        super().__init__(display)

        self.color = pygame.Color('green')

        width, height = display.get_size()
        self.center_x = random.randint(self.radius,
                                       width - self.radius)
        self.center_y = random.randint(self.radius,
                                       height - self.radius)


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
            if not self.vx == 0 or self.vy == 0:
                break


class Report:
    # display.get_size()
    # def __init__(self, balls_remaining):
    #     self.balls_remaining = balls_remaining
    #     fontObj = pygame.font.Font(self.balls_remaining, 50)
    #     textSurfaceObj = fontObj.render('Hello world!',
    #                                     True, yellow, blue)
    #     textRectObj = textSurfaceObj.get_rect()
    #     textRectObj.center = (350, 200)''
    def __init__(self, font, center_x, center_y):
        self.font = font
        self.xy = center_x
        self.yx = center_y

    def set_text(self,display, str):
        # создать текстовый объект suface,
        # на котором нарисован текст.

        white = (255, 255, 255)
        green = (0, 255, 0)
        blue = (0, 0, 128)

        text = font.render(str, True, green, blue)
        # создать прямоугольный объект для
        # текстовая поверхность объекта
        textRect = text.get_rect()
        # установить центр прямоугольного объекта.
        textRect.center = (self.xy, self.yx)
        display.blit(text, textRect)

    # def report_ball(balls):


pygame.init()
pygame.display.set_caption("Безумные шарики")
width, height = 700, 400
display = pygame.display.set_mode((width, height))
display.fill(pygame.Color('white'))

balls = []

for i in range(10):
    ball = RandomPointMoveBall(display)
    ball.show()
    balls.append(ball)

font = pygame.font.Font('freesansbold.ttf', 32)
report = Report(font, width//2, 25)
report.set_text(display,"нет нет")
pygame.display.flip()

"""         GAME ZONE         """
"""---------------------------"""

time.sleep(.5)
clock = pygame.time.Clock()
status = 0

while True:
    count = 0
    event_list = pygame.event.get()
    # x_maus, y_maus = pygame.mouse.get_pos()
    # print(x_maus, y_maus)
    for event in event_list:

        # if event.type == pygame.QUIT:
        #     pygame.quit()
        #     continue
        #

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     count = 0
        #     for ball in balls:
        #         if ball.is_iid(x_maus, y_maus):
        #             ball.color = pygame.Color(0, 0, 0)
        #             ball.stop()
        #             count+=1
        if event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls:
                ball.stop()
            print('report')
            status = 1

    if status == 1:
        for ball in balls:
            if not ball.is_touch_border(width, height): count += 1
        print(count)
        report.set_text(display, f'поймали = {count}')

    for ball in balls:
        ball.move()
    pygame.display.flip()
    clock.tick(60)

    for event in event_list:
        if event.type == pygame.QUIT:
            pygame.quit()
            break
