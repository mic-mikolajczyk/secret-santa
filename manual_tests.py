from secret_santa.models.event import Event

MAIN_PARTY = "Christmas 2023"

christmas_party = Event(name=MAIN_PARTY)

mic = christmas_party.add_participant("mic")
ania = christmas_party.add_participant("Ania")
mama = christmas_party.add_participant("Mama")
tata = christmas_party.add_participant("Tata")
asia = christmas_party.add_participant("Asia")


for _ in range(100):
    christmas_party.draw_name_for(mic)
    christmas_party.draw_name_for(ania)
    christmas_party.draw_name_for(mama)
    christmas_party.draw_name_for(tata)
    christmas_party.draw_name_for(asia)

    for participant in christmas_party.participants:
        print(f"DRAWN NAME FOR {participant.name}: {participant.drawn_name.name}")
        assert participant.name != participant.drawn_name.name
    print()

    christmas_party.reset_draw_for(mic)
    christmas_party.reset_draw_for(ania)
    christmas_party.reset_draw_for(mama)
    christmas_party.reset_draw_for(tata)
    christmas_party.reset_draw_for(asia)
