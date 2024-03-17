import hashlib
from hmac import compare_digest
import uuid
import secrets
from secret_santa.event_manager import EventManager

from secret_santa.models.models import Event, User

# Fake db for PoC purpose
DB = {
    "users": [],
    "events": [],
    "tokens": {}
}


class AppManager:

    def create_user(self, email: str, password: str, name: str | None = None):
        user_uuid = uuid.uuid4()
        password_hash = self._compile_password(password, user_uuid)

        for user in DB["users"]:
            if user.email == email:
                raise ValueError("User already exists")

        new_user = User(
            email=email,
            password=password_hash,
            uuid=user_uuid,
            name=name,
            events=[]
        )
        DB["users"].append(new_user)
        return new_user

    def delete_user(self):
        ...

    def change_password_for_user(self):
        ...

    def create_event(self, name: str) -> EventManager:
        new_event = Event(
            name=name,
        )
        return EventManager(new_event)

    def _compile_password(self, password: str, salt: str):
        password_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), str(salt).encode(), 100_000)
        return password_hash

    def verify_password(self, p_hash: bytes, password: str, salt: str) -> bool:
        """
        Given a previously-stored salt and hash, and a password provided by a user
        trying to log in, check whether the password is correct.
        """
        return compare_digest(p_hash, self._compile_password(password, salt))

    def list_users():
        ...

    def login(self, email: str, password: str):
        for user in DB["users"]:
            if user.email == email:
                if self.verify_password(user.password, password, user.uuid):
                    access_token = secrets.token_hex
                    DB["tokens"][access_token] = user.uuid
                    return access_token
                else:
                    raise ValueError("Wrong password")
        else:
            raise ValueError("User doesn't exists")

    def list_events(self):
        ...
