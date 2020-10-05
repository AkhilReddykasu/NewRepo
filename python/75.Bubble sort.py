# bubble sort


def sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp


num = [8, 924, 82, 6, 4, 7]
sort(num)
print(num)
