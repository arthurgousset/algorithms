# Sort list using merge sort recursively
def mergesort_recursive(input_list: list) -> list:
    if len(input_list) == 1:
        return input_list
    else:
        left = mergesort_recursive(input_list[:len(input_list)//2])
        right = mergesort_recursive(input_list[len(input_list)//2:])
        return merge_lists(left, right)


def merge_lists(left: list, right: list) -> list:
    result = []

    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if left:
        result.extend(left)
    elif right:
        result.extend(right)

    return result


if __name__ == "__main__":
    unsorted = list([4, 3, 2, 1, 5, 5, 6])
    print(mergesort_recursive(unsorted))