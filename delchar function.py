def delchar(s,c): 
    if (len(c)==1):
        for i in range(len(s)):
            if c is not s[i]:
                print(s[i],end="")
            else:
                continue
string=input("enter the string= ")
char=input("enter a character to be reamoved= ")
print("string after the character is reamoved= ") 
delchar(string,char)
