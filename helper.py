from faker import Faker

faker = Faker()

def generate_registration_data():
    name = faker.name()
    surname = faker.surname()
    address = faker.adress()
    telephone = faker.telephone()


    return name, surname, address, telephone