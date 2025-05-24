class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # The iterator object itself

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # End iteration
        else:
            value = self.current
            self.current -= 1
            return value

# Create an instance
countdown = Countdown(5)

# Use in a for-loop
for number in countdown:
    print(number)
