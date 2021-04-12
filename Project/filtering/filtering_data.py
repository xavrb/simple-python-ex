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



    # challenge: implement all filters again but if its implemented previously with hof  now it has to be done using comprehension lists and viceversa.
    print("Challenge: \n")
    # Using hof
    all_python_devs_hof = list(map(lambda worker: worker["name"], list(filter(lambda worker: worker["language"] == "python", DATA))))

 #    [worker["name"] for worker in DATA if worker["language"]== "python"]
    print(all_python_devs_hof)
    all_platzi_workers_hof = list(map(lambda worker: worker["name"], list(filter(lambda worker: worker["organization"] == "Platzi", DATA))))


    #[worker["name"]for worker in DATA if worker["organization"] == "Platzi"]
    print(all_platzi_workers_hof)

    # using filter
    all_adults_cl = [worker["name"] for worker in DATA if worker["age"] >= 18]

    #list(map(lambda adult: adult["name"], list(filter(lambda adult: adult["age"] >= 18, DATA))))
    print(all_adults_cl)

    # using map
    old_people_cl = [worker | {"old":worker["age"]>70} for worker in DATA]


    #list(map(lambda old_adult: old_adult | {"old": old_adult["age"]>70}, DATA))
    print(old_people_cl)




def read_data_bulk(data_set):
    with open(data_set) as file:
        data_list =ast.literal_eval(file.read())
    return data_list
    


if __name__== "__main__":
    run()
