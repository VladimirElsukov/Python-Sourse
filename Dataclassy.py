from dataclasses import dataclass, field
from time import sleep
@dataclass
class User:
    user_id: int
    first_name: str
    last_name: str
    age: int
    email: str
    full_name: str = field(init=False, repr=False)
    job: str = "Data Scientist"


    def __post_init__(self):
        self.full_name = f"Полное имя: {self.first_name} {self.last_name} {self.job}"


def get_user_info(user: User) -> str:
    return f"Пользователь: {user.first_name} {user.last_name}\n"\
           f"Возраст: {user.age}\n"\
           f"Почта: {user.job}\n"\
           f"Почта: {user.email}\n"

def wait_and_print_user_info(user: User) -> None:
    info = get_user_info(user)
    lines = info.split('\n')
    for line in lines:
        print(line)
        sleep(0.5)


# user1 = User(1, 'Vasiliy', 'Serebryakov', 46, 'vasiliypupkin@yandex.ru')
# print(get_user_info(user1))
# print(user1)
# print(user1.full_name, user1.age)


if __name__ == "__main__":
    user1 = User(
        user_id=1,
        first_name="Василий",
        last_name="Новиков",
        age=46,
        email="vasiliy.novikov@example.com"
    )
    wait_and_print_user_info(user1)




