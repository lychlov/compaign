class Solution():
    def dead_lock_check(self, l, r, w):
        state_set = set()
        current = 0
        state_set.add(0)
        status = 'w'
        status_detail = {'w': w, 'r': 0 - r}
        while True:
            # 缓冲区变化
            current = current + status_detail[status]
            if current > l or current < 0:
                return 'Yes'
            # 读写状态变化
            if status == 'w' and current + w > l:
                status = 'r'
            elif status == 'r' and current - r < 0:
                status = 'w'
            if current in state_set:
                return 'No'
            state_set.add(current)


# sol = Solution()
# print(sol.dead_lock_check(8, 6, 5))

if __name__ == '__main__':
    path = r'/Users/zhikuncheng/PycharmProjects/compaign/2019/04-死锁/{}.txt'
    with open(path.format('in'), 'r') as in_strs:
        with open(path.format('out'), 'w',
                  encoding='utf-8') as out_file:
            for in_str in in_strs.readlines():
                in_str = in_str.strip()
                nums = in_str.split(' ')
                l = int(nums[0])
                r = int(nums[1])
                w = int(nums[2])
                sol=Solution()
                out_str=sol.dead_lock_check(l,r,w)
                print(out_str)
                out_file.write('%s\n' % (out_str))


