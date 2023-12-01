# 1
user_name = input('name: ')
print(f'Hi, {user_name}!')

# 2
a = int(input('Введите оценку: '))
b = int(input('Введите оценку: '))
c = int(input('Введите оценку: '))
print(f'Среднее значение: {(a+b+c)/3}')

# 3
math = int(input('Введите оценку: '))
fiz = int(input('Введите оценку: '))
limit = 80

if math > limit and fiz > limit:
    print('Good')
else:
    print('No Good')


# 4
name = input('Name: ')
age = int(input('Age: '))
email = input('Email: ')

print('user_name:', name)
print('user_age: ', age)
print('user_email ', email)
