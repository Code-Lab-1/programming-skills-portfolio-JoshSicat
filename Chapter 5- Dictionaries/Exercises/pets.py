# make an empty list to store the pets in.
pets = []

# make individual pets, and store each one in the list. 
pets ={

    'animel type' : 'python',
    'name': 'john ',
    'onwer': 'guido',
    'weight': 43,
    'eats': 'bugs',
}
pets.append(pets)

pet = {

    'animal type': 'chicken',
    'name': 'josh',
    'onwer': 'tiffany',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)

pet = {

    'animal type': 'dog',
    'name': 'miguel',
    'onwer': 'hanzo',
    'weight': 32,
    'eats': 'shoes',
}
pets.append(pet)

#display information about each pet.
for pet in pets:
    print(f"\nhere's what i know about {pet['name'].title()}")
    for key, value in pet.items():
        print("f\t{key}: {value}")
        dict
