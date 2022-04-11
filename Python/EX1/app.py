weight = int(input("Weight: "))
measurement = input("(L)bs or (K)gs: ")
measurement = measurement.lower()
if measurement == "l":
    weight = weight // 2.205
    print(f"Weight in kgs: {weight}")
elif measurement == "k":
    weight = weight * 2.205
    print(f"Weight in lbs: {weight}")
else:
    print("Enter lbs(L) or kgs(K) only")