class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # Initialize the result with 0s.
        # If there is no warmer temperature in the future,
        # the answer for that day will remain 0.
        result = [0] * len(temperatures)

        # Stack stores tuples of:
        # (temperature, index)
        #
        # The stack will maintain temperatures that are
        # still waiting to find a warmer temperature.
        stack = []

        # Go through each temperature along with its index
        for index, temp in enumerate(temperatures):

            # If the current temperature is warmer than the
            # temperature at the top of the stack, then we
            # have found the warmer day for that stack entry.
            while stack and temp > stack[-1][0]:

                # Remove the previous temperature from the stack
                # and get its temperature and index.
                # thiis pops a tuple
                stackTemp, stackind = stack.pop()

                # Calculate how many days passed between the
                # previous temperature and the current temperature.
                result[stackind] = index - stackind

            # Add the current temperature and its index to the stack.
            # It may need to wait for a warmer temperature later.
            stack.append((temp, index))

        # Return the number of days until a warmer temperature
        # for each day.
        return result