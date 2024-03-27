import math
import random
import power_function
import json
with open('config.json', 'r') as f:
    config = json.load(f)
l = config["l"]
h = config["h"]
k = config["k"]

n_it = 0.1


def fun(x, n):
    return power_function.fun(x, n)


def inverse_fun(y, n):
    return power_function.inverse_fun(y, n)


def check(n):
    mid = (l + h) / 2
    criterion = fun(mid, n)
    lower = fun(l, n)
    upper = fun(h, n)
    cnt_over_mid = 0
    cnt_under_mid = 0
    random.seed(0)

    for i in range(1000000):
        num = random.uniform(lower, upper)
        if num > criterion:
            cnt_over_mid += 1
        else:
            cnt_under_mid += 1

    print(f'小数出现的概率是大数的{cnt_under_mid / cnt_over_mid}倍')


while 1:
    x1 = fun(l, n_it)
    x2 = fun(h, n_it)
    x3 = fun((l + h) / 2, n_it)

    if math.fabs((x3 - x1) / (x2 - x3) - k) < 0.01:
        break
    n_it += 0.01


print(n_it)
check(n_it)
config["n"] = n_it

with open('config.json', 'w') as file:
    json.dump(config, file, indent=4)
