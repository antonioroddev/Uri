def fibbonacci(n):
    if n <= 1:
        return 1
    return fibbonacci(n-1) + fibbonacci(n-2)
    

partir_30 = [2584,4181,6765,10946,17711,28657,46368,75025,121393,196418,317811,514229,832040,1346269,2178309,3524578,5702887,9227465,14930352,24157817,39088169,63245986,102334155,165580141]

while True:
    n = input()
    if n == '0':
        break
    if int(n) >= 17:
        print(partir_30[int(n)-17])
    else:    
        print(fibbonacci(int(n)))
