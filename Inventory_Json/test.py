import json


def new_acc(wood, apple, corn, tomato, corn_seed, tomato_seed, filename='inventory.json'):
    new_data = {"Wood": wood, "Apple": apple, "Corn": corn, "Tomato": tomato, "Corn_seed": corn_seed, "Tomato_seed": tomato_seed}
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data["inventory"][0] = new_data
        file.seek(0)
        json.dump(file_data, file, indent=4)


with open('inventory.json', 'r') as file:
    file_data = json.load(file)['inventory'][0]
    print(file_data)
