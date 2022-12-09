class MaxPooling:
    def __init__(self, step=(2, 2), size=(2,2)):
        self.step = step
        self.size = size

    def __call__(self, matrix, *args, **kwargs):
        for string in matrix:
            for elem in string:
                if type(elem) not in (int, float):
                    raise ValueError("Неверный формат для первого параметра matrix.")
