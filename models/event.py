
from dataclasses import dataclass, field
import datetime
import random

from models.player import Player


@dataclass
class Event:
    name: str
    event_id: str | None = None
    participants: list[Player] = field(default_factory=list)
    drawing_bucket: list[Player] = field(default_factory=list)
    date: datetime = None
    target_gift_price: float | None = None

    def set_event_date(self, day, month, year):
        date = datetime.date(day=day, month=month, year=year)
        self.date = date

    def add_participant(self, name: str):
        new_player = Player(name)
        self.participants.append(new_player)
        self.drawing_bucket.append(new_player)
        return new_player

    def draw_name_for(self, player: Player):
        # More complex problem
        # What if last drawing person can draw only himself?

        if player.drawn_name is None:
            draw_choice = random.choice(self.drawing_bucket)

            if draw_choice == player:
                try:
                    self.draw_name_for(player)
                except RecursionError:  # In this case there is only mayself to draw
                    print("Nobody else to draw but yourself")
                    self.drawing_bucket.remove(draw_choice)
                    player.drawn_name = draw_choice
            else:
                self.drawing_bucket.remove(draw_choice)
                player.drawn_name = draw_choice
        else:
            print("Already made a draw")
