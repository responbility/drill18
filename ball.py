from pico2d import *
import game_world
import game_framework
import random

class Ball:
    image = None

    def __init__(self, x = None, y = None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(100, 1180)
        self.y = y if y else random.randint(100, 924)

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def create_ball():
        ball = Ball()
        game_world.add_object(ball, 1)
        return ball
    create_ball = staticmethod(create_ball)
    def clear_ball(ball):
        game_world.remove_object(ball)
    clear_ball = staticmethod(clear_ball)
    def move_to(x, y):
        for ball in game_world.objects_at_layer(1):
            ball.x = x
            ball.y = y
    move_to = staticmethod(move_to)
    def clear_all():
        for ball in game_world.objects_at_layer(1):
            game_world.remove_object(ball)
    clear_all = staticmethod(clear_all)
    
