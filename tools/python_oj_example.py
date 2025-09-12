# Example solution that calculates averages
import sys

for line in sys.stdin:
    nums = list(map(float, line.strip().split()))
    avg = sum(nums) / len(nums)
    print(f"{avg:.1f}")