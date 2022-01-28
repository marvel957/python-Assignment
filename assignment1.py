#Write a program that prints the first 100 members of the sequence 2 , -3 , 4 , -5 , 6
for x in range(2,101):
    if(x%2 == 0):
        print (x)
    else:
        print((x * -1))
