class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all_pets = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet type. Allowed types: {', '.join(self.PET_TYPES)}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.__class__.all_pets.append(self)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all_pets if isinstance(pet, Pet) and pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet type. Expected type: Pet.")
        pet.owner = self

    def get_sorted_pets(self):
        sorted_pets = sorted([pet for pet in self.pets() if isinstance(pet, Pet)], key=lambda x: x.name)
        return sorted_pets
