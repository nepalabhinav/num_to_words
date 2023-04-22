"""Has a function 'num_to_words'"""


def num_to_words(num: int, mode: str = 's'):
    """Takes [num:int, mode]. Try mode = 'h' for Hindu arabic system. If the given num:int is more than
    -99999999999999 and less than 100000000000000, will return words:str to represent the number in words,
    else will return False"""

    if -99999999999999 < num < 100000000000000:
        if mode != 's' and mode != 'h':
            mode = 's'

        if mode == 's':
            gap = 1000
            system = {
                1000: ' thousand',
                1000000: ' million',
                1000000000: ' billion',
                1000000000000: ' trillion'
            }

        if mode == 'h':
            gap = 100
            system = {
                1000: ' thousand',
                100000: ' lakh',
                10000000: ' karod',
                1000000000: ' arab',
                100000000000: ' kharab',
                10000000000000: ' neel'
            }

        num_pos = abs(num)  # get positive form of number if the number is negative
        num_len = len(list(str(num_pos)))  # get length of str(num_pos)

        def for_1d(n):
            base = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
            return base[n]

        def for_2d(n):
            tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
            if n % 10 == 0:
                return tens[int(n / 10)]
            else:
                if 10 < n < 20:
                    list1 = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
                             'eighteen', 'nineteen']
                    return list1[int(n - 10)]
                elif n < 100:
                    if tens[int(n / 10)] != '':
                        return tens[int(n / 10)] + '-' + for_1d(int(n % 10))
                    elif tens[int(n / 10)] == '':
                        return for_1d(int(n % 10))

        def for_3d(n):
            list1 = ['', 'one hundred', 'two hundred', 'three hundred', 'four hundred', 'five hundred', 'six hundred',
                     'seven hundred', 'eight hundred', 'nine hundred']
            x = list1[int(n / 100)]
            y = n % 100
            if n % 100 == 0:
                return x
            else:
                if x != '':
                    return x + ' ' + for_2d(y)
                elif x == '':
                    return for_2d(y)

        def for_md(n, index):
            dict1 = system
            list1 = ['']
            if mode == 's':
                for i in range(1, 999):
                    list1.append(for_3d(i) + dict1[index])
            if mode == 'h':
                for i in range(1, 99):
                    list1.append(for_2d(i) + dict1[index])
            x = list1[int(n / index)]
            y = n % index
            if y == 0:
                return x
            else:
                if index == 1000:
                    return x + ' ' + for_3d(y)
                elif index <= 1000000000000:
                    return x + ' ' + for_md(y, index / gap)

        def get_words():
            if num_len == 1:
                return for_1d(num_pos)
            elif num_len == 2:
                return for_2d(num_pos)
            elif num_len == 3:
                return for_3d(num_pos)
            else:
                if mode == 's':
                    return for_md(num_pos, pow(10, num_len - num_len % 3))
                if mode == 'h':
                    return for_md(num_pos, pow(10, num_len - (num_len - 3) % 2))

        if num < 0:
            return 'Minus ' + get_words()

        return get_words().capitalize()

    else:
        return False
