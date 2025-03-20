# # # string decoding
# # import unittest
# # def decode_string(str):
# #     if not str:
# #         return ""
    
# #     stack = []
# #     curr_str = ""
# #     curr_num = 0

# #     for x in str:
# #         if x.isdigit():
# #             curr_num = curr_num * 10 + int(x)
# #         elif x == "[":
# #             # save prev stuff, reset stuff
# #             prev_num = int(curr_num)
# #             prev_str = curr_str
# #             stack.append((prev_str, prev_num))
# #             curr_num = 
# #             curr_str = ""
# #         elif x == "]":
# #             # pop prev and add to it
# #             prev_str, prev_num = stack.pop()
# #             curr_str = prev_str + curr_str * prev_num
# #         else:
# #             curr_str += x

# #     return curr_str


# # class TestStringDecoding(unittest.TestCase):
    
# #     def test_basic_cases(self):
# #         # Basic test cases
# #         self.assertEqual(decode_string("3[a]2[bc]"), "aaabcbc")
# #         self.assertEqual(decode_string("3[a2[c]]"), "accaccacc")
# #         self.assertEqual(decode_string("2[abc]3[cd]ef"), "abcabccdcdcdef")
        
# #     def test_single_letter_repetition(self):
# #         # Test single letter repetition
# #         self.assertEqual(decode_string("10[a]"), "aaaaaaaaaa")
# #         self.assertEqual(decode_string("1[a]"), "a")
        
# #     def test_nested_patterns(self):
# #         # Test more complex nested patterns
# #         self.assertEqual(decode_string("2[a3[b]c]"), "abbbcabbc")
# #         self.assertEqual(decode_string("4[xy]z3[a]"), "xyxyxyxyzaaa")
# #         self.assertEqual(decode_string("3[a]2[b4[c]d]"), "aaabccccdbccccd")
        
# #     def test_edge_cases(self):
# #         # Test edge cases
# #         self.assertEqual(decode_string(""), "")
# #         self.assertEqual(decode_string("abc"), "abc")  # No brackets
# #         self.assertEqual(decode_string("3[a]2[b4[c]d]ef"), "aaabccccdbcccdef")  # With trailing characters
        
# #     def test_complex_examples(self):
# #         # Test more complex examples
# #         self.assertEqual(decode_string("2[3[a]b]1[cd]"), "aaabaaabcd")
# #         self.assertEqual(decode_string("3[z]2[2[y]pq4[2[jk]e1[f]]]"), 
# #                          "zzz" + 2 * ("yypq" + 4 * ("jkjkef")))
        
# #     def test_deep_nesting(self):
# #         # Test with multiple levels of nesting
# #         self.assertEqual(decode_string("1[1[1[a]]]"), "a")
        
# #         # A more challenging deep nesting case
# #         deep_nest = "1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[xx]]]]]]]]]]]]]]]]]]]]"
# #         self.assertEqual(decode_string(deep_nest), "xx")
        
# #     def test_original_example(self):
# #         # Test the original complex example
# #         complex_example = "3[a]2[c]2[p2[x]]ef4[3[a]2[cbb]]"
# #         expected = "aaaccpp" + "xx" * 2 + "ef" + 4 * (3 * "a" + 2 * "cbb")
# #         self.assertEqual(decode_string(complex_example), expected)


# # if __name__ == "__main__":
# #     unittest.main()


# import unittest

# def decode_string(s):
#     if not s:
#         return ""
        
#     stack = []
#     curr_str = ""
#     curr_num = 0
    
#     for char in s:
#         if char.isdigit():
#             curr_num = curr_num * 10 + int(char)
#         elif char == '[':
#             # Push current state to stack and reset
#             stack.append((curr_str, curr_num))
#             curr_str = ""
#             curr_num = 0
#         elif char == ']':
#             # Pop previous state
#             prev_str, num = stack.pop()
#             # Combine with current state
#             curr_str = prev_str + curr_str * num
#         else:
#             # Just add the character to current string
#             curr_str += char
    
#     return curr_str


# class TestStringDecoding(unittest.TestCase):
    
#     def test_basic_cases(self):
#         # Basic test cases
#         self.assertEqual(decode_string("3[a]2[bc]"), "aaabcbc")
#         self.assertEqual(decode_string("3[a2[c]]"), "accaccacc")
#         self.assertEqual(decode_string("2[abc]3[cd]ef"), "abcabccdcdcdef")
        
#     def test_single_letter_repetition(self):
#         # Test single letter repetition
#         self.assertEqual(decode_string("10[a]"), "aaaaaaaaaa")
#         self.assertEqual(decode_string("1[a]"), "a")
        
#     def test_nested_patterns(self):
#         # Test more complex nested patterns
#         self.assertEqual(decode_string("2[a3[b]c]"), "abbbcabbc")
#         self.assertEqual(decode_string("4[xy]z3[a]"), "xyxyxyxyzaaa")
#         self.assertEqual(decode_string("3[a]2[b4[c]d]"), "aaabccccdbccccd")
        
#     def test_edge_cases(self):
#         # Test edge cases
#         self.assertEqual(decode_string(""), "")
#         self.assertEqual(decode_string("abc"), "abc")  # No brackets
#         self.assertEqual(decode_string("3[a]2[b4[c]d]ef"), "aaabccccdbcccdef")  # With trailing characters
        
#     def test_complex_examples(self):
#         # Test more complex examples
#         self.assertEqual(decode_string("2[3[a]b]1[cd]"), "aaabaaabcd")
#         self.assertEqual(decode_string("3[z]2[2[y]pq4[2[jk]e1[f]]]"), 
#                          "zzz" + 2 * ("yypq" + 4 * ("jkjkef")))
        
#     def test_deep_nesting(self):
#         # Test with multiple levels of nesting
#         self.assertEqual(decode_string("1[1[1[a]]]"), "a")
        
#         # A more challenging deep nesting case
#         deep_nest = "1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[xx]]]]]]]]]]]]]]]]]]]]"
#         self.assertEqual(decode_string(deep_nest), "xx")
        
#     def test_original_example(self):
#         # Test the original complex example
#         complex_example = "3[a]2[c]2[p2[x]]ef4[3[a]2[cbb]]"
#         expected = "aaaccppxxxxefaaacbbcbbaaacbbcbbaaacbbcbbaaacbbcbb"
#         self.assertEqual(decode_string(complex_example), expected)


# if __name__ == "__main__":
#     unittest.main()

import unittest

def decode_string(s):
    if not s:
        return ""
        
    stack = []
    curr_str = ""
    curr_num = 0
    
    for char in s:
        if char.isdigit():
            curr_num = curr_num * 10 + int(char)
        elif char == '[':
            # Push current state to stack and reset
            stack.append((curr_str, curr_num))
            curr_str = ""
            curr_num = 0
        elif char == ']':
            # Pop previous state
            prev_str, num = stack.pop()
            # Combine with current state
            curr_str = prev_str + curr_str * num
        else:
            # Just add the character to current string
            curr_str += char
    
    return curr_str


class TestStringDecoding(unittest.TestCase):
    
    def test_basic_cases(self):
        # Basic test cases
        self.assertEqual(decode_string("3[a]2[bc]"), "aaabcbc")
        self.assertEqual(decode_string("3[a2[c]]"), "accaccacc")
        self.assertEqual(decode_string("2[abc]3[cd]ef"), "abcabccdcdcdef")
        
    def test_single_letter_repetition(self):
        # Test single letter repetition
        self.assertEqual(decode_string("10[a]"), "aaaaaaaaaa")
        self.assertEqual(decode_string("1[a]"), "a")
        
    def test_nested_patterns(self):
        # Test more complex nested patterns - ADJUSTED EXPECTATION
        self.assertEqual(decode_string("2[a3[b]c]"), "abbbcabbc")
        self.assertEqual(decode_string("4[xy]z3[a]"), "xyxyxyxyzaaa")
        self.assertEqual(decode_string("3[a]2[b4[c]d]"), "aaabccccdbccccd")
        
    def test_edge_cases(self):
        # Test edge cases - ADJUSTED EXPECTATION
        self.assertEqual(decode_string(""), "")
        self.assertEqual(decode_string("abc"), "abc")  # No brackets
        self.assertEqual(decode_string("3[a]2[b4[c]d]ef"), "aaabccccdbccccdef")  # With trailing characters
        
    def test_complex_examples(self):
        # Test more complex examples
        self.assertEqual(decode_string("2[3[a]b]1[cd]"), "aaabaaabcd")
        self.assertEqual(decode_string("3[z]2[2[y]pq4[2[jk]e1[f]]]"), 
                         "zzz" + 2 * ("yypq" + 4 * ("jkjkef")))
        
    def test_deep_nesting(self):
        # Test with multiple levels of nesting
        self.assertEqual(decode_string("1[1[1[a]]]"), "a")
        
        # A more challenging deep nesting case
        deep_nest = "1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[xx]]]]]]]]]]]]]]]]]]]]"
        self.assertEqual(decode_string(deep_nest), "xx")
        
    def test_original_example(self):
        # Test the original complex example - ADJUSTED EXPECTATION
        complex_example = "3[a]2[c]2[p2[x]]ef4[3[a]2[cbb]]"
        # Your algorithm produces this output, which is actually correct per the rules:
        expected = "aaaccpxxpxxefaaacbbcbbaaacbbcbbaaacbbcbbaaacbbcbb"
        self.assertEqual(decode_string(complex_example), expected)


if __name__ == "__main__":
    unittest.main()