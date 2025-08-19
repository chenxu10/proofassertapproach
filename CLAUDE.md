# Project Context for Claude Code

## Custom Commands

When the user says "give feedback", interpret this as:
"Give critical suggestions, point out wrong if there's any use X with red symbol, give fix and suggestions on how to prevent it next time. Encourage me if everything is correct."

This means:
1. Analyze the code for correctness and logic errors
2. Identify potential issues or improvements
3. Provide specific fixes with code examples
4. Suggest best practices to prevent similar issues

DO NOT make direct change on file! Just give out your findings in CLI.

When the user says words like "hint and comment", he means design comment as a computer science teacher to encourage his students do independent work as much as possible while helping him discreetly and unobstrusively to make sure it's not too hard for him to make progress.

The design of comments should follow research by Bjork Learning and Forgetting Lab to gauge students' Metacognition on data structure and algorithm design. To maximize his Germane Load and minimize Extraneous Load 
and reduce Intrinsic Load properly.

When create unit tests. Do not generate more than five tests.