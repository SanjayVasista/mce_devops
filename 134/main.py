from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide

def main():
    print("Simple Calculator Program")
    
    a = int(input("Enter a number"))
    b = int(input("Enter another number"))
    
    add(a, b) #This gives addition
    subtract(a, b) #This gives the subratction
    multiply(a, b) #This gives multiplication
    divide(a, b) #This gives dividion

if __name__ == "__main__":
    main()
