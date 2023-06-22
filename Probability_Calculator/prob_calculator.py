import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = list()
        for key, value in kwargs.items():
            self.contents += [key] * int(value)


    def draw(self, number):
        num_of_collors = len(self.contents)
        if number >= num_of_collors:
            return self.contents
        result = []
        for i in range(0, number):
            trial = random.randint(0, num_of_collors - 1)
            result.append(self.contents.pop(trial))
            num_of_collors -= 1
        return result
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    fit = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        balls_drawn_dict = dict()
        #convert ball_drawn to dict to prepare for comparasion
        for j in range(len(balls_drawn)):
            balls_drawn_dict[balls_drawn[j]] = balls_drawn_dict.get(balls_drawn[j], 0) +1
        res = is_sub_dict(balls_drawn_dict, expected_balls)
        if res :
            fit = fit + 1
    return fit / num_experiments

def is_sub_dict(dictionary, subdictionary):
    len_sub = len(subdictionary)
    res = 0
    for key, value in dictionary.items():
        for k, v in subdictionary.items():
            if key == k:
                if (v <= value):
                    res = res + 1
    if res == len_sub:
        return True
    else :
        return False