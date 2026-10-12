class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        i=0
        for num in nums:
            other = target-num
            if other in map:
                return [map.get(other),i]
            map[num]=i
            i+=1
        