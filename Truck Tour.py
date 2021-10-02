#!/bin/python3

import math
import os
import random
import re
import sys


def truckTour(petrolpumps):
    position = fuel = 0
    for i in range (len(petrolpumps)):
        fuel += petrolpumps[i][0] - petrolpumps[i][1]    #calculate the remaining fuel and add to the fuel variable
        if fuel < 0:       #negative fuel capacity  
            position = i + 1       #update the position to next petrolpump
            fuel = 0
            
    return position       
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
