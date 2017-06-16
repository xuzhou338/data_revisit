from random import choice
from matplotlib import pyplot as plt

class RandomWalk():
    def __init__(self, x_start=0, y_start=0, steps=10000):
        self.x_start = x_start
        self.y_start = y_start
        self.steps = list(range(steps))

    def gen_walk(self):
        x, y = [self.x_start], [self.y_start]
        for step in self.steps:
            x.append(x[step] + choice([-2, -1, 1, 2]))
            y.append(y[step] + choice([-2, -1, 1, 2]))
        self.steps.insert(0,0)
        plt.scatter(x, y, s=1, c=self.steps, cmap=plt.cm.Blues)
        plt.xticks([])
        plt.yticks([])
        plt.title("Random Walk")
        plt.show()

if __name__ == "__main__":
    walk = RandomWalk()
    walk.gen_walk()