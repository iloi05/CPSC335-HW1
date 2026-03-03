# Name: Ivy Loi
# Assignment: HW 1
# Problem: 1c
# Date: 3/2/26

# Keep only the positive numbers in a list
# S is the list
# x represents each element in the list
def keep_positives(list):
    if len(list) == 0:
        return 0
    else:
        result = []
        for x in list:
            if x > 0:
                result.append(x)
        return result
    
def main():
    S = [-2, -1, 0, 1, 2]
    print(keep_positives(S))

main()