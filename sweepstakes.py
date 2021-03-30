import random


class SweepStakes:
    def __init__(self):
        pass

    def contestants(self):
        contestants = [
            {
                'id': 123,
                'first_name': 'Troy',
                'last_name': 'Athens'
            },
            {
                'id': 321,
                'first_name': 'Jon',
                'last_name': 'Smith'
            },
            {
                'id': 543,
                'first_name': 'Demetrice',
                'last_name': 'Williams'
            },
            {
                'id': 789,
                'first_name': 'Jane',
                'last_name': 'Dough'
            },
            {
                'id': 987,
                'first_name': 'That',
                'last_name': 'One-Guy'
            }

        ]
        return contestants

    def choose_winner(self):
        rand_int = random.randint(0, len(march_madness.contestants()) - 1)
        winner = march_madness.contestants()[rand_int]
        print(f'Congrats {winner["first_name"]} {winner["last_name"]} you won!!!')


march_madness = SweepStakes()
march_madness.choose_winner()
