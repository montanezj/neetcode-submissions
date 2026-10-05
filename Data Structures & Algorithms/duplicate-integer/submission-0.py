class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        ui = set()

        for i in nums:
            if i in ui:
                return True
            ui.add(i)
        return False