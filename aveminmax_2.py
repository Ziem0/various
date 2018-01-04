#!/usr/bin/python3

#4 version 2.0
numbers4=[-5,23,0,"dupa",-9,12,99,["streeng",-55],None,105,-43]
i=0 #iteration
minimum=0
maximum=0
global_sum=0
counter=0
while (i<len(numbers4)):
    if (type(numbers4[i])==int):
        counter+=1
        global_sum+=numbers4[i]
        if(numbers4[i]<minimum):
            minimum=numbers4[i]
        if(numbers4[i]>maximum):
            maximum=numbers4[i]

    if (type(numbers4[i])==list): #functions not allowed in this week
        j=0
        while (j<len(numbers4[i])):
            if (type(numbers4[i][j])==int):
                counter+=1
                global_sum+=numbers4[i][j]
                if(numbers4[i][j]<minimum):
                    minimum=numbers4[i][j]
                if(numbers4[i][j]>maximum):
                    maximum=numbers4[i][j]
            j+=1

    i+=1

print("min:",minimum,"max:",maximum,"avg:", global_sum/counter)
