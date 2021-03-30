# 1

months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December')
month_of_PI_day = 'March'

for month in months:
    if month_of_PI_day == month:
        print(f'PI day is in {month}')

# 2

locations_of_party = ['My House', 'Arcade', 'Restaurant', 'The Park', 'Water Park']
locations_of_party.append('Escape Room')
locations_of_party.append('Sports Game')
locations_of_party.append('Party Boat')
for location in locations_of_party:
    print(f'B-Day Party location: {location}')

# 3

family_list = [
    {
        'first_name': 'Leah',
        'last_name': 'Williams',
        'Relationship': 'Mother'
    },
    {
        'first_name': 'Carolina',
        'last_name': 'Williams',
        'Relationship': 'Spouse'
    },
    {
        'first_name': 'Makai',
        'last_name': 'Williams',
        'Relationship': 'Child'
    }
]

print(family_list[1])
