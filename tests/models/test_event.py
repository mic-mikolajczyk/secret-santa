import pytest
from secret_santa.models.event import Event


class Test:

    @pytest.mark.parametrize('execution_number', range(100))
    def test_draw_name_for(self, execution_number):
        """Test to verify drawing method. Repetition due to the randomness of the function"""
        test_event = Event(name="Test Event")
        test_participant_1 = test_event.add_participant("Name_1")
        test_participant_2 = test_event.add_participant("Name_2")
        test_participant_3 = test_event.add_participant("Name_3")
        test_participant_4 = test_event.add_participant("Name_4")
        test_participant_5 = test_event.add_participant("Name_5")

        test_event.draw_name_for(test_participant_1)
        test_event.draw_name_for(test_participant_2)
        test_event.draw_name_for(test_participant_3)
        test_event.draw_name_for(test_participant_4)
        test_event.draw_name_for(test_participant_5)

        for participant in test_event.participants:
            assert participant.name != participant.drawn_name.name
