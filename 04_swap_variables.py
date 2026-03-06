# swap two variable   using third variable
X = 13 
y = 12

temp = 13
print("Now temp variable is :", temp)
x = y 
print("the value of x is", x)

y = temp
print("the value of y is  : ", y)



#without using  third variable


x = 13
y = 12

x , y = y , x

print("The value of x is:", x)
print("The value of y is:", y)

