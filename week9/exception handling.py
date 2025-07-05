
try:
    print(x)
except NameError:
    print ("something went wrong")
else:
    print("everthing went wrong")
    
    x=-1
    if x<0:
        raise Exception("Sorry no number below zero")
    