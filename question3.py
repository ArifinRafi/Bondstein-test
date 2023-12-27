def findIndices(nums, target):
    left, right = 0, len(nums)-1

    while left<right:
        sum = nums[left]+nums[right]
        if sum == target:
            return left, right
        elif sum<target:
            left +=1
        else:
            right -=1

        return None

numbers= [1,3,5,7,9,11,13]
target = 14

print(findIndices(numbers, target))
