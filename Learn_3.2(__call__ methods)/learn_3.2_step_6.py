class RenderList:
    def __init__(self, type_list):
        self.type_list = type_list if type_list in ('ul', 'ol') else 'ul'

    def __call__(self, lst, *args, **kwargs):
        return '\n'.join([f"<{self.type_list}>", *map(lambda x: f"<li>{x}</li>", lst), f"</{self.type_list}>"])

lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("oldfhgdgfhgf")
html = render(lst)
print(html)
