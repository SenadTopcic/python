


#njesto = {"blue": 2, "red": 1 , "black": 3 }
#njesto2 = {"blue": 2, "red": 5 }

#res = all(njesto.get(key, None) == val for key, val in njesto2.items())

#print(res)
#expected_balls = {"blue": 3, "red": 3, "black" : 2 }
#balls_drawn = ["blue", "blue", "blue", "blue","red","red","red", "black", "black"]
#print(balls_drawn[1])
#balls_drawn_dict = dict()
#fit = 0
#for j in range(len(balls_drawn)):
#    balls_drawn_dict[balls_drawn[j]] = balls_drawn_dict.get(balls_drawn[j], 0) +1
#print(balls_drawn_dict)
#print(type(balls_drawn_dict['blue']))
#print(expected_balls) 
#res = all(expected_balls.get(key, None) <= val for key, val in balls_drawn_dict.items())
#print(res)
#if res :
#    fit = fit + 1

D = {'red': 1, 'green': 2, 'blue': 2}
S = {'blue': 1, 'red': 1,}
print(len(S))
#res  = set(test_dict2.items()).issubset(set(test_dict1.items()))
res = S.items() <= D.items()

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

print(is_sub_dict(D, S))