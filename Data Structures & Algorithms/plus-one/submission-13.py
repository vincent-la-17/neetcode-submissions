class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # Start from the last digit and move toward the first digit
        for i in range(len(digits) - 1, -1, -1):

            # If the current digit is not 9, simply add 1
            # and return the result because there is no carry
            if digits[i] != 9:
                digits[i] += 1
                return digits

            # If the digit is 9, adding 1 makes it 0
            # and the carry moves to the digit on the left
            digits[i] = 0

        # If we reach here, every digit was 9
        # For example: [9, 9, 9] -> [1, 0, 0, 0]
        digits.insert(0, 1)

        # Return the updated number
        return digits