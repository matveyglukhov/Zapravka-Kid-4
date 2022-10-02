import Rubles
employees_number = int(input('Введите число сотруднников от 1 до 1000 '))
sum = 0
dist_list = []
price_list = []

for i in range(employees_number):
    dist = int(input('Введите расстояние до дома {0}-го сотрудника: '.format(i+1)))
    dist_list.append(dist)
for i in range(employees_number):
    price = int(input('Введите тариф {0}-го такси:  '.format(i+1)))
    price_list.append(price)
c_distance_list = dist_list[:] 
c_price_list = price_list[:]
index_list_d = []
index_list_p = []
max_distance = 0

for i in range(employees_number):                              
    index = c_distance_list.index(max(c_distance_list))
    index_list_d.append(index)
    c_distance_list[index] = 0
for i in range(employees_number):
    index = c_price_list.index(min(c_price_list))
    index_list_p.append(index)
    c_price_list[index] = 10**10
print('Такси для клиента 1, 2, 3, ...:')

for i in range(employees_number):
    taxi_num = index_list_p[index_list_d.index(i)]
    print(taxi_num+1)
for i in range(employees_number):
    sum += dist_list[index_list_d[i]]*price_list[index_list_p[i]]
print(sum)

print('Необходимо заплатить:')
Rubles.out(sum)