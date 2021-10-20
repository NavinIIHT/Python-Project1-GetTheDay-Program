

def count_characters(s):
    if type(s)==type(" "):
        L=[]
        lower=0
        upper=0
        digits=0
        specialchars=0
        for ch in s:
            if ch.islower():
                lower+=1
            elif ch.isupper():
                upper+=1
            elif ch.isdigit():
                digits+=1
            elif ch!=" ":
                specialchars+=1
        L.extend([lower,upper,digits,specialchars])
        return L
    else:
        raise TypeError("Input must be string format")

if __name__=="__main__":
    s=input("Enter a string:")#Karthik Age Is 18 @2021
    L=count_characters(s)
    #L=count_characters(120)#TypeError will be raised
    print(L)
    print("The total no of lower case letters is:",L[0])
    print("The total no of upper case letters is:",L[1])
    print("The total no of digits is:",L[2])
    print("The no of special characters is:",L[3])
