for i in range(101):
    if i % 15 == 0:
        print(f"{i}: freezes bugs")
    elif i % 3 == 0:
        print(f"{i}: freeze")
    elif i % 5 == 0:
        print(f"{i}: bugs")
    else:
        print(f"{i}: {i}")