class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:

        result = []

        def backtrack(index, expression, value, previous):

            # Base case
            if index == len(num):
                if value == target:
                    result.append(expression)
                return

            # Choose the next number
            for end in range(index, len(num)):

                # Don't allow numbers like 05
                if num[index] == "0" and end > index:
                    break

                current = num[index:end + 1]
                number = int(current)
                next_index = end + 1

                # First number
                if index == 0:
                    backtrack(
                        next_index,
                        current,
                        number,
                        number
                    )

                else:

                    # Addition
                    backtrack(
                        next_index,
                        expression + "+" + current,
                        value + number,
                        number
                    )

                    # Subtraction
                    backtrack(
                        next_index,
                        expression + "-" + current,
                        value - number,
                        -number
                    )

                    # Multiplication
                    new_value = (
                        value
                        - previous
                        + previous * number
                    )

                    backtrack(
                        next_index,
                        expression + "*" + current,
                        new_value,
                        previous * number
                    )

        backtrack(0, "", 0, 0)

        return result
