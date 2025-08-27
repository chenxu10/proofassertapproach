# Project Context for Claude Code

## Custom Commands

### Give Feedback

When the user says "give feedback", interpret this as:

Always criticize first and encourage later. But do not forget to encourage.

"Give critical suggestions, point out wrong if there's any use X with red symbol, give fix and suggestions on how to prevent it next time. Encourage me if everything is correct."

This means:
1. Analyze the code for correctness and logic errors
2. Identify potential issues or improvements
3. Provide specific fixes with code examples
4. Suggest best practices to prevent similar issues

DO NOT make direct change on file! Just give out your findings in CLI.

Give encouragement on what is doing correct should kept for the next time. Trying to find smallest amount positive signs of the solution even when
the solution is totally off.

### Hint and Comment

When the user says words like "hint and comment", he means design comment as a computer science teacher to encourage his students to acquire as much experience of independent work as possible. You do not want to left him alone without any help that he makes no progress at all. Try to help the student effectively but unobstrusively. You should help student to solve the problem at hand, but more important you should develop students' ability to solve a class of problem in the future by himself.

The design of comments should follow research by Bjork Learning and Forgetting Lab to gauge students' Metacognition on data structure and algorithm design. To maximize his Germane Load and minimize Extraneous Load and reduce Intrinsic Load properly.

The comment should be a well-defined task with an appropriate difficulty level for the particular individual based on his input in the current function or class, informative feedback, and opportunities for repetition and corrections of errors.

The comment should be directly written in function with blankets for students to fill in the actual content and change original file directly.

When creating unit tests. Do not generate more than five tests.

### Draw a diagram

When users say "draw a diagram" he means adding ASICC style diagram into docstring of the function. 
Use cases from unit test. Test cases should be small sized. Add notation. 
Diagram should be easy for user to build mental representation to see things at a glance suggested research by Anderson Ericsson.
If necessary, add data flow. 

