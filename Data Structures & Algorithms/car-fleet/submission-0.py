class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Pair each car's position with its speed
        pairs = [(p, s) for p, s in zip(position, speed)]

        # Sort cars by position from closest to target to farthest
        pairs.sort(reverse=True)

        # Stack stores the time it takes each fleet to reach the target
        stack = []

        # Process cars starting with the car closest to the target
        for p, s in pairs:

            # Calculate the time this car would take to reach the target
            time = (target - p) / s
            stack.append(time)

            # If this car reaches the target at the same time or earlier
            # than the fleet ahead of it, it will catch that fleet.
            # Therefore, it becomes part of the same fleet.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        # The number of remaining times represents the number of fleets
        return len(stack)