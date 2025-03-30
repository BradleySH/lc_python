from leetcode.arrays.remove_element import Solution
from leetcode.arrays.remove_duplicates import RemoveDuplicates
def test_remove_element():
    solution = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    k = solution.removeElement(nums, val)
    print(f"Input: nums = [3, 2, 2, 3], val = 3")
    print(f"Output: {k}, nums = {nums[:k]}")

def test_remove_duplicates():
    solution = RemoveDuplicates()
    nums = [1, 1, 2]
    k = solution.remove_duplicates(nums)
    print(f"Input: nums = [1, 1, 2]")
    print(f"Output: {k}, nums = {nums[:k]}")

def main():
    test_remove_element()
    test_remove_duplicates()
if __name__ == "__main__":
    main()
