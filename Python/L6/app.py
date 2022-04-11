# is_good = False
# money = 1000000
#
# if is_good:
#     down_payment = money * 0.1
# else:
#     down_payment = money * 0.2
# print(f"Down Payment: £{int(down_payment)}")

name = input("Enter a name: ")
if len(name) < 3:
    print("Too Short!")
elif len(name) > 50:
    print("Too Long!")
else:
    print("Name is eligible")