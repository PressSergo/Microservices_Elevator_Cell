from statemachine import StateMachine, State
import logging

logger = logging.getLogger(__name__)

cells = [
{"f1": 1, "f2": 3},
        {"f1": 3, "f2": 8},
        {"f1": 5, "f2": 3},
        {"f1": 9, "f2": 1},
        {"f1": 9, "f2": 10},
        {"f1": 1, "f2": 0},
        {"f1": 11, "f2": 2},
        {"f1": 2, "f2": 10},
] # вызовы этажей считываем из RabbitMQ
curerntFloor = 0 # текущий этаж всегда указывать максимальный
maxFloor = 11

class TrafficElevatorMachine(StateMachine):
    initial = State('хол', initial=True)
    up = State('движение вверх')
    down = State('Движение вниз')

    upWord = initial.to(up)
    upDown = up.to(down)
    upFromDown = down.to(up)

    def on_upWord(self,i):
        logger.info('движение вверх, этаж '+i)
        print('движение вверх, этаж '+i)

    def on_upDown(self,i):
        logger.info('движение вниз, этаж '+i)
        print('движение вниз, этаж '+i)

    def on_upFromDown(self,i):
        logger.info('движение вверх, этаж '+i)
        print('движение вверх, этаж '+i)

elevator = TrafficElevatorMachine()

def initialCells(body): # это будет как сслыка чтобы сюда приходили данные
    cells.append(body)

def resolveMove(): # это URL откуда будут уходить данные о движении
    tempResolve = []
    resolveUp = []
    resolveDown = []
    print(cells)
    for i in cells:
        tempResolve.append(i["f2"]-i["f1"])
    print(tempResolve)
    for (i,k) in zip(cells,range(0,len(tempResolve))):
        if tempResolve[k]>=0:
            resolveUp.append(i)
        else:
            resolveDown.append(i)

    resolveUp = sorted(resolveUp, key=lambda floor: floor["f1"])  # Сортируем по этажу вызова
    resolveDown = sorted(resolveDown, key=lambda floor: floor["f1"])  # Сортируем по этажу вызова

    tempResolve.clear()
    tempResolve.append(resolveUp)
    tempResolve.append(resolveDown)
    print(tempResolve)
    return answerMovement(tempResolve)

def answerMovement(resolve):
    upCells = []
    downCells = []

    for i in resolve[0]:
        upCells+=i.values()

    for i in resolve[1]:
        downCells+=i.values()

    upCells.sort()
    downCells.sort(reverse=True)
    return upCells+downCells


resolveMove()