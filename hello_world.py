import sys

if len(sys.argv) > 1:
    name = 'Hello ' + ' '.join(sys.argv[1:]) + '!'
    print (name)
else:
    print ("Hello World !")

#print (type(sys.argv))
