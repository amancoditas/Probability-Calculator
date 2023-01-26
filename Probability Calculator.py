import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents += [color] * count

    def draw(self, num_balls):
        if num_balls > len(self.contents):
            return self.contents
        else:
            drawn_balls = random.sample(self.contents, num_balls)
            for ball in drawn_balls:
                self.contents.remove(ball)
            return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0
    for i in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        drawn_balls = copy_hat.draw(num_balls_drawn)
        ball_counts = {}
        for ball in drawn_balls:
            if ball not in ball_counts:
                ball_counts[ball] = 1
            else:
                ball_counts[ball] += 1
        success = True
        for color, count in expected_balls.items():
            if color not in ball
