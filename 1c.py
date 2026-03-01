def keep_positives(S):
    if len(S) == 0:
        return 0
    else:
        result = []
        for x in S:
            if x > 0:
                result.append(x)
        return result
    
def main():
    S = [-2, -1, 0, 1, 2]
    print(keep_positives(S))

main()