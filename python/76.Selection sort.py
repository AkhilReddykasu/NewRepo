# Selection sort

def sort(nums):
    for i in range(0, len(nums)):
        for j in range(i, 6):
            if nums[i] > nums[j+1]:
                temp = nums[i]
                nums[i] = num[j+1]
                nums[j+1] = temp


num = [8, 6, 7, 3, 10, 64, 2]
sort(num)
print(num)