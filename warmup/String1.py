class String1:
    @staticmethod
    def hello_name(name):
        return 'Hello ' + name + '!'

    @staticmethod
    def make_abba(a, b):
        return a + b + b + a

    @staticmethod
    def make_tags(tag, word):
        return '<' + tag + '>' + word + '</' + tag + '>'

    @staticmethod
    def make_out_word(out, word):
        return out[:2] + word + out[2:]

    @staticmethod
    def extra_end(str):
        end = str[len(str) - 2:]
        return end + end + end

    @staticmethod
    def first_two(str):
        if len(str) <= 2:
            return str
        else:
            return str[:2]

    @staticmethod
    def first_half(str):
        half = (len(str) // 2)
        return str[:half]

    @staticmethod
    def without_end(str):
        return str[1:len(str) - 1]

    @staticmethod
    def combo_string(a, b):
        if len(a) > len(b):
            return b + a + b
        else:
            return a + b + a

    @staticmethod
    def non_start(a, b):
        return a[1:] + b[1:]

    @staticmethod
    def left2(str):
        return str[2:] + str[0:2]
