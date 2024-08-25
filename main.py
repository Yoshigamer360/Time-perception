while True:
    print('A) See how a time period at your age feels for another age. B) See how a time period for another age feels for your age')
    question = input('Select A or B: ').lower()
    print('\n' * 3)
    
    if question == 'a':
        print('As a __ year old, I feel __ weeks/months/years as long as a __ year old feels __ weeks/months/years')
        print('Fill in the blanks\n')

        timemeasurement = ''
        currentAge = int(input('Your current age: '))
        currentTimeCount = int(input('How many weeks, months or years (just the number): '))
        timemeasurement = input('A) Weeks, B) Months, C) Years: ').lower()
        previousAge = int(input('What age are you comparing yours to: '))
        print()

        if timemeasurement == 'a':
            fractionOfLife = 1 / (currentAge * 52 / currentTimeCount)
            previousTimeCount = previousAge * 52 * fractionOfLife
            print(f'As a {currentAge} year old, I feel {currentTimeCount} weeks as long as a {previousAge} year old feels {previousTimeCount} weeks')
        elif timemeasurement == 'b':
            fractionOfLife = 1 / (currentAge * 12 / currentTimeCount)
            previousTimeCount = previousAge * 12 * fractionOfLife
            print(f'As a {currentAge} year old, I feel {currentTimeCount} months as long as a {previousAge} year old feels {previousTimeCount} months')
        elif timemeasurement == 'c':
            fractionOfLife = 1 / (currentAge / currentTimeCount)
            previousTimeCount = previousAge * fractionOfLife
            print(f'As a {currentAge} year old, I feel {currentTimeCount} years as long as a {previousAge} year old feels {previousTimeCount} years')
        else:
            print('You made an error! When it asks you "A) Weeks, B) Months, C) Years:" enter the letter a or b or c')

    else:
        print('For a __ years old, __ weeks/months/years feels as long as __ weeks/months/years for me as a __ year old')
        print('Fill in the blanks\n')

        timemeasurement = ''
        previousAge = int(input('When I was __ years old: '))
        previousTimeCount = int(input('__ weeks/months/years: '))
        timemeasurement = input('A) Weeks, B) Months, C) Years: ').lower()
        currentAge = int(input('Your current age: '))
        print()

        if timemeasurement == 'a':
            fractionOfLife = 1 / (previousAge * 52 / previousTimeCount)
            currentTimeCount = currentAge * 52 * fractionOfLife
            print(f'For a {previousAge} years old, {previousTimeCount} weeks feels as long as {currentTimeCount} weeks for me as a {currentAge} year old')
        elif timemeasurement == 'b':
            fractionOfLife = 1 / (previousAge * 12 / previousTimeCount)
            currentTimeCount = currentAge * 12 * fractionOfLife
            print(f'For a {previousAge} years old, {previousTimeCount} months feels as long as {currentTimeCount} months for me as a {currentAge} year old')
        elif timemeasurement == 'c':
            fractionOfLife = 1 / (previousAge / previousTimeCount)
            currentTimeCount = currentAge * fractionOfLife
            print(f'For a {previousAge} years old, {previousTimeCount} years feels as long as {currentTimeCount} years for me as a {currentAge} year old')
        else:
            print('You made an error! When it asks you "A) Weeks, B) Months, C) Years:" enter the letter a or b or c')

    print('\n' * 5)
