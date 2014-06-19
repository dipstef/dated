from datetime import timedelta


def to_seconds(time_delta):
    seconds = time_delta.seconds
    seconds += 24 * 60 * 60 * time_delta.days
    return seconds


def seconds(value):
    return timedelta(seconds=value)