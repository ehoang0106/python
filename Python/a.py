a = input("a = ")
b = input("b = ")
c = input("c = ")
def maxi():
if a>b and a >c:
	a = maxi
elif b>a and b>c:
	b = maxi
elif c>a and c>b:
	c = maxi;	


print("max: ",maxi)