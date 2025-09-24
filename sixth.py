# A royal adviser must categorize a citizen based on their age. If they are under 18, they are a 'MINOR'. If they are 18 to 65 (inclusive), they are an 'ADULT'. However, if their age is exactly 25 and they have a royal decree (true/false value), they are a 'NOBLE'. Anyone over 65 is an 'ELDER'. Determine their title.

age = int(input("Enter Your Age: "))
if age<18:
    print("Your are Miner")
elif age>=18 and age<=65:
    print("Adult")
elif age==25:
    print("True")
elif age>65:
    print("Elder")
