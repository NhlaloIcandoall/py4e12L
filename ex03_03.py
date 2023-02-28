score = input("Enter Score: ")
try:
    fs = float(score)
except:
    print('Error, please put a numeric score')
    quit()

if fs >= 0.9:
    print('A')

elif fs >= 0.8:
    print('B')

elif fs >= 0.7:
    print('C')

elif fs >= 0.6:
    print('D')

elif fs < 0.6:
    print('F')

else:
    print('error, input out of range')
