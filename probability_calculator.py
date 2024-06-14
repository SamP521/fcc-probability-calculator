import copy
import random

class Hat:
    def __init__(self, **all_items):
        self.contents = []
        self.drawn = []

        for color, number in all_items.items():
            color = [color] * number
            self.contents.extend(color)

    def __str__(self):
        return str(self.contents)

    def draw(self, amount):
        if amount < len(self.contents):
            for n in range(amount):
                self.drawn += [self.contents.pop(random.randrange(len(self.contents)))]
            return self.drawn

        self.drawn = copy.copy(self.contents)
        self.contents.clear()
        return self.drawn  

def compare_lists(list1, list2):
    for item in set(list1):
        if list1.count(item) > list2.count(item):
            return False
    return True     
        
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_total = 0
    prob_drawn = []

    for color, number in expected_balls.items():
        color = [color] * number
        prob_drawn.extend(color)

    for n in range(num_experiments):
        test_hat = copy.deepcopy(hat)
        if compare_lists(prob_drawn, test_hat.draw(num_balls_drawn)):
            success_total += 1

    probability = success_total / num_experiments
    return probability