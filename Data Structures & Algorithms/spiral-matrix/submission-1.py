class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        #0111-1-1-10
        #3up!=down
        #4left!=right
        # Get the number of rows and columns in the matrix
        rows, columns = len(matrix), len(matrix[0])

        # Define the current boundaries of the unvisited portion
        up = left = 0
        right = columns - 1
        down = rows - 1

        # Continue until every element has been added to result
        while len(result) < rows * columns:

            # Traverse the top row from left to right
            for col in range(left, right + 1):
                result.append(matrix[up][col])

            # Traverse the right column from top to bottom
            # Start at up + 1 because the top-right element
            # was already added in the previous loop
            for row in range(up + 1, down + 1):
                result.append(matrix[row][right])

            # Traverse the bottom row from right to left
            # Only do this if there is a distinct bottom row.
            # This prevents traversing the same row twice
            # when up == down.
            if up != down:
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[down][col])

            # Traverse the left column from bottom to top
            # Only do this if there is a distinct left column.
            # Start at down - 1 and stop at up + 1 because
            # both corners were already visited.
            if left != right:
                for row in range(down - 1, up, -1):
                    result.append(matrix[row][left])

            # Move all four boundaries inward
            # so that the next iteration processes
            # the next inner layer of the matrix
            up += 1
            left += 1
            right -= 1
            down -= 1

        return result