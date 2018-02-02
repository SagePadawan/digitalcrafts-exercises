ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}
print (ramit.get('email'))
print (ramit.get('interests'))
print (ramit.get('friends'[1]))
ramit_friends = ramit.get('friends')
print(ramit_friends[0].get('interests'))
second_interest = (ramit_friends[1].get('interests'))
print(second_interest[1])