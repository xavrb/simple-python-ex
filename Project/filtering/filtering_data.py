import ast 

def run():
    DATA = read_data_bulk("./data/names_langs.dat")
    
    # Using comprehension lists
    all_python_devs = [worker["name"] for worker in DATA if worker["language"]== "python"]
    print(all_python_devs)
    all_platzi_workers = [worker["name"]for worker in DATA if worker["organization"] == "Platzi"]
    print(all_platzi_workers)
    
    # using filter
    all_adults = list(map(lambda adult: adult["name"], list(filter(lambda adult: adult["age"] >= 18, DATA))))
    print(all_adults)

    # using map
    old_people = list(map(lambda old_adult: old_adult | {"old": old_adult["age"]>70}, DATA))
    print(old_people)


def read_data_bulk(data_set):
    with open(data_set) as file:
        data_list =ast.literal_eval(file.read())
    return data_list
    


if __name__== "__main__":
    run()
