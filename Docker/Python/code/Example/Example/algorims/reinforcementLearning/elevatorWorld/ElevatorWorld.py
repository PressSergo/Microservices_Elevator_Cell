import numpy as np


currentFloors = [1,1,3,4,2,2]
dependFloors = [4,3,1,1,3,1]

class Elevator:

    def __init__(self):
        self.currentElevatorFloor = 1
        self.currentFloor = currentFloors.copy()
        self.dependFloor = dependFloors.copy()
        self.activeDependFloor = []

    def reset(self):
        self.currentElevatorFloor = 1
        self.currentFloor = currentFloors.copy()
        self.dependFloor = dependFloors.copy()
        self.activeDependFloor = []
        return np.array([0])

    def action(self,move):
        rewards = 0
        if self.currentElevatorFloor in self.currentFloor:
            self.activeDependFloor.append(self.dependFloor[self.currentFloor.index(self.currentElevatorFloor)])
            self.dependFloor.remove(self.dependFloor[self.currentFloor.index(self.currentElevatorFloor)])
            self.currentFloor.remove(self.currentElevatorFloor)
            print("пассажир подобран на этаже: {}".format(self.currentElevatorFloor))
            rewards+=1

        if move == 1:
            self.currentElevatorFloor+=1
            print("лифт движется вверх")
        else:
            self.currentElevatorFloor-=1
            print("лифт движется вниз")

        if self.currentElevatorFloor in self.currentFloor:
            self.activeDependFloor.append(self.dependFloor[self.currentFloor.index(self.currentElevatorFloor)])
            self.dependFloor.remove(self.dependFloor[self.currentFloor.index(self.currentElevatorFloor)])
            self.currentFloor.remove(self.currentElevatorFloor)
            print("пассажир подобран на этаже: {}".format(self.currentElevatorFloor))
            rewards += 1

        if self.currentElevatorFloor in self.activeDependFloor:
            self.activeDependFloor.remove(self.currentElevatorFloor)
            print("пассажир вышел на этаже: {}".format(self.currentElevatorFloor))
            rewards += 1

        return np.array([self.currentElevatorFloor, move ,len(self.activeDependFloor),len(self.currentFloor)]), rewards