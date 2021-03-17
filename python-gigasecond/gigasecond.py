from datetime import  timedelta

def add_gigasecond(your_birthday):
    delta = timedelta(
        seconds=10**9
    )
    your_gigasecond = your_birthday + delta
    return your_gigasecond