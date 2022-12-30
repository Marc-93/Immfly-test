import faker
fake = faker.Faker()


def get_braze_id():
    return fake.pystr_format(string_format=('?'*22)+':APA91b'+('?'*134),
                             letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_')
