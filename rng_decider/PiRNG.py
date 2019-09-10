import datetime


def get_date():
    today = datetime.date.today()
    return today.day*10000 + today.month*100 + today.year - 2000


if __name__ == "__main__":
    pi_text = open('pi1000000.txt', 'r')

    try:
        pi_mem = open('pi_mem.txt', 'r+')
        stored_date = int(pi_mem.readline())
        instance = int(pi_mem.readline())
        pi_mem.close()
        date = get_date()
        if stored_date == date:
            instance += 1
        else:
            instance = 0

    except (ValueError, FileNotFoundError) as e:
        date = get_date()
        instance = 0

    print(date)
    print(instance)
    print('')
    print('****')

    num = date
    if instance > 0:
        num += (instance + 30)*10000

    if 2 < num <= 1000000:
        pi_text.seek(num)
        digit = pi_text.read(1)
        digit2 = pi_text.read(1)
    else:
        digit = 'go f*ck yourself'
        digit2 = ' buddy'

    print('Your digit is ' + digit + ',' + digit2)
    print('****')

    pi_mem = open('pi_mem.txt', 'w+')
    pi_mem.write(str(date) + '\n' + str(instance))
    pi_mem.close()
	
