class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        carry, i = 1, 0

        while carry and i < len(digits):
            if digits[i] != 9:
                digits[i] += carry
                carry = 0
            else:
                digits[i] = 0
            i += 1
        
        if carry:
            digits.append(carry)
        
        return digits[::-1]