# A king taxes his subjects. If their income is over 1000 gold, the tax is 20%. If it's over 500 but not over 1000, it's 15%. If it's 500 or less but greater than 0, it's 10%. If income is 0, there is no tax. Given an income, calculate and print the exact gold amount owed in tax.

gold=int(input("Enter the gold amount:"))

if gold>1000:
    x= gold*(0.20)
    print("Total tax -- 20%")
    print("Total tax:",x)
    

elif gold>500 and gold<1000:
    y=gold*(0.15)
    print("total tax-15% ")
    print("Tax=",y)

elif gold<=500 and gold>0:
    z=gold*(0.10)
    print("tax-10%")
    print("Tax-",z)

else:
    print("No tax")