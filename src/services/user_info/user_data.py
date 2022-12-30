import random
from faker import Faker

from src.services.logs.logger import Logger

country_list = ['es', 'fr']


class UserData:
    def __generate_random_phone(self, max_len):
        num = ""
        while len(num) < max_len:
            num = num + str(random.randint(0, 9))
        return num

    def __create_sp_phone(self):
        phone = f'+346{self.__generate_random_phone(8)}'
        Logger(f'user_phone: {phone}').substep_passed()
        return phone

    def __create_fr_phone(self):
        pre_num = str(random.randint(6, 7))
        if pre_num == "7":
            num = str(random.randint(3, 9)) + self.__generate_random_phone(7)
            phone = f'+33{pre_num}{num}'
            Logger(f'user_phone: {phone}').substep_passed()
            return phone
        if pre_num == "6":
            num = self.__generate_random_phone(8)
            phone = f'+33{pre_num}{num}'
            Logger(f'user_phone: {phone}').substep_passed()
            return phone

    def random_password(self):
        """Generates a random password.

        :return: random password
        """
        num = ""
        while len(num) < 4:
            num = num + str(random.randint(0, 9))
        return num

    def random_country(self):
        """Generates a random country.

        :return: random country from allowed list
        """
        random_country_index = random.randint(0, len(country_list) - 1)
        country = country_list[random_country_index]
        return country

    def random_phone(self, user_country):
        """Generates a random phone number using the selected country from user.

        :param user_country: user country id.
        :return: user phone number.
        """
        l_user_country = str(user_country).lower()
        if l_user_country in country_list:
            if l_user_country == 'es':
                return self.__create_sp_phone()
            if l_user_country == 'fr':
                return self.__create_fr_phone()
        else:
            Logger(f'no phone has been generated').substep_failed()
            return None

    def random_name(self):
        """Generates a random first name.

        :return: user random name.
        """
        faker = Faker()
        return f"{faker.first_name()}{str(random.randint(0, 999))}"

    def random_last_name(self):
        """Generates a random last name.

        :return: user random last name.
        """
        faker = Faker()
        return f"{faker.last_name()}{str(random.randint(0, 999))}"

    def random_address(self):
        """Generates a random address.

        :return: user random address.
        """
        faker = Faker()
        return faker.address()

    def random_city(self):
        """Generates a random city.

        :return: user random city.
        """
        faker = Faker()
        return faker.city()

    def random_valid_birth_date(self):
        """Generates a random valid birthdate.

        :return: user random birthdate.
        """
        day = random.randint(1, 28)
        month = random.randint(1, 12)
        year = random.randint(1960, 2003)
        return f"{year}-{month}-{day}"
