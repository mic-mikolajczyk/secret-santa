
import datetime
import random

from secret_santa.models.models import Event, Participant


class EventManager:

    def __init__(self, event: Event) -> None:
        self.event = event

    def set_event_date(self, day, month, year):
        date = datetime.date(day=day, month=month, year=year)
        self.event.date = date

    def add_participant(self, name: str):
        new_participant = Participant(name=name)
        self.event.participants.append(new_participant)
        self.event.drawing_bucket.append(new_participant)
        return new_participant

    def draw_name_for(self, participant: Participant):
        if participant.drawn_name is None:
            remaining_names = [p for p in self.event.drawing_bucket if p != participant]
            participants_left = [p for p in self.event.participants if p.drawn_name is None]
            if len(remaining_names) == 2:
                only_choice = [n for n in remaining_names if n in participants_left]
                # In case of 2 only choices, doesn't matter which to pick
                participant.drawn_name = only_choice[0] if only_choice else random.choice(remaining_names)
            else:
                participant.drawn_name = random.choice(remaining_names)
            self.event.drawing_bucket.remove(participant.drawn_name)

    def reset_draw_for(self, participant: Participant):
        if participant.drawn_name is not None:
            self.event.drawing_bucket.append(participant.drawn_name)
            participant.drawn_name = None
