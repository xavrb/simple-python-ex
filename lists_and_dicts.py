def run():
	my_list = [1, "Hello", True, 4.5]
	my_dict = {"firstname":"Facundo", "lastname":"García"}
	# Definitions
	super_list = [
		{"firstname":"Facundo", "lastname":"García"},
		{"firstname":"Facundo1", "lastname":"García2"},
		{"firstname":"Facundo2", "lastname":"García3"},
		{"firstname":"Facundo3", "lastname":"García4"},
		{"firstname":"Facundo4", "lastname":"García5"},
		{"firstname":"Facundo5", "lastname":"García6"},
		{"firstname":"Facundo6", "lastname":"García7"},

	]
	super_dict = {
		"natural_nums": [1,2,3,4,5],
		"integer_nums": [-1,-2,0,1,2],
		"floating_nums": [1.1, 4.5, 6.43]
	}
	print("Iterating over the dictionary of lists.")

	for key, value in super_dict.items(): # printing the dictionary of lists
		print(f"{key} - {value}")

	print("Iterationg over the list of dictionaries.")

	for x in super_list:
		print(f" First name:{x['firstname']} - {x['lastname']}")


if __name__ == '__main__':
	run()
