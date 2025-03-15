def fibonacci(n):
    sequence = [0, 1]
    for _ in range(n - 2):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

print("I primi 10 numeri della sequenza di Fibonacci sono:")
print(fibonacci(10))
