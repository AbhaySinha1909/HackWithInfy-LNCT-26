class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        ans = []

        left_remove = 0
        right_remove = 0

        # Find minimum number of removals needed
        for ch in s:
            if ch == '(':
                left_remove += 1

            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        def backtrack(index, left_count, right_count,
                      left_remove, right_remove, curr):

            # Reached end
            if index == len(s):
                if left_remove == 0 and right_remove == 0:
                    if left_count == right_count:
                        ans.append("".join(curr))
                return

            ch = s[index]

            # '('
            if ch == '(':

                # Option 1: Remove '('
                if left_remove > 0:
                    backtrack(
                        index + 1,
                        left_count,
                        right_count,
                        left_remove - 1,
                        right_remove,
                        curr
                    )

                # Option 2: Keep '('
                curr.append(ch)

                backtrack(
                    index + 1,
                    left_count + 1,
                    right_count,
                    left_remove,
                    right_remove,
                    curr
                )

                curr.pop()

            # ')'
            elif ch == ')':

                # Option 1: Remove ')'
                if right_remove > 0:
                    backtrack(
                        index + 1,
                        left_count,
                        right_count,
                        left_remove,
                        right_remove - 1,
                        curr
                    )

                # Option 2: Keep ')'
                # Only if there is an unmatched '('
                if left_count > right_count:

                    curr.append(ch)

                    backtrack(
                        index + 1,
                        left_count,
                        right_count + 1,
                        left_remove,
                        right_remove,
                        curr
                    )

                    curr.pop()

            # Letter
            else:
                curr.append(ch)

                backtrack(
                    index + 1,
                    left_count,
                    right_count,
                    left_remove,
                    right_remove,
                    curr
                )

                curr.pop()

        backtrack(
            0,
            0,
            0,
            left_remove,
            right_remove,
            []
        )

        return list(set(ans))