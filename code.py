def display(text):
	print("     " + text)
def display1(text):
	print("          " + text)

def Solve(a, d, n):
	answer = (n + d - a) / d
	
	display("")
	display("Lowest multiple of " + str(n) + " between this range = " + str(a))
	display("Highest multiple of " + str(n) + " between this range = " + str(n))
	display("")
	display("a = " + str(a) + "; d = " + str(d) + "; aₙ = " + str(n))
	display("")
	display("Solving:")
	display1("aₙ = a + (n - 1) d")
	display1(str(n) + " = " + str(a) + " + (n - 1) " + str(d))
	display1(str(n) + " = " + str(a) + " + " + str(d) + "n - " + str(d))
	display1(str(n) + " - " + str(a) + " + " + str(d) + " = " + str(d) + "n")
	display1(str(n - a + d) + " = " + str(d) + "n")
	display1("n = " + str(int(answer)))
	display("")
	display("Answer: " + str(int(answer)))

min_ = int(input("Minimum: "))
max_ = int(input("Maximum: "))
multiple = int(input("Multiple: "))

min_m = None
max_m = None

i = min_
while i <= max_:
	if i % multiple == 0:
		min_m = i
		break
	
	i += 1

j = max_
while j >= min_:
	if j % multiple == 0:
		max_m = j
		break
	
	j -= 1

if min_m == None or max_m == None:
	display("Multiples not found in the given range.")
else:
	Solve(a=min_m, d=multiple, n=max_m)
