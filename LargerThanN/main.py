#Title: Larger Than n
#Author: Dominic Corneliusen
#Date last modified: 3/5/2026

#Start
def main(list, n):
    greater_than_n = []
    for number in list:
        if number > n:
            greater_than_n.append(number)
    for i in greater_than_n:
        print(i)
array_of_numbers = [1,2,3,4,5,6,7,8,9,10]
n = int(input('Enter a number between one and ten: '))
main(array_of_numbers, n)
