def fibonacci_check(n):
    a, b = 0, 1
    fib_sequence = [a, b]
    
    while b < n:
        a, b = b, a + b
        fib_sequence.append(b)
    
    if n in fib_sequence:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."

numero = int(input("Digite um número: "))
print(fibonacci_check(numero))
