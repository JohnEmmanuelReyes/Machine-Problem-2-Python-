from math import sqrt 
print("\n\n!!! Input Three Points to the Function: circle() !!!\n\ncircle(  p1(x,y)  ,  p2(x,y)  ,  p3(x,y)  )")
print("Example input: circle([10,2],[3,1],[-4,5]))\n\n***Please Input Three Points***")

def circle(p1,p2,p3):
    #Getting the X in the given points
    x1=p1[0];    x2=p2[0];    x3=p3[0]
    #Getting the Y in the given points
    y1=p1[1];    y2=p2[1];    y3=p3[1]

    #Summarize Equation for k
    k = -((((x1**2)-(x3**2)) * (x1 - x2) + ((y1**2)-(y3**2)) * (x1 - x2) + 
         ((x2**2)-(x1**2)) * (x1 - x3) + ((y2**2)-(y1**2)) * (x1 - x3)) // 
         (2 * ((y3 - y1) * (x1 - x2) - (y2 - y1) * (x1 - x3))))
    #Summarize Equation for h      
    h = -((((x1**2)-(x3**2)) * (y1 - y2) + ((y1**2)-(y3**2)) * (y1 - y2) + 
         ((x2**2)-(x1**2)) * (y1 - y3) + ((y2**2)-(y1**2)) * (y1 - y3)) //  
         (2 * ((x3 - x1 ) * (y1 - y2) - (x2 - x1 ) * (y1 - y3))))  
    #center equation
    c = (-(x1**2)-(y1**2)-2*-h*x1-2*-k*y1);  
    
    
    sqr= (h*h)+(k*k)-c  
    #Radius of the circle
    r = round(sqrt(sqr), 3);  
    #Getting the Vector [x,y,z]
    x=-2*h;
    y=-2*k;
    z= (h**2)+(k**2)-(r**2);
  
    print("Centre = (", h, ", ", k, ")");  
    print("Radius = ", r);  
    print("Vector = (", x,", ",y,", ", z,")")

    return
    

