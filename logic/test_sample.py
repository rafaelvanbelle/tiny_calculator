from logic import add_numbers


class TestAnswers:
    def test_answer(self):
        assert add_numbers(3, 4) == 7

    def test_two(self):
        assert add_numbers(-1, -2) == -3
