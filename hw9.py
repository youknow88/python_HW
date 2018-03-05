snake_style = 'employee_first_name'

lst = snake_style. split('_')
first_part = lst[0].capitalize()
second_part = lst[1].capitalize()
third_part = lst[2].capitalize()
camel_style = first_part + second_part + third_part
print(camel_style)