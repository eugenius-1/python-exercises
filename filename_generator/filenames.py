# This program generates filenames which corresponds to all the days in a month for all the months
# in a year given a particular year. The

year = input('Enter the year: ')
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

for days in range(len(months)):
    print('\n')
    print('Month: ', months[days], '\n')
    for day in range(1, 32):
        filename = ''

        days_counter = days + 1
        days_counter = str(days_counter)
        if len(days_counter) == 1:
            days_counter = '0' + days_counter
        day_counter = day
        day_counter = str(day_counter)
        if len(day_counter) == 1:
            day_counter = '0' + day_counter
        filename = filename + f'{year}' + f'{days_counter}' + f'{day_counter}' + '_backup_ptrg.zip'
        if months[days] == 'Feb':
            if int(year) % 4 == 0:
                if day == 30:
                    break
            else:
                if day == 29:
                    break
        if months[days] == 'Apr' or months[days] == 'Jun' or months[days] == 'Sep' or months[days] == 'Nov':
            if day == 31:
                break
        print(f'day{day}: ', filename)