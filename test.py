#1부터 50의자연수 중 짝수를 구하는 함수(Python)
def even(nums):
    for i in range(1,nums+1):
        if i % 2 == 0:
            return(i)
