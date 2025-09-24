# A guardian has three heads, each speaking a number. You can only pass if the sum of ANY two heads' numbers is greater than the third head's number. This must be true for all three combinations! If you can pass, print 'PROCEED', otherwise, print 'HALT'.

one=int(input("ENter your first number:"))
two=int(input("Enter your second number:"))
three=int(input("Enter your third number:"))

if one+two>three:
    print("halt")

elif one+three>two:
    print("halt")

elif two+three>one:
    print("halt")

else:
    print("proceed")    