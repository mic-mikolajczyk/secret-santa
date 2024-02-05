
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
        if player.drawn_name is None:
            remaining_names = [p for p in self.drawing_bucket if p != player]
            if len(remaining_names) == 2:
                only_choice = []
                participants_left = []
                for p in self.participants:
                    if p.drawn_name is None:
                        participants_left.append(p)
                for n in remaining_names:
                    if n in participants_left:
                        only_choice.append(n)
                if only_choice:
                    player.drawn_name = only_choice[0]
                    self.drawing_bucket.remove(player.drawn_name)
                else:
                    player.drawn_name = random.choice(remaining_names)
                    self.drawing_bucket.remove(player.drawn_name)

            elif not remaining_names:
                print("[INFO] No one left but you")
                player.drawn_name = player
            else:
                player.drawn_name = random.choice(remaining_names)
                self.drawing_bucket.remove(player.drawn_name)
        else:
            pass

    def reset_draw_for(self, player: Player):
        self.drawing_bucket.append(player.drawn_name)
        player.drawn_name = None
