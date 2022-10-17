import time

def countdown(countdown_time):
    while countdown_time:
        mins, secs = divmod(countdown_time,60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        countdown_time -= 1

    print("timer completed")

countdown_time = input('Enter the time in seconds: ')

countdown(int(countdown_time))

