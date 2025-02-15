medical=input("do you have medical cause Y or N")
attend=int (input("enter the attendents of the student"))
if medical=="Y":
    print(" You are allowed")
else:
    if attend>=75:
        print ("you are allowed")
    else:
        print("you are not allowed")
