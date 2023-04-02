# Модуль книги рецептов
class Cook_book:
    def __init__(self):
        self._c_b = {}
    def get_recipes(self, file_path):
        with open(file_path, "r", encoding= 'utf-8') as f:
            for line in f:
                name = line.strip()
                list_of_ingr = []
                count = int(f.readline().strip())
                for _ in range(count):
                    ingredient_name, quantity, measure = f.readline().strip().split('|')
                    list_of_ingr += [{'ingredient_name':ingredient_name, 'quantity':quantity, 'measure':measure}]
                self._c_b[name] = list_of_ingr
                f.readline()

    def get_shop_list_by_dishes(self, dishes, person_count):
        s_ingr = []
        vivod = {}
        for i in dishes:
            s_ingr += self._c_b[i]
        for j in s_ingr:
            if j['ingredient_name'] in vivod:
                vivod[j['ingredient_name']]['quantity'] += int(j['quantity']) * person_count
            else:
                vivod[j['ingredient_name']] = {'measure': j['measure'], 'quantity': int(j['quantity']) * person_count}
        return vivod

    def __str__(self) ->str:
        str = ''
        for key,val in self._c_b.items():
            str += f'_______________\nБлюдо: {key}\n--------------------'
            for ing in val:
                str += f'\n{ing["ingredient_name"]} - {ing["quantity"]}{ing["measure"]}'
            str+= '\n__________________'
        return str
         
   
c_b_1 = Cook_book()
c_b_1.get_recipes(file_path = "./recipes.txt")
print(c_b_1)
print(c_b_1.get_shop_list_by_dishes(['Запеченный картофель','Омлет'], 2))



    


