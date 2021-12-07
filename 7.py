import matplotlib.pyplot as plt

with open('input/7.txt', 'r') as file:

    initialstate = [int(i) for i in file.readlines()[0].strip().split(",")]

    initialstate = sorted(initialstate)

    fuelcostlista = []
    fuelcostlistb = []

    fuelcosta = []
    fuelcostb = []

    for i in range(2000):
        for state in initialstate:
            x = abs(i - state)
            cost = (x*(x+1))/2
            fuelcostb.append(cost)
            fuelcosta.append(x)
        fuelcostlistb.append(sum(fuelcostb))
        fuelcostlista.append(sum(fuelcosta))
        fuelcosta = []
        fuelcostb = []

    print(int(min(fuelcostlista)))
    print(int(min(fuelcostlistb)))