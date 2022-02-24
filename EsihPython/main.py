import statFunction
import keyboard
import time

print("""There is a statistics program made to calculate the variance, 
    the standardDerivation , the mean and the customTotal of statistics data,
    press Q to quit 
    """)

data=[0,10,20,15,13,7,0,20]
            
print(f"""The mean of the list is: {statFunction.mean(data)}  
    The variance is: {statFunction.variance(data)}
    The standard derivation is : {statFunction.standardDeviation(data)} 
    The customTotal is: {statFunction.customTotal(data)} 
      """)

    

