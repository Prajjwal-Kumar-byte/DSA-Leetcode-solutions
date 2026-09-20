# LC 17 — Letter Combinations of a Phone Number

## Problem

Given a string containing digits from `2` to `9`, return all possible letter combinations that the digits could represent.

The mapping is based on the letters found on a traditional telephone keypad:

```text
2 → abc
3 → def
4 → ghi
5 → jkl
6 → mno
7 → pqrs
8 → tuv
9 → wxyz
The order of the returned combinations does not matter.
If the input is empty, return an empty list.
--------------------------------------------------------------------------------------------------------------------------
Example
Example 1
Input:
digits = "23"

Output:
[
    "ad",
    "ae",
    "af",
    "bd",
    "be",
    "bf",
    "cd",
    "ce",
    "cf"
]
Explanation:
2 → a, b, c
3 → d, e, f
Therefore, every letter from 2 can be combined with every letter from 3.
Example 2
Input:
digits = ""

Output:
[]
Example 3
Input:
digits = "2"

Output:
["a", "b", "c"]
-------------------------------------------------------------------------------------------------------------------------
What the Problem Requires
We need to generate every possible string that can be formed by selecting:
- one letter from the first digit
- one letter from the second digit
- one letter from the third digit
- and so on
For example:
digits = "23"
The choices are:
2 → a b c
3 → d e f
We need to combine them:
a + d → ad
a + e → ae
a + f → af

b + d → bd
b + e → be
b + f → bf

c + d → cd
c + e → ce
c + f → cf
So the final answer contains:
9 combinations
-------------------------------------------------------------------------------------------------------------------------
Solution Approach
This problem is naturally solved using Backtracking.
We construct one combination from left to right.
At each position:
1. Look at the current digit.
2. Find the letters mapped to that digit.
3. Choose one letter.
4. Add that letter to the current combination.
5. Recursively process the next digit.
6. Remove the letter after returning from recursion.
7. Try the next letter.
The core pattern is:
Choose
  ↓
Recurse
  ↓
Undo
  ↓
Choose another option
-------------------------------------------------------------------------------------------------------------------------
Why Backtracking Works
Suppose:
digits = "23"
For the first digit:
2 → a, b, c
Suppose we choose:
a
Our current combination becomes:
a
Now we recursively solve the remaining digit:
3 → d, e, f
This creates:
ad
ae
af
After all possibilities beginning with a are finished, we undo the choice:
a
↓
empty
Then choose:
b
and repeat:
bd
be
bf
Then:
c
giving:
cd
ce
cf
-------------------------------------------------------------------------------------------------------------------------
Recursive State
The recursive function is:
backtrack(index)
Its meaning is:
Build all possible combinations starting from digit index.

The recursion keeps track of:
index
The position of the digit we are currently processing.
For:
digits = "23"
we have:
index = 0 → digit "2"
index = 1 → digit "3"
index = 2 → finished
current
current stores the combination currently being constructed.
For example:
current = ["a", "d"]
represents:
"ad"
answer
answer stores every completed combination.
Example:
answer = [
    "ad",
    "ae",
    "af"
]
-------------------------------------------------------------------------------------------------------------------------
Algorithm
Step 1 — Handle Empty Input
If:
digits = ""
there are no combinations.
Return:
[]

Step 2 — Create the Phone Mapping
Create a mapping from each digit to its letters:
2 → abc
3 → def
4 → ghi
5 → jkl
6 → mno
7 → pqrs
8 → tuv
9 → wxyz


Step 3 — Start Backtracking
Start from:
index = 0
This means:
Start processing the first digit.

Step 4 — Base Case
If:
index == len(digits)
we have processed every digit.
Therefore, current contains one complete combination.
Convert it into a string:
"".join(current)
and add it to answer.
Then return.


Step 5 — Get the Current Digit's Letters
For:
digits = "23"
index = 0
we get:
digits[index] = "2"
The mapping tells us:
letters = "abc"


Step 6 — Try Every Letter
Loop through:
a
b
c
For each letter:
Choose
Add it to current.
current.append(letter)
Recurse
Move to the next digit.
backtrack(index + 1)
Undo
Remove the letter.
current.pop()
This allows the next letter to be tried.
-------------------------------------------------------------------------------------------------------------------------
The Choose → Recurse → Undo Pattern
The most important part of this solution is:
for letter in letters:

    CHOOSE
    current.append(letter)

    RECURSE
    backtrack(index + 1)

    UNDO
    current.pop()
This is the fundamental backtracking pattern.
-------------------------------------------------------------------------------------------------------------------------
Why Do We Need pop()?
This is extremely important.
Suppose:
digits = "23"
We choose:
a
So:
current = ["a"]
Then choose:
d
Now:
current = ["a", "d"]
We reach the base case and store:
"ad"
Now recursion returns.
If we did not remove d, current would still contain:
["a", "d"]
When we try e, we would incorrectly get:
"ade"
Instead, we undo:
current.pop()
Now:
current = ["a"]
Then we can correctly choose:
e
giving:
"ae"
So pop() means:
Remove the choice I just finished exploring.
-------------------------------------------------------------------------------------------------------------------------
Recursion Tree
For:
digits = "23"
the recursion tree looks like:
                         ""
                    /     |     \
                   a      b      c
                 / | \   / | \  / | \
                ad ae af bd be bf cd ce cf
Each path from the root to a leaf represents one complete combination.
-------------------------------------------------------------------------------------------------------------------------
Detailed Trace
Starting with:
current = []
index = 0
The first choice is:
a
So:
current = ["a"]
Recurse:
backtrack(1)
Now the current digit is:
3
Choose:
d
So:
current = ["a", "d"]
We have reached the end:
index == len(digits)
Therefore:
"ad"
is added to the answer.
Then we undo:
current.pop()
Now:
current = ["a"]
Try:
e
giving:
"ae"
Then:
f
giving:
"af"
After finishing all choices for a, we return to the previous level.
We undo:
a
and try:
b
This produces:
bd
be
bf
Then we try:
c
producing:
cd
ce
cf
-------------------------------------------------------------------------------------------------------------------------
Python Solution
The implementation uses:
- a dictionary for the phone keypad mapping
- a list named current to build one combination
- a list named answer to store completed combinations
- recursive backtracking to explore all possibilities
The solution is stored in:
solution.py
-------------------------------------------------------------------------------------------------------------------------
Complexity Analysis
Let:
n = number of digits
Each digit normally has either 3 or 4 possible letters.
In the worst case, all digits are 7 or 9, which each have 4 letters.
Therefore, the maximum number of combinations is:
4^n
Time Complexity
O(n × 4^n)
There can be up to:
4^n
combinations.
Each completed combination contains n characters, so constructing/storing each result takes O(n) time.
Therefore:
O(n × 4^n)
is the appropriate output-sensitive complexity.
Space Complexity
The recursion depth is:
O(n)
and the current list can contain at most n characters.
Therefore, the auxiliary recursion space is:
O(n)
excluding the output list.
The output itself can contain up to:
O(n × 4^n)
characters.
-------------------------------------------------------------------------------------------------------------------------
Important Concepts
1. Backtracking
The solution repeatedly follows:
Choose
→ Recurse
→ Undo
2. Recursion
Each recursive call processes exactly one more digit.
backtrack(index)
means:
Process the digits starting from index.

3. Mutable State
current is shared between recursive calls.
We modify it:
append
and restore it:
pop
This is what makes backtracking possible.
4. Base Case
When:
index == len(digits)
a complete combination has been constructed.
5. Recursion Tree
Every branch represents a different choice of letters.
Every leaf represents one complete answer.
-------------------------------------------------------------------------------------------------------------------------
Key Takeaways
- The problem asks us to generate every possible letter combination.
- Each digit gives us a set of possible letters.
- We process one digit at a time.
- index tells us which digit we are processing.
- current stores the combination currently being built.
- answer stores completed combinations.
- For every letter, we:
  1. choose it
  2. recursively process the next digit
  3. undo the choice
- current.pop() is the backtracking step.
- The recursion tree represents all possible combinations.
- The worst-case number of combinations is 4^n.
- Time complexity is O(n × 4^n), excluding details of Python string/list operations.
- Auxiliary recursion space is O(n), excluding the output.
