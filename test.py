x=int(input("How many numer?\n"))
arr=[]
for i in range(x):
    arr.append(int(input(f"{i+1} number: ")))
print(*arr)
print("Done")
