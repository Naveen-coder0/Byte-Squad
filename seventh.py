# A mystical Gryphon only appears in a leap year. A year is a leap year if it's divisible by 4, BUT NOT if it's divisible by 100, UNLESS it's ALSO divisible by 400. Given a year, will you see a 'GRYPHON SIGHTING' or have a 'QUIET YEAR'?


year=int(input("Enter the year:"))

if year%4==0 and year%100!=0 and year%400==0 :
    print("GRYPHON YEAR")

else:
    print("QUIET YEAR")    