def run():
	squares = []
	#non-pythonistic way
	# List with all the squares 1 to 100
	print("Doing the boring way.")
	for i in range(1, 101):
		squares.append(i**2)
	print(squares)
	squares_div3 = []
	# list of  squares of numbers non divisible by 3
	for x in range(1,101):
		if x%3 != 0:
			squares_div3.append(x**2)

	print(squares_div3)

	#pythonistic way
	# comprehension lists
	print("Comprehension lists:")
	sq_cl = [i**2 for i in range(1,101)]
	sql_cl_div3 = [i**2 for i in range (1,101) if i%3 != 0]
	print(f"Square list with comprehension lists: {sq_cl}")
	print(f"Square of numbers that cannot be divided by 3 with comprehension lists: {sql_cl_div3}")


if __name__ == "__main__":
	run()
