class Solution:

    def get_largest_number(self, number_str, k):
        n = len(number_str)
        if n == k:
            return 0
        elif k > n:
            k = k % n
        result = ''
        cursor = 0
        ok=n-k
        while k > 0:
            sub_str = number_str[cursor:cursor + k + 1]
            if sub_str:
                digs = str(max([int(j) for j in sub_str]))
            else:
                return number_str[:ok]
            index = sub_str.index(digs)
            number_str = number_str[:cursor] + number_str[cursor + index:]
            cursor += 1

            k = k - index

        return number_str

    pass


if __name__ == '__main__':
    sol = Solution()
    print(sol.get_largest_number('97388640145',19))
    path_to_file = r'/Users/zhikuncheng/PycharmProjects/2019battle' + '/{}.txt'
    with open(path_to_file.format('01-in'), 'r') as in_file:
        with open(path_to_file.format('01-out'), 'w', encoding='utf-8') as out_file:
            while in_file.readable():
                in_line = in_file.readline().strip()
                if not in_line:
                    break
                number = in_line.split(',')[0]
                k = int(in_line.split(',')[1])
                sol = Solution()
                result = sol.get_largest_number(number, k)
                out_file.write("{}\n".format(result))
