from secret_santa.event_manager import EventManager
from secret_santa.models.models import Event, User

MAIN_PARTY = "Christmas 2023"

christmas_party = Event(name=MAIN_PARTY)
event_manager = EventManager(christmas_party)


event_manager.assign_user_

mic = event_manager.add_participant("mic")
ania = event_manager.add_participant("Ania")
mama = event_manager.add_participant("Mama")
tata = event_manager.add_participant("Tata")
asia = event_manager.add_participant("Asia")

event_manager.draw_name_for(mama)
print(mama)
