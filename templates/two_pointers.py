# pointers from two ends
def pointers_from_two_ends(arr):
    left, right = 0, len(arr)-1
    while left < right:
        if condition_left():
            left += 1
        if condition_right():
            right -= 1
        do_something()


# sliding window
def sliding_window(arr):
    start, end = 0, 0
    # outer loop to move end index
    while end < len(arr):
        end += 1
        # start index only increase when condition
        while condition():
            do_something_before() # before moving start
            start += 1
        do_something_after() # after moving both pointers


# fast and slow pointers
def fast_slow_pointers(arr):
    slow = 0
    for fast in range(len(arr)):
        # only move slow pointer when condition
        if condition_slow():
            slow += 1
        do_something()


# helpers
def condition_left():
    pass

def condition_right():
    pass

def do_something():
    pass

def condition():
    pass

def do_something_before():
    pass

def do_something_after():
    pass

def condition_slow():
    pass