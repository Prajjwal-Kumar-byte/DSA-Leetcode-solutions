# LC 8 — String to Integer (atoi)

## Problem

Implement the `myAtoi` function that converts a string into a 32-bit signed integer.

The conversion follows these rules:

1. Ignore leading spaces.
2. Check for an optional `+` or `-` sign.
3. Read consecutive digits and convert them into an integer.
4. Stop reading when a non-digit character is encountered.
5. If no digits are found, return `0`.
6. If the resulting number is outside the 32-bit signed integer range, clamp it.

The valid 32-bit signed integer range is:

```text
[-2^31, 2^31 - 1]

[-2147483648, 2147483647]
------------------------------------------------------------------------------------------
Example
Example 1
Input:
s = "42"

Output:
42
Example 2
Input:
s = "   -42"

Output:
-42
Example 3
Input:
s = "4193 with words"

Output:
4193
The conversion stops when the first non-digit character (" ") is encountered.
Example 4
Input:
s = "words and 987"

Output:
0
No valid number appears at the beginning after ignoring leading spaces.
----------------------------------------------------------------------------------
What the Problem Requires
We need to process the string in a specific order.
String
  ↓
Ignore leading spaces
  ↓
Check sign
  ↓
Read digits
  ↓
Stop at first non-digit
  ↓
Build integer
  ↓
Apply sign
  ↓
Clamp to 32-bit range
The important point is that the order matters.
For example:
"   -123abc"
should become:
-123
because:
- "   " → ignored
- "-" → negative sign
- "123" → valid digits
- "a" → stop
----------------------------------------------------------------------------------------------------------
Solution Approach
This solution uses recursion to process the digits one at a time.
Instead of using a normal loop to construct the number, we create a recursive function:
parse(i, num)
Its job is:
Starting from index i, continue reading digits and add them to the number represented by num.

For example, suppose we have:
s = "123"
The recursive calls conceptually become:
parse(0, 0)
    ↓
parse(1, 1)
    ↓
parse(2, 12)
    ↓
parse(3, 123)
When the recursion reaches the end of the string, or encounters a non-digit character, it returns the number constructed so far.
-------------------------------------------------------------------------------------------------------------------------
Step-by-Step Algorithm
Step 1 — Handle an Empty String
If:
s = ""
there is nothing to convert.
Return:
0
Step 2 — Skip Leading Spaces
Start with:
index = 0
Move index forward while:
s[index] == " "
For:
"   123"
the index moves:
0 → 1 → 2 → 3
and eventually points to:
1
Step 3 — Determine the Sign
The next character may be:
+
or:
-
If it is -:
sign = -1
If it is +:
sign = 1
If neither is present:
sign = 1
The sign is stored separately while the digits are processed.
Step 4 — Parse the Digits Recursively
The recursive function receives:
i
num
where:
- i = current position in the string
- num = number constructed so far
Suppose:
s = "123"
Initially:
parse(0, 0)
The current digit is:
1
Convert it to an integer:
digit = 1
Then construct:
new_num = num * 10 + digit
Therefore:
new_num = 0 * 10 + 1
        = 1
Then recursively process the next digit:
parse(1, 1)
Step 5 — Continue Building the Number
For the next digit:
2
we calculate:
new_num = 1 * 10 + 2
        = 12
Then:
parse(2, 12)
For the final digit:
3
we calculate:
new_num = 12 * 10 + 3
        = 123
Then:
parse(3, 123)
Step 6 — Base Case
The recursive function stops when either:
i == len(s)
or:
s[i] is not a digit
For example:
s = "123abc"
The recursion processes:
1
12
123
When it reaches:
a
a is not a digit.
Therefore, the recursion returns:
123
The remaining characters:
abc
are ignored.
------------------------------------------------------------------------------------------------------------------------
Recursion Structure
The recursive function can be understood as:
parse(i, num)
       |
       |-- Is i at the end?
       |       YES → return num
       |
       |-- Is s[i] not a digit?
       |       YES → return num
       |
       |-- Read current digit
       |
       |-- Build new number
       |
       └-- parse(i + 1, new_num)
The important idea is:
Each recursive call processes exactly one more character.
-------------------------------------------------------------------------------------------------------------------------
Example Recursion Trace
For:
s = "123"
the recursion behaves like:
parse(0, 0)
    |
    | digit = 1
    ↓
parse(1, 1)
    |
    | digit = 2
    ↓
parse(2, 12)
    |
    | digit = 3
    ↓
parse(3, 123)
    |
    | end of string
    ↓
return 123
The returned value travels back through the recursive calls:
123
 ↑
parse(2, 12)

123
 ↑
parse(1, 1)

123
 ↑
parse(0, 0)
-------------------------------------------------------------------------------------------------------------------------
Applying the Sign
After parsing the digits, the sign is applied.
For:
s = "-123"
the parser produces:
123
and:
sign = -1
Therefore:
123 * -1
= -123
-------------------------------------------------------------------------------------------------------------------------
Handling Overflow
The final result must fit inside:
[-2147483648, 2147483647]
Therefore:
if num > 2147483647:
    num = 2147483647
and:
if num < -2147483648:
    num = -2147483648
This is called clamping.
For example:
Input:
"999999999999999999999"
The number is larger than the maximum 32-bit signed integer.
Therefore the result becomes:
2147483647
Similarly:
"-999999999999999999999"
becomes:
-2147483648
-------------------------------------------------------------------------------------------------------------------------
mportant Edge Cases
Empty String
""
→ 0
Only Spaces
"     "
→ 0
Positive Sign
"+123"
→ 123
Negative Sign
"-123"
→ -123
Leading Spaces
"   123"
→ 123
Digits Followed by Characters
"123abc"
→ 123
Characters Before Digits
"abc123"
→ 0
Overflow
"999999999999999999"
→ 2147483647
Negative Overflow
"-999999999999999999"
→ -2147483648
-------------------------------------------------------------------------------------------------------------------------
Algorithm Summary
1. Check whether the string is empty.
2. Skip leading spaces.
3. Determine the sign.
4. Recursively process consecutive digits.
5. Stop at the first non-digit.
6. Apply the sign.
7. Clamp the result to the 32-bit signed integer range.
8. Return the final integer.
-------------------------------------------------------------------------------------------------------------------------
Complexity Analysis
Let:
n = length of the input string
Time Complexity
O(n)
Each character is processed at most once.
The recursive parser moves from left to right through the string.
Space Complexity
O(n)
The recursive function creates one stack frame for each processed digit.
Therefore, in the worst case, the recursion depth can be n.
This is different from an iterative solution, which would use:
O(1)
auxiliary space.
-------------------------------------------------------------------------------------------------------------------------
Important Concepts
This problem demonstrates several useful concepts:
1. String Traversal
Processing a string character by character.
2. Index Tracking
Using an index to remember the current position.
3. Recursion
Processing one character and recursively asking the next call to process the remaining characters.
4. Building a Number
Using:
num * 10 + digit
to append a digit to an integer.
For example:
12 → append 3 → 123
using:
12 * 10 + 3
= 123
5. Base Cases
Stopping recursion when:
- the end of the string is reached
- a non-digit character is encountered
6. Integer Range Handling
Clamping the result to the valid 32-bit signed integer range.
-------------------------------------------------------------------------------------------------------------------------
Key Takeaways
- index tells us where we currently are in the string.
- num stores the number constructed so far.
- Each recursive call processes one additional digit.
- num * 10 + digit appends a digit to the current number.
- The recursion stops at the first non-digit character.
- Leading spaces are handled before parsing.
- The sign is handled separately.
- The final result must be clamped to the 32-bit signed integer range.
- The recursive approach takes O(n) time and O(n) recursion-stack space.
- An iterative solution can achieve O(1) auxiliary space.
