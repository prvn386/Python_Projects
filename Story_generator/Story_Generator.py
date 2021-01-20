import random
when = ['A few years ago','On 1st Jan','Last night','Yesterday','Today']
who = ['A Lion','Peter','A Cat','A Dog','An Elephant']
name = ['Jack','daniel','parker','Stark']
residence = ['Wakanda','Europe','England','India','Atlantic']
went = ['cinema', 'university','seminar', 'school', 'laundry']
happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']
print(random.choice(when)+','+random.choice(who) +' that lived in '+ random.choice(residence) +' went to the ' + random.choice(went) +
      ' along with ' + random.choice(name) +' and ' + random.choice(happened))