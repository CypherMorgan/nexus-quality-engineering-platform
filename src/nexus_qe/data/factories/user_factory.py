from faker import Faker

from nexus_qe.data.models.user import User

faker = Faker()


class UserFactory:

    @staticmethod
    def build() -> User:
        return User(
            username=faker.user_name(),
            password=faker.password(),
        )

    @staticmethod
    def demo_user() -> User:
        return User(
            username="demo",
            password="password",
        )