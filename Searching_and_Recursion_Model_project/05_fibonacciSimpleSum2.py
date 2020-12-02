"""
For a given positive integer n determine if it can be represented as a sum of two Fibonacci numbers (possibly equal).

Example

For n = 1, the output should be
fibonacciSimpleSum2(n) = true.

Explanation: 1 = 0 + 1 = F0 + F1.

For n = 11, the output should be
fibonacciSimpleSum2(n) = true.

Explanation: 11 = 3 + 8 = F4 + F6.

For n = 60, the output should be
fibonacciSimpleSum2(n) = true.

Explanation: 11 = 5 + 55 = F5 + F10.

For n = 66, the output should be
fibonacciSimpleSum2(n) = false.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
1 ≤ n ≤ 2 · 109.

[output] boolean

true if n can be represented as Fi + Fj, false otherwise.

"""
def fibonacciSimpleSum2(n):
    
    fib_prev = 0
    fib_curr = 1
    fibonaciNumbers = set()
    fibonaciNumbers.add(fib_prev)
    fibonaciNumbers.add(fib_curr)
    
    while fib_curr < n:
        sum = fib_curr + fib_prev
        fibonaciNumbers.add(sum)
        fib_prev = fib_curr
        fib_curr = sum
        
    print(fibonaciNumbers)
    for i in fibonaciNumbers:
        print(i, n-i)
        if i in fibonaciNumbers and (n - i) in fibonaciNumbers:
            return True
    return False

    
