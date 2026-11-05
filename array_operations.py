class Array:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.length = 0

    def is_full(self):
        return self.length == self.capacity

    def is_empty(self):
        return self.length == 0

    def display(self):
        if self.is_empty():
            print("The array is empty.")
            return
        values = [str(self.items[i]) for i in range(self.length)]
        print(f"Array ({self.length}/{self.capacity}): [" + ", ".join(values) + "]")

    def insert(self, value, position):
        if self.is_full():
            print("Insertion failed: the array is full.")
            return False
        if position < 0 or position > self.length:
            print(f"Insertion failed: position must be between 0 and {self.length}.")
            return False
        for i in range(self.length, position, -1):
            self.items[i] = self.items[i - 1]
        self.items[position] = value
        self.length += 1
        print(f"{value} inserted at position {position}.")
        return True

    def search(self, value):
        for i in range(self.length):
            if self.items[i] == value:
                return i
        return -1

    def delete(self, value):
        if self.is_empty():
            print("Deletion failed: the array is empty.")
            return False
        position = self.search(value)
        if position == -1:
            print(f"Deletion failed: {value} is not in the array.")
            return False
        for i in range(position, self.length - 1):
            self.items[i] = self.items[i + 1]
        self.items[self.length - 1] = None
        self.length -= 1
        print(f"{value} deleted from position {position}.")
        return True


def read_int(prompt, minimum=None, maximum=None):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if minimum is not None and number < minimum:
            print(f"Please enter a number of at least {minimum}.")
        elif maximum is not None and number > maximum:
            print(f"Please enter a number of at most {maximum}.")
        else:
            return number


def create_array():
    capacity = read_int("Enter the size of the array: ", 1)
    array = Array(capacity)
    count = read_int(f"How many values do you want to enter now (0-{capacity})? ", 0, capacity)
    for i in range(count):
        value = read_int(f"Enter value {i + 1}: ")
        array.insert(value, array.length)
    return array


def main():
    print("=== ARRAY OPERATIONS ===")
    array = create_array()
    array.display()

    while True:
        print("\n1. Insert a value")
        print("2. Delete a value")
        print("3. Display the array")
        print("4. Exit")
        choice = read_int("Choose an option (1-4): ", 1, 4)

        if choice == 1:
            value = read_int("Enter the value to insert: ")
            position = read_int(f"Enter the position (0-{array.length}): ")
            array.insert(value, position)
            array.display()
        elif choice == 2:
            value = read_int("Enter the value to delete: ")
            array.delete(value)
            array.display()
        elif choice == 3:
            array.display()
        else:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
