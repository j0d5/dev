/// # Two Sum
class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        for i in 0..<nums.count - 1 {
            for j in i+1..<nums.count {
                if nums[i] + nums[j] == target {
                    return [i, j]
                }
            }
        }
        return []
    }
}

print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([3, 2, 3], 6))
print(Solution().twoSum([2,5,5,11], 10))