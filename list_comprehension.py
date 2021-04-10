def run():
	squares = []
	#non-pythonic way
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

	#pythonic way
	# comprehension lists
	print("Comprehension lists:")
	sq_cl = [i**2 for i in range(1,101)]
	sql_cl_div3 = [i**2 for i in range (1,101) if i%3 != 0]
	print(f"Square list with comprehension lists: {sq_cl}")
	print(f"Square of numbers that cannot be divided by 3 with comprehension lists: {sql_cl_div3}")




	#HW
	# Print a list using comprehension lists of numbers that can be divided by 4,6,9 range: 1-99999

	hw_list = [i for i in range(1,100000) if (i%4 == 0 and i%6 == 0 and i%9 == 0)]
	print(hw_list)


if __name__ == "__main__":
	run()
