class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """

    @staticmethod
    def isValidParentheses(s):
        # write your code here
        stack = []
        pair = {')': '(', '}': '{', ']': '['}
        for c in s.strip():

            if c in pair.keys():
                if stack.pop() != pair[c]:
                    return False
            else:
                stack.append(c)
        return not stack


if __name__ == '__main__':
    with open('sample.txt', 'r') as in_file:
        with open('out1.txt', 'w') as out1_file:
            with open('out2.txt', 'w') as out2_file:
                for line in in_file.readlines():
                    count1 = line.count('{')
                    count2 = line.count('[')
                    count3 = line.count('(')
                    flag = Solution.isValidParentheses(line)
                    out1_file.write('%s %s %s\r\n' % (count1, count2, count3))
                    out2_file.write('true\r\n' if flag else 'false\n')
