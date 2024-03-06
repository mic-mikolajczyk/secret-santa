
import datetime
import random

from secret_santa.models.models import Event, Player


class EventManager:

    def __init__(self, event: Event) -> None:
        self.event = event

    def set_event_date(self, day, month, year):
        date = datetime.date(day=day, month=month, year=year)
        self.event.date = date

    def add_participant(self, name: str):
        new_player = Player(name=name)
        self.event.participants.append(new_player)
        self.event.drawing_bucket.append(new_player)
        return new_player

    def draw_name_for(self, player: Player):
        if player.drawn_name is None:
            remaining_names = [p for p in self.event.drawing_bucket if p != player]
            participants_left = [p for p in self.event.participants if p.drawn_name is None]
            if len(remaining_names) == 2:
                only_choice = [n for n in remaining_names if n in participants_left]
                # In case of 2 only choices, doesn't matter which to pick
                player.drawn_name = only_choice[0] if only_choice else random.choice(remaining_names)
            else:
                player.drawn_name = random.choice(remaining_names)
            self.event.drawing_bucket.remove(player.drawn_name)

    def reset_draw_for(self, player: Player):
        if player.drawn_name is not None:
            self.event.drawing_bucket.append(player.drawn_name)
            player.drawn_name = None
