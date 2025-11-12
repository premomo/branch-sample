#1. 둘 다 지운다.
#2. 둘을 중재하여 타협한다.
#3. 둘 중 하나를 고른다.

# -> 어떻게 하든 내가 원하는 최종단계의 코드를 만들어내야한다.
for j in range(4, 45+1):
    if j % 15 == 0:
        print('fizzbuzz')
    elif j % 3 == 0:
        print('fizz')
    elif j % 5 == 0:
        print('buzz')
    else:
        print(j)
