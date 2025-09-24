# A goblin demands a toll. If a traveler has more than 50 silver OR more than 5 gold, they pay the 'RICH TAX'. If they have less than 10 silver AND 0 gold, they are 'TOO POOR' and pass free. Everyone else pays the 'NORMAL TOLL'. What is the traveler's fate?

gold=int(input("Enter the gold coins number:"))
silver=int(input("Enter the silver coins numbers:"))

if gold>5 or silver>50:
    print("Rich taxs")

elif silver<10 or gold==0 :
    print("Too Poor")

else:
    print("normal toll")
    