if __name__ == '__main__':
    with open(r'/Users/zhikuncheng/devspace/0828/02/in.txt', 'r') as in_str:
        with open(r'/Users/zhikuncheng/devspace/0828/02/out.txt', 'w', encoding='utf-8') as out_file:
            for total in in_str.readlines():
                total = int(total)
                circle = list(range(1, total + 1))
                count = 0
                while len(circle) > 1:
                    length = len(circle)
                    if length > 5:
                        temp_count = 0
                        for i in range(4, length, 5):
                            circle.pop(i - temp_count)
                            temp_count += 1
                        # for i in range(0, length % 5):
                        #     circle.insert(0, circle.pop())
                        circle = circle[-(length % 5):]+circle[0:-(length % 5)]
                    else:
                        temp = circle.pop(0)
                        count += 1
                        if count != 5:
                            circle.append(temp)
                        else:
                            count = 0
                print(circle[0])
                out_file.write('%s\n' % (circle[0]))
