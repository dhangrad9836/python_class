# Program Explanation
# 1. User must enter the base and exponential value.
# 2. The numbers are passed as arguments to a recursive function to find the power of the number.
# 3. The base condition is given that if the exponential power is equal to 1, the base number is returned.
# 4. If the exponential power isn’t equal to 1, the base number multiplied with the power function
# is called recursively with the arguments as the base and power minus 1.
# 5. The final result is printed.

def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print("Result:",power(base,exp))