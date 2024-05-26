def tinh_tong(a, b): #Biến là một primitive value
    a += 5
    b += 10
    return a + b

x = 10
y = 20

tong = tinh_tong(x, y)
print('x', x)
print('y', y)

print('Tổng =', tong)


lst_item = [1,2,3]

def add_item(lst, new_item): #Địa chỉ là một reference value
    new_list = lst.copy()
    new_list.append(new_item)
    return new_list

print('list method', add_item(lst_item, 5))
print('list_item', lst_item)