# LC 282 — Expression Add Operators

## Problem

Given a string containing only digits and an integer `target`, insert the operators:

- `+`
- `-`
- `*`

between the digits so that the resulting expression evaluates to `target`.

Operands must not contain leading zeros.

Return all valid expressions.

### Example

```text
Input:
num = "123"
target = 6

Output:
["1+2+3", "1*2*3"]

What the Problem Requires
We need to construct mathematical expressions from the given digit string.
For each position, we may:
- take one digit as a number
- take multiple digits as one number
- place +, -, or * before the next number
For example, from:
123
we can create:
123
1+23
1-23
1*23
12+3
12-3
12*3
1+2+3
1+2-3
1+2*3
...
We keep only the expressions whose final value equals target.
--------------------------------------------------------------
Solution Approach
The problem is solved using Backtracking / Depth-First Search.
We build the expression from left to right.
At every recursive step:
1. Choose the next number from the remaining digits.
2. If it is the first number, start the expression with it.
3. Otherwise, try:
   - addition
   - subtraction
   - multiplication
4. Recursively process the remaining digits.
5. Continue exploring other choices.
The recursion explores all possible valid expressions.
-------------------------------------------------------------
Recursive State
The recursive function keeps track of four values:
index
The position of the next unused digit.
expression
The mathematical expression constructed so far.
Example:
"1+2"
value
The current evaluated value of the expression.
Example:
1 + 2 = 3
so:
value = 3
previous
The contribution of the most recently added operand.
This is required to correctly handle multiplication precedence.
---------------------------------------------------------------
Algorithm
Step 1 — Start from index 0
Begin with:
index = 0
expression = ""
value = 0
previous = 0
Step 2 — Choose the next number
At each index, try every possible substring beginning at that position.
For:
123
at index 0, the possible numbers are:
1
12
123
If we choose 1, the recursion continues with the remaining:
23
Step 3 — Handle the first number
The first number does not have an operator before it.
For example:
1
becomes the starting expression.
Step 4 — Try all operators
After the first number, try:
+
-
*
For example, after choosing 1 and then 2:
1+2
1-2
1*2
Each possibility creates another recursive branch.
Handling Multiplication
Multiplication has higher precedence than addition and subtraction.
For example:
2 + 3 * 2
should equal:
2 + 6 = 8
not:
(2 + 3) * 2 = 10
Suppose the current expression is:
2 + 3
The current value is:
5
and:
previous = 3
If we now multiply by 2, we remove the previous contribution:
5 - 3
and replace it with:
3 * 2
Therefore:
new_value = value - previous + previous * number
Example:
5 - 3 + (3 * 2)
= 8
Leading Zero Rule
Numbers such as:
05
00
012
are not allowed.
However:
0
by itself is valid.
Therefore, if a number starts with 0, we stop extending that number.
--------------------------------------------------------------------
Base Case
When:
index == len(num)
all digits have been used.
If:
value == target
the current expression is valid and is added to the result.
Otherwise, that recursive branch is discarded.
--------------------------------------------------------------------
Backtracking Pattern
The main idea is:
Choose the next number
        ↓
Choose an operator
        ↓
Recurse on the remaining digits
        ↓
Return
        ↓
Try another choice
Because strings such as:
expression + "+" + current
create a new string, we do not need to manually remove characters from the expression after recursion returns.
--------------------------------------------------------------------------------------------------------------
Complexity Analysis
Let n be the number of digits.
Time Complexity
Approximately:
O(4^n)
in the worst case.
At each gap between digits, we can conceptually:
- join the digits
- insert +
- insert -
- insert *
so the number of possibilities grows exponentially.
The actual implementation also performs substring creation and integer conversion, so the precise runtime contains additional factors.
Space Complexity
O(n)
for the recursive call stack, excluding the output list.
The returned expressions themselves can require exponential output space.
-------------------------------------------------------------------------------------------------------------------
Key Takeaways
- This is a backtracking problem.
- Build the expression from left to right.
- index tracks how many digits have been consumed.
- expression stores the expression constructed so far.
- value stores its current evaluated value.
- previous is needed to correctly handle multiplication.
- The first number is handled separately because it has no operator before it.
- Leading-zero operands must be rejected.
- Each recursive call solves the remaining unused digits.
-------------------------------------------------------------------------------------------------------------------

