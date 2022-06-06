x = input("Whats your favorite number?")
y = int(input("Whats your age?"))

for i in range(len(x)):
    if x[i]=="1" or x[i]=="2" or [i]=="3" or x[i]=="4" or x[i]=="5" or x[i]=="6" or x[i]=="7" or x[i]=="8" or x[i]=="9" or x[i]=="0":
        x = x[i:len(x)]
        break
print(int(x)* y)

