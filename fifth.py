# A dragon guards three piles of gold: 10, 15, and 20 coins. A knight can only pass if the total is NOT exactly 45, AND the first pile has exactly 10 coins. Tell the knight if he should 'PASS' or 'FAIL'.

one=int(input("ENter the first pill value"))
two=int(input("enter value of second pills"))
three=int(input("enter the value of third pills"))

if one!=10:
    print("first pills in not 10")

elif one+two+three==45:
    print("fail")

else:
    print("pass")
