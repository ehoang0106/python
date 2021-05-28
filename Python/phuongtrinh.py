import math
 

def equation (a, b, c):
    
    if (a == 0):
        if (b == 0):
            print ("the equation has no solution");
        else:
            print ("the equation has only 1 solution: x = ", + (-c / b));
        return;
 
   
    delta = b * b - 4 * a * c;
   
    if (delta > 0):
        x1 = (float)((-b + math.sqrt(delta)) / (2 * a));
        x2 = (float)((-b - math.sqrt(delta)) / (2 * a));
        print ("x1 = ", x1);
        print ("x2 = ", x2);
    elif (delta == 0):
        x1 = (-b / (2 * a));
        print("The equation with a double solution: x1 = x2 = ", x1);
    else:
        print("the equation has no solution!");
 

a = float(input("a = "));
b = float(input("b = "));
c = float(input("c = "));

equation(a, b, c)