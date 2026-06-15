#Number classifier program
num = int(input("Give a number:"))
if(num == 0):
    print("The number is zero (neutral number)")
elif(num < 0):
    if(num%2==0):
        print("Negative and even number")
    else:
        print("Negative and odd number")
elif(num > 0):
    if(num%2!=0):
        print("Positive and odd number")
    else:
        print("Positive and even number")

#Letter grade calculator
mark=int(input("Enter your score: "))
if(mark > 100 or mark < 0):
    print("Invalid mark, enter score within 1-100")

if(mark <= 100 and mark >= 90):
    print("A Grade")
elif(mark < 90 and mark >= 80):
    print("B Grade")
elif(mark < 80 and mark >= 65):
    print("C Grade")
elif(mark < 65 and mark >= 50):
    print("D Grade")
elif(mark <50 and mark >= 0):
    print("F Grade")

#Login check program
stored_Username = "Kiran"
stored_password = "kiran21"

username = input("Enter username: ")
password = input("Enter password: ")

if(username == stored_Username and password == stored_password):
    print(f"Authentication verified, welcome {username}.")
else:
    print("Username/Password is wrong, try again!!")

#Largest of three numbers finder
nums = []
for i in range(3):
    num = input("Enter a number: ")
    try:
        num = int(num)
        nums.append(num)
    except ValueError:
        try:
            num = float(num)
            nums.append(num)
        except ValueError:
            print("Input is not a number")


result = max(nums)
print("The max num is ",result)





