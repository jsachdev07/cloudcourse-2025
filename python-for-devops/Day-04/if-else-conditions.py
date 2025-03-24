import sys
type=sys.argv[1]
if type=="t2.micro":
    print("instance will be created, $2 will be charged")
else:
    print("instance will not be created, you are not eligible")