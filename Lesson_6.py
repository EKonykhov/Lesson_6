#=====#1=====

import time
x = 1
n = 2

class Tl:
    __ = "private"

    def r(s):
        for i in range(0,x):
            print(f"\033[31m Красный")
            time.sleep(n)
            print(f"\033[33m Желтый")
            time.sleep(n)
            print(f"\033[32m Зеленый")
            time.sleep(n)
            print(f"\033[33m Желтый")
            time.sleep(n)

Tl().r()

#=====#2=====

o,p,n,m = 20,5000,25,5
class r:
    def __init__(s, l, w):
        s._l = l
        s._w = w
    def x(s):
        return s._l*s._w*n*m/1000
print(f"Результат: {r(o,p).x()} т")

#=====#3=====

name, surname, position, wage, bonus = "a", 'b', "ccc", 10, 10

class Worker:
    def __init__(s, name, surname, position, wage, bonus):
        s.name = name
        s.surname = surname
        s.position = position
        s._income = {"wage": wage, "bonus": bonus}

class Pos (Worker):
    def y (s):
        return f"Работник: {s.name} {s.surname}, из: {s.position} с доходом: {sum(s._income.values())} руб."

print(Pos(name, surname, "веселого отдела IT", wage, bonus).y())

#=====#random и if (4-е задание ниже!)=====

import random

x = {1:"TownCar", 2:"SportCar", 3:"WorkCar", 4:"PoliceCar"}
x1 = {1:"куда то поехал", 2:"почему то остановился"}
x2 = {1:"повернул", 2:"не повернул"}
x3 = {1:"на право", 2:"на лево"}

y = random.randint(1,4)
y2 = random.randint(1,2)

if y2 == 2: y3 = 0
else:
    y3 = random.randint(30,70)

if y == 1 and y3 > 60 or y == 3 and y3 > 40: x4 = "ВНИМАНИЕ ПРЕВЫШЕНА СКОРОСТЬ!!!"
elif y3 == 0: x4 = "Начните движение!"
else:
    x4 = "Счастливого пути"

print(f"Ваш {x[y]} {x1[y2]} и {x2[y2]}: {x3[y2]}! Со скоростью: ({y3} км/ч). {x4}")

#=====#4=====

import random

name, color, speed, is_police = 'Грузовик', "белый", 10, 0

x = {1:"TownCar", 2:"SportCar", 3:"WorkCar", 4:"PoliceCar"}
x1 = random.randint(0,1)
x2 = random.randint(1,4)

class Car:
    def __init__(s, name, color, speed, is_police=0):
        s.name = name
        s.color = color
        s.speed = speed
        s.is_police = is_police

    def go(s):
        print(f"Ваш {s.name} поехал")

    def stop(s):
        print(f"Ваш {s.name} остановился")

    def turn(s):
        print(f"Ваш {s.name} повернул на: {'Налево' if x1 == 0 else 'Направо'}.")

    def show_speed(s):
        return (f"Ваш {s.name} скорость: {s.speed}.")


class TownCar(Car):
    def show_speed(s):
        return (f"Ваш {s.name} скорость: {s.speed}. Превышение скорости!"
                if s.speed > 60 else f"Ваш {s.name} скорость: {s.speed}.")

class WorkCar(Car):
    def show_speed(s):
        return (f"Ваш {s.name} скорость: {s.speed}. Превышение скорости!"
                if s.speed > 40 else f"Ваш {s.name} скорость: {s.speed}.")

print(TownCar(name, color, 80).show_speed())
TownCar(name, color, 80).turn()
TownCar(name, color, 80).stop()

#=====#5=====

x = "уроки рисования"

class Stationery:
    def __init__(s, title = x):
        s.title = title

    def draw (s):
        print(f"Начало: {s.title}")

class Pen(Stationery):
    def draw(s):
        print(f"Рисуйте: {s.title} ручкой")

class Pencil(Stationery):
    def draw(s):
        print(f"Рисуйте: {s.title} карандашом")

class Marker(Stationery):
    def draw(s):
        print(f"Рисуйте: {s.title} маркером")

Stationery().draw()
Pen("Parker").draw()
Marker("555").draw()