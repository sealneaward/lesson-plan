names = [
    'Hyo Galyon',
    'Asuncion Walkup',
    'Herminia Beaton',
    'Chrissy Keesling',
    'Shanti Delsignore',
    'Eugena Sheller',
    'Karyn Quesinberry',
    'Laura Haug',
    'Concetta Rives',
    'Raguel Christina',
    'Roselia Weinstock',
    'Sharita Cadiz',
    'Maisie Duprey',
    'Virgil Cales',
    'Maida Roysden',
    'Norene Rentschler',
    'Ronald Baney',
    'Theo Mckillip',
    'Lauralee Barrio',
    'Verda Trybus'
]

# find all indexes of names that start  with letter 'R'
indexes_of_first = []
for i, name in enumerate(names):
    if name[0] == 'R':
        indexes_of_first.append(i)
# find all indexes of names that end with letter 'r'
indexes_of_last = []
for i, name in enumerate(names):
    if name[-1] == 'r':
        indexes_of_last.append(i)
