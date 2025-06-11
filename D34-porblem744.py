class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        left, right = 0, n  # search range is [left … right)

        # Find the insertion point where ord(letters[mid]) > ord(target)
        while left < right:
            mid = (left + right) // 2
            if ord(letters[mid]) > ord(target):
                right = mid       # mid could be the answer
            else:
                left = mid + 1    # skip mid and anything ≤ target

        # left == 0..n, so wrap around with mod n
        return letters[left % n]