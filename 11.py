import turtle as t
import math
gtpi=360
point=1
def circle(n,rl):
    for i in range(math.ceil(gtpi*(1+0.1*n))):
        t.forward(1)
        if rl:
            t.left(1/(1+0.1*n))
        else:
            t.right(1/(1+0.1*n))
allcirclespl1=21
halfpi=90
t.left(halfpi)
for i in range(1,allcirclespl1):
    for j in range(2):
        circle(i,j)
    
    
