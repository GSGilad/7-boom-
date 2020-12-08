set_number = int(input("Set a number : "))
for boom in range(1, set_number+1):
    if boom % 7 == 0 :
        print("boom")
        continue
    elif '7' in str(boom) :
        print("boom")
        continue
    print(boom)

