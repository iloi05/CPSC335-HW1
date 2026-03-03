# Name: Ivy Loi
# Assignment: HW 1
# Problem: 1a
# Date: 3/2/26
# Get the sum of a list of numbers
def sum_list(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total

def main():
    list = [1, 2, 3, 4, 5]
    print(sum_list(list))

main()