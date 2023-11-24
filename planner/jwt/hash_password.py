from passlib.context import CryptContext

pwd_context = CryptContext(
    deprecated="auto",
    schemes=[
        "bcrypt",
    ],
)


class HashPassword:
    def hash_password(self, password):
        return pwd_context.hash(password)

    def confirm_password(self, plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)
