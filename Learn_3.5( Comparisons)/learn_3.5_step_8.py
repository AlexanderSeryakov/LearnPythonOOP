class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money):
        money.cb = cls


class MoneyR:
    def __init__(self, volume=0):
        self.volume = volume
        self.cb = None

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb):
        self.__cb = cb

    def __eq__(self, other):
        if self.cb:
            if isinstance(other, MoneyD):
                return round(other.volume, 1) == round(self.volume/self.cb.rates['rub'], 1)
            if isinstance(other, MoneyE):
                return round(other.volume / other.cb.rates['euro']) == round(self.volume/self.cb.rates['rub'], 1)
            else:
                return round(other.volume, 1) == round(self.volume, 1)
        raise ValueError("Неизвестен курс валют.")

    def __gt__(self, other):
        if self.cb:
            if isinstance(other, MoneyD):
                return round(other.volume, 1) < round(self.volume/self.cb.rates['rub'], 1)
            if isinstance(other, MoneyE):
                return round(other.volume / other.cb.rates['euro']) < round(self.volume/self.cb.rates['rub'], 1)
            else:
                return round(other.volume, 1) < round(self.volume, 1)
        raise ValueError("Неизвестен курс валют.")

    def __ge__(self, other):
        if self.cb:
            if isinstance(other, MoneyD):
                return round(other.volume, 1) <= round(self.volume / self.cb.rates['rub'], 1)
            if isinstance(other, MoneyE):
                return round(other.volume / other.cb.rates['euro']) <= round(self.volume / self.cb.rates['rub'], 1)
            else:
                return round(other.volume, 1) <= round(self.volume, 1)
        raise ValueError("Неизвестен курс валют.")


class MoneyD:
    def __init__(self, volume=0):
        self.volume = volume
        self.cb = None

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb):
        self.__cb = cb

    def __eq__(self, other):
        if self.cb:
            if isinstance(other, MoneyR):
                return round(other.volume/other.cb.rates['rub']) == round(self.volume, 1)
            if isinstance(other, MoneyE):
                return round(other.volume / other.cb.rates['euro']) == round(self.volume, 1)
            else:
                return round(other.volume, 1) == round(self.volume, 1)
        raise ValueError("Неизвестен курс валют.")

    def __gt__(self, other):
        if self.cb:
            if isinstance(other, MoneyR):
                return round(other.volume/other.cb.rates['rub']) < round(self.volume, 1)
            if isinstance(other, MoneyE):
                return round(other.volume / other.cb.rates['euro']) < round(self.volume, 1)
            else:
                return round(other.volume, 1) < round(self.volume, 1)
        raise ValueError("Неизвестен курс валют.")

    def __ge__(self, other):
        if self.cb:
            if isinstance(other, MoneyR):
                return round(other.volume / other.cb.rates['rub']) <= round(self.volume, 1)
            if isinstance(other, MoneyE):
                return round(other.volume / other.cb.rates['euro']) <= round(self.volume, 1)
            else:
                return round(other.volume, 1) <= round(self.volume, 1)
        raise ValueError("Неизвестен курс валют.")


class MoneyE:
    def __init__(self, volume=0):
        self.volume = volume
        self.cb = None

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb):
        self.__cb = cb

    def __eq__(self, other):
        if self.cb:
            if isinstance(other, MoneyR):
                return round(other.volume/other.cb.rates['rub'], 1) == round(self.volume/self.cb.rates['euro'])
            if isinstance(other, MoneyD):
                return round(other.volume, 1) == round(self.volume / self.cb.rates['euro'])
            else:
                return round(other.volume, 1) == round(self.volume)

    def __gt__(self, other):
        if self.cb:
            if isinstance(other, MoneyR):
                return round(other.volume/other.cb.rates['rub'], 1) < round(self.volume/self.cb.rates['euro'])
            if isinstance(other, MoneyD):
                return round(other.volume, 1) < round(self.volume / self.cb.rates['euro'])
            else:
                return round(other.volume, 1) < round(self.volume)
        raise ValueError("Неизвестен курс валют.")

    def __ge__(self, other):
        if self.cb:
            if isinstance(other, MoneyR):
                return round(other.volume / other.cb.rates['rub'], 1) <= round(self.volume / self.cb.rates['euro'])
            if isinstance(other, MoneyD):
                return round(other.volume, 1) <= round(self.volume / self.cb.rates['euro'])
            else:
                return round(other.volume, 1) <= round(self.volume, 1)
        raise ValueError("Неизвестен курс валют.")


dl = MoneyD(100)
rb = MoneyR(100)
er = MoneyE(100)

CentralBank.register(dl)
CentralBank.register(rb)
CentralBank.register(er)

print(er > rb)
