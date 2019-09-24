class Soltion():
    def find_once(self, in_str):
        for i in in_str:
            index = in_str.index(i)
            rear = in_str.rindex(i)
            if index == rear:
                return i
            else:
                pass
        return -1



if __name__ == '__main__':
    with open(r'/Users/zhikuncheng/PycharmProjects/compaign/2019/02-找出字符串中第一个只出现一次的字符（20分）/in.txt', 'r') as in_strs:
        with open(r'/Users/zhikuncheng/PycharmProjects/compaign/2019/02-找出字符串中第一个只出现一次的字符（20分）/out.txt', 'w',
                  encoding='utf-8') as out_file:
            for in_str in in_strs.readlines():
                in_str = in_str.strip()
                print(in_str)
                sol = Soltion()
                out_str = sol.find_once(in_str)
                print(out_str)
                out_file.write('%s\n' % (out_str))
