msg = "enter a number betwee 1 and 1000: "
num = int(input(msg))
for i in range(1000000) :
    if num >5 or num <1:
        num = int(input(msg))
while num>5 or num < 1:
    num= int(input(msg))
    print("done")