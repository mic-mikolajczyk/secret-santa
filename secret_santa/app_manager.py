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
        hashed_password = self._compile_password(password)

        for user in DB["users"]:
            if user.email == email:
                raise ValueError("User already exists")

        new_user = User(
            email=email,
            password=hashed_password,
            uuid=uuid.uuid4(),
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

    def _compile_password(self, password: str):
        ...

    def list_users():
        ...

    def login(self, email: str, password: str):
        for user in DB["users"]:
            if user.email == email:
                if user.password == self._compile_password(password):
                    access_token = secrets.token_hex
                    DB["tokens"][access_token] = user.uuid
                    return access_token
                else:
                    raise ValueError("Wrong password")
        else:
            raise ValueError("User doesn't exists")
