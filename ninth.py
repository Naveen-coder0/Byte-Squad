# A potion's color changes based on temperature. If it's below 0, it turns 'BLUE'. If it's above 100, it turns 'RED'. If it's exactly 50, it turns 'PURPLE'. For anything else, it remains 'CLEAR'. What color is the potion?


color = float(input("Enter Temprature"))

if color<0.0:
    print("Blue")
elif color>100.0:
    print("Red")
elif color==50.0:
    print("Purple")
else:
    print("Clear")
