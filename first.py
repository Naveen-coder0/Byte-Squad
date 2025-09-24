# You are at coordinates (x, y) in a maze. You can escape if you are on the edge (x=0 or y=0) but NOT if you are in a corner (x=0 AND y=0). If you can escape, print 'ESCAPE'. Otherwise, print 'TRAPPED'.

x=int(input("Enter x coordinate: "))
y=int(input("Enter y coordinate: "))
if x==0 or y==0 :
    if x==0 and y==0:
        print("Traped")
    elif x==0 or y==0 :
     print("escaped")

