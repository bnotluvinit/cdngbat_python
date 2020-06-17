class WarmUp1:
    @staticmethod
    def sleep_in(weekday, vacation):
        if not weekday or vacation:
            return True
        else:
            return False

    @staticmethod
    def monkey_trouble(a_smile, b_smile):
        return a_smile == b_smile

    @staticmethod
    def sum_trouble(a, b):
        sum = a + b
        if a == b:
            sum = sum * 2
        return sum

    @staticmethod
    def diff21(n):
        if n <= 21:
            return 21 - n
        else:
            return (n - 21) * 2

    @staticmethod
    def parrot_trouble(talking, hour):
        return talking and (hour < 7 or hour > 20)

    @staticmethod
    def makes10(a, b):
        return a == 10 or b == 10 or a + b == 10

    @staticmethod
    def near_hundred(n):
        return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)

    @staticmethod
    def pos_nes(a, b, negative):
        if negative:
            return a < 0 and b < 0
        else:
            return (a < 0 and b > 0) or (a > 0 and b < 0)

    @staticmethod
    def not_string(str):
        if len(str) >= 3 and str[:3] == 'not':
            return str
        return 'not ' + str

    @staticmethod
    def missing_char(str, n):
        front = str[:n]
        back = str[n + 1:]

        return front + back

    @staticmethod
    def front_back(str):
        if len(str) <= 1:
            return str
        mid = str[1:len(str) - 1]
        return str[len(str) - 1] + mid + str[0]

    @staticmethod
    def front3(str):
        if len(str) <= 3:
            return str + str + str
        else:
            return str[0:3] + str[0:3] + str[0:3]

