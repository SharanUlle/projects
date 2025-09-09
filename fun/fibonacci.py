# Fibonacci sequence generator

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

if __name__ == "__main__":
    num = int(input("Enter the number of Fibonacci terms: "))
    print(f"Fibonacci sequence (first {num} terms):")
    print(fibonacci(num))
