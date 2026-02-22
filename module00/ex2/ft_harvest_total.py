
def ft_harvest_total():
    day = 1
    harvest = 0
    while day < 4:
        harvest = harvest + int(input("Day " + str(day) + " harvest: "))
        day += 1
    print("Total harvest:", harvest)
