if __name__ == '__main__':
    numbers = []
    while len(numbers) < 3:
        number = input()
        try:
            number = int(number)
            numbers.append(number)
        except Exception as e:
            print(e)
    numbers.sort()
    for i in numbers:
        print(i)

