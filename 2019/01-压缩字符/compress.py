class Solution:
    """
    @param str: a string
    @return: a compressed string
    """
    def compress(self, str):
        # write your code here
        if not str:
            return str
        ret = [str[0]]
        prev_c = str[0]
        count = 0
        for i in range(1, len(str)):
            if str[i] == prev_c:
                count += 1
            else:
                ret.append('%d' % count)
                prev_c = str[i]
                ret.append(prev_c)
                count = 0
        ret.append('%d' % count)
        # ret = ''.join(ret)
        return ret

# easy: http://lintcode.com/zh-cn/problem/string-compression/




if __name__ == '__main__':
    with open(r'/Users/zhikuncheng/PycharmProjects/compaign/2019/01-压缩字符/in.txt', 'r') as in_strs:
        with open(r'/Users/zhikuncheng/PycharmProjects/compaign/2019/01-压缩字符/out.txt', 'w', encoding='utf-8') as out_file:

            for in_str in in_strs.readlines():
                in_str=in_str.strip()
                print(in_str)
                sol = Solution()
                result = sol.compress(in_str)
                ret = []
                for i in range(0, len(result), 2):
                    if result[i + 1] != '0':
                        ret.append(result[i + 1])
                    ret.append(result[i])
                out_str = ''.join(ret)
                out_file.write('%s\n' % (out_str))





