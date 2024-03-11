from secret_santa.app_manager import AppManager


MAIN_PARTY = "Christmas 2023"

app_manager = AppManager()

user_1 = app_manager.create_user(
    email="user1@mail.com",
    name="some-user",
    password="super-secret"
)


christmas_party_manager = AppManager.create_event(name=MAIN_PARTY)

mic = christmas_party_manager.add_participant("mic")
ania = christmas_party_manager.add_participant("Ania")
mama = christmas_party_manager.add_participant("Mama")
tata = christmas_party_manager.add_participant("Tata")
asia = christmas_party_manager.add_participant("Asia")

christmas_party_manager.assign_user(user_1, mama)

christmas_party_manager.draw_name_for(mama)
print(mama)
