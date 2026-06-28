n = int(input("Enter number of elements: "))

nums = []
for i in range(n):
    nums.append(int(input(f"Enter element {i + 1}: ")))

total = sum(nums)
left_sum = 0
answer = []

for num in nums:
    total -= num
    answer.append(abs(left_sum - total))
    left_sum += num

print("Answer:", answer)