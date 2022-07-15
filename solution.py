#Q1
def count_down_iterative(n):
    for i in range(n,-1,-1):
        print(i)

def count_down_recursive(n):
    if n == 0:
        print(n)
        return
    else:
        print(n)
        return count_down_recursive(n-1)

#Q2
def string_reverse(string):
    if len(string) <= 1:
        return string
    else:
        return string[-1] + string_reverse(string[:-1])

#Q3
def sum_digits(num):
    if num // 10 == 0:
        return num
    else:
        return (num % 10) + sum_digits(num // 10)

#Q4
def LCM_iterative(num1, num2):
    for i in range(max(num1,num2),num1*num2 + 1):
        if i % num1 == 0 and i % num2 == 0:
            return i



def LCM_iterative_2(num1, num2):
    cur_lcm, max_num = min(num1, num2), max(num1, num2)
    ctr = 2

    while (cur_lcm <= num1*num2):
        if cur_lcm % max_num == 0:
            return cur_lcm
        cur_lcm = min(num1, num2) * ctr
        ctr+=1
        
#Q5
def gcd_recursive(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcd_recursive(num2, num1 % num2)

def lcm_via_gcd(num1, num2):
    return (num1 * num2) / gcd_recursive(num1, num2)



if __name__ == '__main__':
    import random
    import time

    #count_down_iterative(10)
    #count_down_recursive(12)    
    #print(string_reverse(string_reverse('where is the dog?'))== 'where is the dog?')


    #while(True):
    #    random_num = random.randint(1,99999)
    #    if(sum_digits(random_num) != sum([int(x) for x in str(random_num)])):
    #        print(random_num)


    #random_num_1 = random.randint(1,100000)
    #random_num_2 = random.randint(1,100000)



    #t0 = time.time()

    #LCM_iterative(random_num_1, random_num_2)

    #t1 = time.time()

    #t_delta1 = t1-t0



    #t0 = time.time()

    #LCM_iterative_2(random_num_1, random_num_2)

    #t1 = time.time()

    #t_delta2 = t1-t0



    #print(t_delta1, t_delta2, 'for', random_num_1, random_num_2)

    

    #while(True):

    #    random_num_1 = random.randint(1,1000)

    #    random_num_2 = random.randint(1,1000)

    #    if(LCM_iterative(random_num_1, random_num_2) != LCM_iterative_2(random_num_1, random_num_2)):

    #        print(random_num_1, random_num_2, LCM_iterative(random_num_1, random_num_2),LCM_iterative_2(random_num_1, random_num_2))





    #while(True):

    #    random_num_1 = random.randint(1,1000)

    #    random_num_2 = random.randint(1,1000)

    #    if(LCM_iterative_2(random_num_1, random_num_2) != lcm_via_gcd(random_num_1, random_num_2)):

    #        print(random_num_1, random_num_2,LCM_iterative_2(random_num_1, random_num_2), lcm_via_gcd(random_num_1, random_num_2),LCM_iterative(random_num_1, random_num_2))