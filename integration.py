#Intergral Calculator

def left_reiman_sum():
    integral = 0.0
    str_func = input("Enter f(x) -> ")
    first_bound = float(input("Enter first bound -> "))
    second_bound = float(input("Enter second bound -> "))
    n = float(input("Enter how many rectanges you want to use in Reiman sum calucluation -> "))
    delta_x = abs((second_bound-first_bound))/n

    counter = first_bound

    #This is when integrating backwards
    if first_bound > second_bound:        
        while (second_bound - counter) < .0001:
            func = lambda x: eval(str_func)
            integral+=-1*(func(counter) * delta_x)
            counter-=delta_x
    else:
        while second_bound - counter > .0001:
            func = lambda x: eval(str_func)
            integral+=(func(counter) * delta_x)
            counter+=delta_x

    return integral

print(left_reiman_sum())
