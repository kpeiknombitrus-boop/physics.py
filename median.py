# Function 1: Calculate Sum
def total_sum(numbers):
    return sum(numbers)


# Function 2: Calculate Mean
def average(numbers):
    count = len(numbers)
    return total_sum(numbers) / count


# Function 3: Calculate Median and Mode
def median_mode(numbers):
    data = sorted(numbers)
    size = len(data)

    middle = size // 2

    if size % 2 == 0:
        med = (data[middle - 1] + data[middle]) / 2
    else:
        med = data[middle]

    counts = {x: numbers.count(x) for x in set(numbers)}
    highest = max(counts.values())

    mod = [x for x in counts if counts[x] == highest]

    return med, mod


# Main Program
while True:

    values = input("Enter numbers separated by spaces: ")

    numbers = list(map(float, values.split()))

    print("\nSUM:", total_sum(numbers))
    print("MEAN:", average(numbers))

    med, mod = median_mode(numbers)

    print("MEDIAN:", med)
    print("MODE:", mod)

    choice = input("\nDo you want to continue? (yes/no): ")

    if choice.lower() != "yes":
        print("Program ended.")
        break
