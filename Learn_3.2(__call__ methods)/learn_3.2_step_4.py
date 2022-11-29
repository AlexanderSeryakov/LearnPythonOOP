from string import ascii_lowercase, digits


class LengthValidator:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, string, *args, **kwargs):
        return self.min_length <= len(str(string)) <= self.max_length


class CharsValidator:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, string, *args, **kwargs):
        return all(map(lambda x: x in self.chars, string))


admissible_char = ascii_lowercase + digits
lv = LengthValidator(5, 20)  # min_length - минимально допустимая длина; max_length - максимально допустимая длина
cv = CharsValidator(admissible_char)  # chars - строка из допустимых символов

login_check_len = lv('xui42@bkru')
login_check_char = cv('xui42bkru')

print(login_check_len, login_check_char, sep='\n')
