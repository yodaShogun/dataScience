from math import sqrt

def askElement():
    dataElement = 0
    while dataElement == 0:
        dataStr = input("input a number: ")
        try:
            dataElement = int(dataStr)
        except ValueError:
            print("They should be a number.......Try Again")
        else:
            return dataElement


def mean(statList):
    return sum(statList)/len(statList)
    
def variance(statList):
    somme = 0
    m = mean(statList)
    for v in statList: 
        somme += (v-m)**2
    return somme / len(statList)

def standardDeviation(statList):
     return sqrt(variance(statList)) 


def customTotal(statList):
    total = 0
    for S in statList:
        total += S
    return total

