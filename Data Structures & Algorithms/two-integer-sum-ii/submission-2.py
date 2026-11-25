class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Array is sorted, ascending order 1234
        # returning a list of indicies
        # list index 1 < index 2, sorted value
        # The indicies have to be unique number

        # what does o(1) space mean, like no hashmap?

        mp = defaultdict(int)
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if mp[tmp]:
                return [mp[tmp], i + 1]
            mp[numbers[i]] = i + 1
        return []