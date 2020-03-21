def parse_length(length):
    split_length = length.split(":")
    hours = 0
    minutes = 0
    seconds = 0
    if len(split_length) == 3:
        hours = int(split_length[0])
        minutes = int(split_length[1])
        seconds = int(split_length[2])
    elif len(split_length) == 2:
        minutes = int(split_length[0])
        seconds = int(split_length[1])
    elif len(split_length) == 1:
        seconds = int(split_length[0])

    if seconds > 59:
        raise ValueError("Incorrect seconds!")

    if minutes > 59:
        if hours == 0:
            hours += minutes // 60
            minutes %= 60
        else:
            raise ValueError("Incorrect minutes!")

    return (hours,minutes,seconds)