def subsets_without_duplicates(nums):
    subsets, cur_set = [],[]
    helper(0, nums, cur_set, subsets)
    return subsets

def helper(i, nums, cur_set, subsets):
    if i >= len(nums):
        subsets.append(cur_set.copy())
        return
    
    cur_set.append(nums[i])
    helper(i+1, nums, cur_set, subsets)
    cur_set.pop()

    helper(i+1, nums, cur_set, subsets)

nums = [1,2,3]
print(subsets_without_duplicates(nums))