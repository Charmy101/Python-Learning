score = input("Enter Score: ")
score1 = float(score)
if score1 > 1.0 or score1 < 0:
    print("out of range")
elif score1 >= 0.9:
    print("A")
elif score1 >= 0.8:
    print("B")
elif score1 >= 0.7:
    print("C")
elif score1 >= 0.6:
    print("D")
else:
    print("F")
