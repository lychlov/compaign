class Solution(object):
    def count_cars(self, target=0, cars=[]):
        count = 0
        reach = []
        while len(cars) > 0:
            # 判断到达
            reach = []
            catch = []
            reach_count = set()

            for car in cars:
                if car[0] >= target:
                    reach.append(car)
            for car_reach in reach:
                reach_count.add((target-(car_reach[0]-car_reach[1]))/car_reach[1])
                cars.remove(car_reach)
            print(reach_count)
            if 0.75 in reach_count:
                print(cars)
            if len(reach) > 0:
                count += len(reach_count)

            for i in range(len(cars) - 1,0,-1):
                if cars[i-1][0] <= cars[i][0]:
                    catch.append(cars[i])
            for car_catch in catch:
                cars.remove(car_catch)
            for i in range(len(cars)):
                cars[i][0] += cars[i][1]

            pass
        return count

    pass


if __name__ == '__main__':
    in_file = open('carfleet.txt', 'r')
    out_file = open('3-carfleet.txt', 'w')
    lines = []
    solution = Solution()
    for line in in_file.readlines():
        if '-' not in line:
            lines.append(line.strip())
            cars = []
            target = 0

        else:
            lines = []
        if len(lines) == 3:
            target = int(lines[0])
            for i in range(len(lines[1].split(','))):
                cars.append([int(lines[1].split(',')[i]), int(lines[2].split(',')[i])])
            cars.sort(reverse=True)
            res= solution.count_cars(target, cars)
            out_file.write(str(res)+'\r\n')

    pass
