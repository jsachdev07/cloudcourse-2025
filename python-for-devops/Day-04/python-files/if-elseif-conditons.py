import sys

type=sys.argv[1]

if type=="t2.micro":
    print("$2 will be charged")
elif type=="t2.medium":
    print("$4 willbe charged")
elif type=="t2.xlarge":
    print("$8 willbe charged")
else:
    print("kindly input correct machine type")