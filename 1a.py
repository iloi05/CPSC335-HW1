def sum_list(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total

def main():
    list = [1, 2, 3, 4, 5]
    print(sum_list(list))

main()