class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Array is sorted, ascending order 1234
        # returning a list of indicies
        # list index 1 < index 2, sorted value
        # The indicies have to be unique number

        # l start list, right end list
        # target 3, 4+1= 5 target
        # sum > target sum, r - 1
        # sum < target sum, l + 1

        l,r = 0, len(numbers) - 1

        while l<r:
            two_sum = numbers[r] + numbers[l]
            if target == two_sum:
                return [l + 1, r + 1]
            if target > two_sum:
                l += 1
            else:
                r-=1
        return []