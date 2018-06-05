def quick_sort(arr):
    if len(arr) < 2:
        return arr
    flag = arr[0]
    less_flag = [i for i in arr[1:] if i <= flag]
    greater_flag = [i for i in arr[1:] if i > flag]
    return quick_sort(less_flag) + [flag] + quick_sort(greater_flag)

if __name__ == "__main__":
    arr = [3, 5, 2, 1, 8, 9, 15]
    print quick_sort(arr)