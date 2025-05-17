from faker import Faker

faker = Faker('ru_RU')

def generate_order_data():
    return {
        'name': faker.name(),
        'surname': faker.surname(),
        'address': faker.address(),
        'metro': faker.random_element([
            'Сокольники', 'Красносельская', 'Чистые пруды',
            'Лубянка', 'Охотный ряд', 'Библиотека им. Ленина'
        ]),
        'telephone': faker.phone_number(),
        'date': faker.date_between(start_date='today', end_date='+30d').strftime('%Y-%m-%d'),
        'period': faker.random_element([
            'сутки', 'двое суток', 'трое суток',
            'четверо суток', 'пятеро суток', 'шестеро суток',
            'семеро суток'
        ]),
        'color': faker.random_element(['black', 'grey']),
        'comment': faker.text(max_nb_chars=100)
    }


#def generate_registration_data():

    #return (
        #faker.first_name(),
        #faker.last_name(),
       # faker.street_address(),
        #faker.phone_number()
   # )