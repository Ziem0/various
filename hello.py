#!/usr/bin/env python3

import sys

def main():

   if len(sys.argv) == 2:
       name = sys.argv[1]
   elif len(sys.argv) == 3:
       name = sys.argv[len(sys.argv)-2] + " " + sys.argv[len(sys.argv)-1]
   elif len(sys.argv) == 4:
       name = name = sys.argv[len(sys.argv)-3] + " " + sys.argv[len(sys.argv)-2] + " " + sys.argv[len(sys.argv)-1]
   elif len(sys.argv) == 5:
       name = name = sys.argv[len(sys.argv)-4] + " " + sys.argv[len(sys.argv)-3] + " " + sys.argv[len(sys.argv)-2]+ " " + sys.argv[len(sys.argv)-1]
   else:
    name = "World"
   print ("Hello",name,"!")

if __name__ == "__main__":
 main()
