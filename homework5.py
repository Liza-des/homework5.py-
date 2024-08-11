immutable_var = 1, 2, "строка", True
print(immutable_var)
#print(immutable_var .replace(' ','*')) - не удалось откорреткировать, содержит неизменяемый тип данных, кортеж содержит ссылку на список, а не сам список.
mutable_list = (["Аптека", "улица"], "фонарь...", 10, "октября", 1912)
print(mutable_list)
mutable_list [0][0] = "Ночь"
print(mutable_list)