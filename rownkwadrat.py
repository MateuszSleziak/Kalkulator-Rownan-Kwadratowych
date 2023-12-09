import math

def rowania_kwadratowe():
    a = float(input("Podaj \"a\": "))
    b = float(input("Podaj \"b\": "))
    c = float(input("Podaj \"c\": "))
    return a, b, c

def delt(a, b, c):
    delta = b**2 - 4*a*c
    return delta

def mzerowe1(a, b, c):
    delta = delt(a, b, c)
    x_1 = (-b - math.sqrt(delta)) / (2*a)
    return x_1

def mzerowe2(a, b, c):
    delta = delt(a, b, c)
    x_2 = (-b + math.sqrt(delta)) / (2*a)
    return x_2

if __name__ == "__main__":
    a, b, c = rowania_kwadratowe()
    delta = delt(a, b, c)

    if delta < 0:
        print("Brak pierwiastków rzeczywistych.")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Jeden pierwiastek rzeczywisty: {x}")
    else:
        x1 = mzerowe1(a, b, c)
        x2 = mzerowe2(a, b, c)
        print(f"Dwa pierwiastki rzeczywiste: X1 = {x1}, X2 = {x2}")