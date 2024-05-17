def nearest_number(first, target):
    sort = sorted(first, key=lambda x: abs(x - target))
    return target, sort

n1 = nearest_number(first=[312, 996, 31, 1991], target=1000)
n2 = nearest_number(first=[5, 20, 18, 103, 4], target=27)
print(f'сортировка 1: {n1}\n'
      f'сортировка 2: {n2}\n')

# def element(iterable):
# while True:

numbers = [i for i in range(1, 11)]
print(f'список цифр: {numbers}')

#filter
delenie_na_tri = last(filter(lambda x: x % 3 == 0, numbers ))
print(f'делят на 3: {delenie_na_tri}')

# map
cube = list(map(lambda x: x***3, numbers))
print(f'числа в кубе: {cube}')

numbers = [i for i in range(1, 11)]
print(f'список цифр: {numbers}')

# Filter
delenie_na_tri = list(filter(lambda x: x % 3 == 0, numbers))[-1]
print(f'делятся на 3: {delenie_na_tri}')

# Map
cube = list(map(lambda x: x**3, numbers))
print(f'числа в кубе: {cube}')

