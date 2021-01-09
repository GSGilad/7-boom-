flag = 0
num = int(input("Enter a number: "))
for boom in range(1, num + 1):
    if boom % 7 == 0:
        print("boom")
        flag += 1
    elif "7" in str(boom):
        print("boom")
        flag += 1
    else:
        print(boom)
print("There were", flag, "boom")