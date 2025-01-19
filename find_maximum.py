def find_maximum(nums: list) -> int:
    max = nums[0]
    for n in nums:
        if n > max:
            max = n
    return max