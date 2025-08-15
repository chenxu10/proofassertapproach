"""
Test cases for Valid Parentheses problem based on constructive proof approach.

The Valid Parentheses problem: Given a string containing just the characters 
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

A valid string must satisfy:
1. Open brackets must be closed by the same type of brackets
2. Open brackets must be closed in the correct order
3. Every close bracket has a corresponding open bracket

Test cases are designed to verify proof requirements:
1. Correctness: Correctly identifies valid parentheses sequences
2. Completeness: Handles all invalid cases (wrong type, wrong order, unmatched)
3. Termination: Algorithm terminates for all finite strings
4. Stack invariant: Maintains proper bracket matching using stack LIFO property
5. Edge cases: Empty strings, single brackets, nested vs. interleaved patterns

Stack Invariant Proof for Valid Parentheses Algorithm:

Theorem: The stack-based algorithm correctly determines if parentheses are valid.

Algorithm:
    def is_valid(s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:  # closing bracket
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:  # opening bracket
                stack.append(char)
        
        return len(stack) == 0

Loop Invariant: 
At any point during iteration, stack contains only unmatched opening brackets 
in correct nesting order (most recent opening bracket on top).

Proof by Induction:

Base Case: Before processing any character, stack is empty.
- Invariant holds: no unmatched brackets exist ✓

Inductive Step: Assume invariant holds before processing character i.
Case 1 - Opening bracket:
  - Push onto stack
  - Invariant maintained: stack still contains only opening brackets ✓

Case 2 - Closing bracket with matching opening bracket on top:
  - Pop matching opening bracket
  - Invariant maintained: remaining brackets still properly nested ✓
  
Case 3 - Closing bracket with no match (empty stack or wrong type):
  - Return False immediately
  - Algorithm terminates with correct result ✓

Correctness:
- Valid string: All opening brackets matched and removed → empty stack
- Invalid string: Either unmatched closing bracket (early return) or 
  unmatched opening brackets (non-empty final stack)

Termination: Algorithm processes each character exactly once, O(n) steps.
"""

import unittest


def is_valid_parentheses(s):
    """
    Main function to validate parentheses string.
    
    Args:
        s (str): String containing only '(){}[]' characters
        
    Returns:
        bool: True if valid parentheses, False otherwise
    """
    stack = []
    mapping = get_bracket_mapping()
    
    for char in s:
        if is_closing_bracket(char):
            if not can_match_closing_bracket(stack, char, mapping):
                return False
        else:
            push_opening_bracket(stack, char)
    
    return is_stack_empty(stack)


def get_bracket_mapping():
    """
    Returns the mapping of closing brackets to their corresponding opening brackets.
    
    Returns:
        dict: Mapping of closing brackets to opening brackets
    """
    return {")": "(", "]": "[", "}": "{"}


def is_closing_bracket(char):
    """
    Checks if the character is a closing bracket.
    
    Args:
        char (str): Character to check
        
    Returns:
        bool: True if closing bracket, False otherwise
    """
    return char in ")}]"


def can_match_closing_bracket(stack, closing_bracket, mapping):
    """
    Attempts to match a closing bracket with the top of the stack.
    
    Args:
        stack (list): Stack of opening brackets
        closing_bracket (str): Closing bracket to match
        mapping (dict): Mapping of closing to opening brackets
        
    Returns:
        bool: True if match successful, False otherwise
    """
    if is_stack_empty(stack):
        return False
    
    top_bracket = pop_from_stack(stack)
    return top_bracket == mapping[closing_bracket]


def push_opening_bracket(stack, bracket):
    """
    Pushes an opening bracket onto the stack.
    
    Args:
        stack (list): Stack to push onto
        bracket (str): Opening bracket to push
    """
    stack.append(bracket)


def pop_from_stack(stack):
    """
    Pops and returns the top element from the stack.
    
    Args:
        stack (list): Stack to pop from
        
    Returns:
        str: Top element from stack
    """
    return stack.pop()


def is_stack_empty(stack):
    """
    Checks if the stack is empty.
    
    Args:
        stack (list): Stack to check
        
    Returns:
        bool: True if stack is empty, False otherwise
    """
    return len(stack) == 0


class TestValidParentheses(unittest.TestCase):
    
    def test_simple_valid_cases(self):
        """
        Test Case 1: Basic valid parentheses
        Proof requirement: Correctness - identifies valid sequences
        
        Examples: "()", "()[]{}", "{[]}"
        Expected: True for all
        
        This verifies the algorithm correctly identifies properly
        nested and matched parentheses sequences.
        """
        valid_cases = [
            "()",           # Simple pair
            "()[]{}", 	    # Multiple types
            "{[]}",         # Nested brackets
            "((()))",       # Nested same type
            "{[()]}",       # Complex nesting
        ]
        
        for case in valid_cases:
            result = is_valid_parentheses(case)
            self.assertTrue(result, f"'{case}' should be valid but got {result}")
            
    def test_simple_invalid_cases(self):
        """
        Test Case 2: Basic invalid parentheses
        Proof requirement: Completeness - identifies invalid sequences
        
        Examples: "(]", "([)]", "((("
        Expected: False for all
        
        This tests various ways parentheses can be invalid:
        wrong type matching, wrong order, unmatched brackets.
        """
        invalid_cases = [
            "(",            # Unmatched opening
            ")",            # Unmatched closing  
            "(]",           # Wrong type match
            "([)]",         # Wrong nesting order
            "(((",          # Multiple unmatched opening
            ")))",          # Multiple unmatched closing
            "}{",           # Wrong order
        ]
        
        for case in invalid_cases:
            result = is_valid_parentheses(case)
            self.assertFalse(result, f"'{case}' should be invalid but got {result}")
    
    def test_empty_string(self):
        """
        Test Case 3: Empty string
        Proof requirement: Base case handling
        
        Input: ""
        Expected: True (vacuously valid - no brackets to mismatch)
        
        This tests the algorithm's behavior on the empty string,
        which should be considered valid by definition.
        """
        result = is_valid_parentheses("")
        self.assertTrue(result, "Empty string should be valid")
        
    def test_single_brackets(self):
        """
        Test Case 4: Single bracket cases
        Proof requirement: Minimal invalid cases
        
        Examples: "(", ")", "{", "}", "[", "]"
        Expected: False for all single brackets
        
        This verifies the algorithm correctly handles the smallest
        possible invalid inputs (single unmatched brackets).
        """
        single_brackets = ["(", ")", "{", "}", "[", "]"]
        
        for bracket in single_brackets:
            result = is_valid_parentheses(bracket)
            self.assertFalse(result, f"Single bracket '{bracket}' should be invalid")
    
    def test_complex_nested_valid(self):
        """
        Test Case 5: Complex nested valid patterns
        Proof requirement: Algorithm scales with complexity
        
        Examples: Deep nesting, multiple bracket types
        Expected: True for properly formed complex patterns
        
        This tests the algorithm's correctness on more complex
        valid parentheses patterns to ensure it scales properly.
        """
        complex_valid = [
            "(())",                 # Double nesting
            "([{}])",               # Triple nested different types
            "{[()()]}",             # Multiple pairs in nesting
            "()[]{}",               # Sequential different types
            "((()))[]{}",           # Mixed sequential and nested
            "{[()]}()[]{}",         # Complex combination
        ]
        
        for case in complex_valid:
            result = is_valid_parentheses(case)
            self.assertTrue(result, f"Complex valid case '{case}' should be True")
    
    def test_complex_nested_invalid(self):
        """
        Test Case 6: Complex nested invalid patterns  
        Proof requirement: Detects subtle invalid patterns
        
        Examples: Interleaved brackets, subtle mismatches
        Expected: False for improperly formed patterns
        
        This tests the algorithm's ability to detect more subtle
        invalid patterns that might pass simpler validation.
        """
        complex_invalid = [
            "([)]",                 # Interleaved different types
            "(()",                  # Missing closing
            "())",                  # Extra closing
            "{[}]",                 # Wrong inner closing
            "([{})",                # Missing outer closing
            "{[(])}",               # Mixed up closing order
        ]
        
        for case in complex_invalid:
            result = is_valid_parentheses(case)
            self.assertFalse(result, f"Complex invalid case '{case}' should be False")
            
    def test_stack_behavior_verification(self):
        """
        Test Case 7: Stack behavior verification
        Proof requirement: Verify stack invariant maintained
        
        This test specifically monitors stack behavior to ensure
        the stack invariant is maintained throughout execution.
        We test by examining the algorithm's behavior on patterns
        that would break if stack wasn't working correctly.
        """
        # Test case that would fail if stack wasn't LIFO
        # Should process: { [ ( ) ] }
        # Stack evolution: [] → ['{'] → ['{','['] → ['{','[','('] 
        #                 → ['{','['] → ['{'] → []
        nested_case = "{[()]}"
        result = is_valid_parentheses(nested_case)
        self.assertTrue(result, "Stack LIFO behavior test should pass")
        
        # Test case that would incorrectly pass without proper stack
        # Should fail because of wrong nesting order
        wrong_nesting = "([)]"
        result = is_valid_parentheses(wrong_nesting)
        self.assertFalse(result, "Wrong nesting should fail with proper stack")


if __name__ == '__main__':
    unittest.main()