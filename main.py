from leetcode.arrays.remove_element import Solution

def test_remove_element():
    solution = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    k = solution.removeElement(nums, val)
    print(f"Input: nums = [3, 2, 2, 3], val = 3")
    print(f"Output: {k}, nums = {nums[:k]}")

def main():
    test_remove_element()

if __name__ == "__main__":
    main()
