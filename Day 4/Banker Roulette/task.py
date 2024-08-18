import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(random.choice(friends))
random_friend_number = random.randint(1,len(friends))
randon_friend = friends[random_friend_number-1]
print(randon_friend)