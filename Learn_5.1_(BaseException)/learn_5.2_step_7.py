"""В программе вводятся в одну строчку через пробел некоторые данные, например:

"1 -5.6 2 abc 0 False 22.5 hello world"
Эти данные разбиваются по пробелу и представляются в виде списка строк:

lst_in = input().split()
Ваша задача посчитать сумму всех целочисленных значений, присутствующих в списке lst_in. Результат (сумму) вывести на
экран."""


lst_in = input().split()

print(sum([int(x) for x in lst_in if x.strip('-').isdigit()]))
