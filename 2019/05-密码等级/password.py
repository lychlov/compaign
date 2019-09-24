import re


class Solution():
    def check_password(self, password):
        score = 0
        if len(password) <= 4:
            score += 5
        elif len(password) <= 7:
            score += 10
        else:
            score += 25
        nums = len(re.findall(r'[0-9]', password))
        if nums > 1:
            score += 20
        elif nums > 0:
            score += 10
        else:
            score += 0
        digs = len(re.findall(r'[a-z]', password))
        caps = len(re.findall(r'[A-Z]', password))
        if (digs + caps) == 0:
            score += 0
        elif (digs * caps) == 0:
            score += 10
        else:
            score += 20
        others = len(password) - nums - digs - caps
        if others > 1:
            score += 25
        elif others > 0:
            score += 10
        else:
            score += 0

        if digs * caps * others * nums != 0:
            score += 5
        elif caps * others * nums > 0 or digs * others * nums > 0:
            score += 3
        elif caps * nums > 0 or digs * nums > 0:
            score += 2
        if score >= 90:
            result = 'VERY_SECURE'
        elif score >= 80:
            result = 'SECURE'
        elif score >= 70:
            result = 'VERY_STRONG'
        elif score >= 60:
            result = 'STRONG'
        elif score >= 50:
            result = 'AVERAGE'
        elif score >= 25:
            result = 'WEAK'
        else:
            result = 'VERY_WEAK'
        return result


sol = Solution()
result = sol.check_password('pPPsf133&&&&()')
print(result)

if __name__ == '__main__':
    path = r'/Users/zhikuncheng/PycharmProjects/compaign/2019/05-密码等级/{}.txt'
    with open(path.format('in'), 'r') as in_strs:
        with open(path.format('out'), 'w',
                  encoding='utf-8') as out_file:
            for in_str in in_strs.readlines():
                in_str = in_str.strip()
                print(in_str)
                sol = Solution()
                out_str = sol.check_password(in_str)
                print(out_str)
                out_file.write('%s\n' % (out_str))
