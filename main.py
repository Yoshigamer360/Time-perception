print('When I was __ years old, __ weeks/months/years feels as long as __ weeks/months/years for a __ years old')
print('Fill in the blanks\n')

previousAge = int(input('When I was __ years old: '))
previousTimeCount = int(input('__ weeks/months/years: '))
timemeasurement = input('A) Weeks, B) Months, C) Years: ').lower()
currentAge = int(input('Your current age: '))
print()

if timemeasurement == 'a':
    fractionOfLife = 1 / (previousAge * 52 / previousTimeCount)
    currentTimeCount = currentAge * 52 * fractionOfLife
    print(f'When I was {previousAge} years old, {previousTimeCount} weeks feels as long as {currentTimeCount} weeks for a {currentAge} year old')
elif timemeasurement == 'b':
    fractionOfLife = 1 / (previousAge * 12 / previousTimeCount)
    currentTimeCount = currentAge * 12 * fractionOfLife
    print(f'When I was {previousAge} years old, {previousTimeCount} months feels as long as {currentTimeCount} months for a {currentAge} year old')
elif timemeasurement == 'c':
    fractionOfLife = 1 / (previousAge / previousTimeCount)
    currentTimeCount = currentAge * fractionOfLife
    print(f'When I was {previousAge} years old, {previousTimeCount} years feels as long as {currentTimeCount} years for a {currentAge} year old')
