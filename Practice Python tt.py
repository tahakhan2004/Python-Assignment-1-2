# RECEIPT TOTAL WITH AVERAGE
#x = 0
#s = 0
#amt = 0
#avg = 0
#while amt >= 0:
#    amt = float(input("Enter amount: "))
#    if amt > 0:
#        s=s+amt
#        x = x+1
#       avg = s/x
#print("Total amount: ",s, "Total Average: ", avg)


#Recipt total
#y=0
#x = 0
#amtt = 0
#while amtt >= 0:
#    amtt = float(input("Enter Amount: "))
#    if amtt > 0:
#        x = x + amtt
#        y = y+1
#print("Total: %0.f" % x)

#Q1
# ob = float(input("Enter obtained Marks: "))
# mb = float(input("Enter maximum marks: "))
# print("Percentage: %0.2f" %(ob/mb*100),"%")

#Q2
#rad = float(input("Enter radius: "))
#cir = 2 * 3.142 * rad
#area = 3.142 * (rad ** 2)
#print("Area: ", area, "Circumference: ", cir)

#Q3
#op = float(input("Enter original pirce: "))
#dp = float(input("Enter Discount percent: "))
#tp = op - (op * dp / 100)
#print("Total Price: ", tp)

#Q4
#dp = float(input("Enter dicounted pirce: "))
#dpp = float(input("Enter Discount percent: "))
#tp = dp / (100 - dpp) * 100
#a=dp/tp
#print("Total Price: ", tp)


#a=0
#a=float((input))
#while a>0:

#Q5
#volt = float(input("Enter volts"))
#amp = float(input("Enter ampere"))
#power = volt * amp
#print("POWER: ", power)

#Q6
#a = float(input("length of side 1: "))
#b = float(input("length of side 2: "))
#h = float(input("height: "))
#area = h * (a+b) / 2
#print("Area: ", area)

#Q7
#integer = float(input("Enter number: "))  
#if integer >=0:
#    if integer / 2 == 1:
#        print("Even Number")
#    else:
#        print("odd number")
        
#Q8
#import math
#a=float(input("Enter length of side1: "))
#b=float(input("Enter length of side2: "))        
#c=float(input("Enter length of side3: "))        
#s=(a+b+c)/2
#d=math.sqrt((s*(s-a)*(s-b)*(s-c)))       
#print(d)        


#Assi 2
#Q1
#i=0
#for i in range(1500, 2700):
#    if i % 7 ==0 and i % 5 ==0:
#        print(i)

#Q2
n = int(input("Enter number: "))
for i in range(1,n):
    n=n*i   
print(n)    
    
#Q3
#lis = [1452,11.23,"1+2j", True, 'w3resource', (0,-1), [5,12], {"class":'V',"section":'A'}]
#for i in lis:
#    print(i," Type: ",type(i))

#Q4
#i = 0
#for i in range(100,400):
#    if i%2==0:
#        print(i, end = ", ")


#Q5
#a=int(input("Enter num: "))
#for i in range(1, 200):
#    if a % i == 0:
#       print(i)
    
#Q6
#a=int(input("Enter num 1: "))
#b=int(input("Enter num 2: "))

#for i in range(1, min(a,b)+1):
#    if a % i == b % i == 0:
#       print(i)
   

#Q7 not really complete
a=int(input("Enter num 1: "))
b=int(input("Enter num 2: "))

for i in range(1, min(a,b)+1):
    if a % i == b % i == 0:
       c = i
print(c) 

    

