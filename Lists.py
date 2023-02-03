bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

names = ['asus', 'lenovo', 'dell']
print(names[1].title())

bicycles = ['cannondale', 'trek', 'specialized', 'redline']
print(bicycles[1])
print(bicycles[-1])

bicycles = ['cannondale', 'trek', 'specialized', 'redline']
message = f"my first bicycles was {bicycles[0].title()}"
print(message)

names = ['eric', 'sam', 'trek', 'cric']
print(names[2])
print(names[0])
print(names[3])

names = ['eric', 'sam', 'trek', 'cric']
message = f"hello, {names[0].title()}"
print(message)

names = ['eric', 'sam', 'trek', 'cric']
message = f"hello, {names[1].title()}"
print(message)

names = ['eric', 'sam', 'trek', 'cric']
message = f"hello, {names[2].title()}"
print(message)

names = ['eric', 'sam', 'trek', 'cric']
message = f"hello, {names[3].title()}"
print(message)

letters = ['A', 'B', 'C', 'D']
letters[1] = 'E'
print(letters)
letters[0] =  'z'
print(letters)

#adding element in list
letters = ['A', 'B', 'C', 'D']
letters.append('x')
print(letters)
letters.append('z')
print(letters)

#inserting element in list
letters = ['A', 'B', 'C', 'D']
letters.insert(0, 'O')
print(letters)

#deleting elements from list
letters = ['A', 'B', 'C', 'D']
del(letters[1])
print(letters)

letters = ['A', 'B', 'C', 'D']
del(letters[3])
del(letters[2])
print(letters)

letters = ['A', 'B', 'C', 'D']
letters.remove('A')
print(letters)

guest = ['van', 'jack', 'hill', 'turner']
name = guest[0].title()
print(f"{name}, please come to dinner.")

guest = ['van', 'jack', 'hill', 'turner']
name = guest[1].title()
print(f"{name}, please come to dinner.")

guest = ['van', 'jack', 'hill', 'turner']
name = guest[2].title()
print(f"{name}, please come to dinner.")

guest = ['van', 'jack', 'hill', 'turner']
name = guest[3].title()
print(f"{name}, please come to dinner.")

guest = ['van', 'jack', 'hill', 'turner']
del(guest[0])
guest.insert(0, 'accurate')
message = 'sorry van cant make for the party'
print(message)
print(guest)

locations = ['dubai', 'thailand', 'england', 'nepal']
print(sorted(locations))

locations = ['dubai', 'thailand', 'england', 'nepal']
print(sorted(locations,reverse = True))

locations = ['dubai', 'thailand', 'england', 'nepal']
print('original order:')
print (locations)

locations = ['dubai', 'thailand', 'england', 'nepal']
print('alphabetical order:')
print(sorted(locations))




