def inversions(sequence: list) -> int:
    count = 0
    for i in range(len(sequence) - 1):
        for j in range(i + 1, len(sequence)):
            if sequence[i] > sequence[j]:
                count += 1
    return count


sequence = [4, 3, 2, 1]
print(inversions(sequence))
