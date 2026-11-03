"""
LeetCode 1. 两数之和 (Two Sum)
https://leetcode.cn/problems/two-sum/

给定一个整数数组 nums 和目标值 target，
找出数组中和为目标值的两个整数的下标。

示例:
    输入: nums = [2, 7, 11, 15], target = 9
    输出: [0, 1]   (因为 nums[0] + nums[1] = 2 + 7 = 9)
"""
from typing import List


# ---------- 方法一：暴力枚举 ----------
# 思路：两两组合试一遍，看哪对加起来等于 target
# 时间复杂度 O(n^2)，空间复杂度 O(1)
# 数据量大时会很慢，但胜在直观，是思考的起点
def two_sum_brute(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# ---------- 方法二：哈希表（推荐） ----------
# 思路：遍历数组，对每个数 x，问一句——"target - x 之前出现过吗？"
# 用字典把"出现过的数 -> 下标"记下来，查询只需 O(1)，
# 整体时间复杂度降到 O(n)，空间换时间的经典示范
def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}  # {数值: 下标}
    for i, x in enumerate(nums):
        y = target - x          # 我需要的那个搭档
        if y in seen:           # 搭档之前出现过？
            return [seen[y], i] # 返回它的下标和我的下标
        seen[x] = i             # 把自己登记进花名册，等后面的数来找
    return []


# ---------- 本地自测 ----------
if __name__ == "__main__":
    # 几组测试用例：常规 / 有负数 / 无解
    cases = [
        ([2, 7, 11, 15], 9),
        ([-3, 4, 3, 90], 0),
        ([1, 2, 3], 100),
    ]
    for nums, target in cases:
        print(f"nums={nums}, target={target}")
        print("  暴力法:", two_sum_brute(nums, target))
        print("  哈希法:", two_sum(nums, target))
