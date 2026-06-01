from faker import Faker

from nexus_qe.data.models import User

fake = Faker()


class UserFactory:
    """Creates test users."""

    @staticmethod
    def build() -> User:
        return User(
            username=fake.user_name(),
            password=fake.password(),
        )