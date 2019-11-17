#Intergral Calculator
import math
from random import uniform
from random import randint
"""IMPORTANT: When inputting a function it most follow python's mathmatical format
            Example: When mutiplying use *, division use /, etc."""
def left_reiman_sum():
    print("Left Reiman Approximation:")
    
    integral = 0.0
    str_func = input("Enter f(x) -> ")
    func = lambda x: eval(str_func)
    
    first_bound = float(input("Enter first bound -> "))
    second_bound = float(input("Enter second bound -> "))
    n = float(input("Enter how many rectangle you want to use in Reiman sum calculation -> "))
    delta_x = (second_bound-first_bound) / n
    counter = first_bound

    #This is when integrating backwards
    if first_bound > second_bound:        
        while second_bound - counter < .00001:
            integral += -1 * (func(counter) * delta_x)
            counter += delta_x
    else:
        while second_bound - counter > .00001:
            integral += (func(counter) * delta_x)
            counter += delta_x

    return integral

def simpson_appox():
    print("Simpson's Apporimation:")
    
    integral = 0.0
    str_func = input("Enter f(x) -> ")
    func = lambda x: eval(str_func)
    
    first_bound = float(input("Enter first bound -> "))
    second_bound = float(input("Enter second bound -> "))
    n = int(input("Enter how many subintervals you want in Simpson's integral aproximation -> "))
    delta_x = (second_bound-first_bound) / n
    counter = first_bound + delta_x

    integral+=func(first_bound) + func(second_bound)
    for c in range(1,n):
        if c % 2 == 0:
            integral+=2*func(counter)
        else:
            integral+=4*func(counter)
        counter+=delta_x
    integral*=delta_x/3.0
    
    return integral

def get_max(func, first_bound, second_bound):
    counter = first_bound
    f_max = func(counter)
    while abs(counter - second_bound) > .00001:
        if func(counter) > f_max:
            f_max = func(counter)
        counter+=.0001
    return f_max

def get_min(func, first_bound, second_bound):
    counter = first_bound
    f_min = func(counter)
    while abs(counter - second_bound) > .00001:
        if func(counter) < f_min:
            f_min = func(counter)
        counter+=.0001
    return f_min

def monte_carlo_method():
    print("Monte Carlo Method")

    in_point = 0
    integral = 0.0
    str_func = input("Enter f(x) -> ")
    func = lambda x: eval(str_func)
    first_bound = float(input("Enter first bound -> "))
    second_bound = float(input("Enter second bound -> "))
    n = int(input("Enter how many trials you want to perform ->"))
    
    delta_x = second_bound - first_bound
    f_max = get_max(func, first_bound, second_bound)
    f_min = get_min(func, first_bound, second_bound)
    known_area = delta_x * (f_max - f_min)
    
    for c in range(n):
        rand_x = randint(first_bound, second_bound)
        rand_y = uniform(f_min, f_max+1)

        if rand_y <= func(rand_x):
            in_point+=1
            
    integral = (in_point / n) * known_area

    return integral
    

print(left_reiman_sum(), '\n')
print(simpson_appox(), '\n')
print(monte_carlo_method())
