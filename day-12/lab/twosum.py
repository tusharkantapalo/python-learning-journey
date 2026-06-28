def two_sum(nums, target):
    p1 = 0
    p2 = len(nums) - 1

    while p1 < p2:
        current_sum = nums[p1] + nums[p2]

        if current_sum == target:
            return (nums[p1], nums[p2])

        elif current_sum < target:
            p1 += 1

        else:
            p2 -= 1

    return None


n = int(input("Enter the number of inputs: "))
nums = []

for i in range(n):
    nums.append(int(input("Enter: ")))

nums.sort()  # required for two pointers

target = int(input("Enter the target number: "))

result = two_sum(nums, target)

if result:
    print(f"The pair is {result[0]} and {result[1]}")
else:
    print("No pair found")