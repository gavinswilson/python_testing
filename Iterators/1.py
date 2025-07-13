class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        """
        The __iter__ method makes this class an iterable.
        It should return an iterator object.
        """
        return self

    def __next__(self):
        """
        The __next__ method defines the iteration behavior.
        It should return the next item in the sequence or raise StopIteration.
        """
        if self.current < self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration


# Example usage of the custom iterator
if __name__ == "__main__":
    my_range = MyRange(1, 5)  # Create an instance of MyRange

    # Iterating over the custom iterator using a for loop
    for number in my_range:
        print(number)  # Output: 1, 2, 3, 4

# Using the built-in range function
    # The built-in range function is an iterable that generates numbers in a specified range.
    r = range(2,10,2)

    itr = iter(r)
    print(next(itr))  # Output: 0

    print(next(itr))  # Output: 1

    p = range(1, 10, 2)
    itr2 = iter(p)
    while True:
        try:
            print(next(itr))  # Output: 1, 3, 5, 7, 9
        except StopIteration:
            break
