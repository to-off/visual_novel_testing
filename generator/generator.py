
from faker import Faker

from data.user import Person

faker_en = Faker('En')


def generated_person():
    return Person(
    username = faker_en.first_name(),
    password1 = faker_en.password(),
    #password2 = faker_en.password()
    email = faker_en.email()
    )
