def reverse_count(n):
    if n < 1:
        return
    print(n)
    reverse_count(n - 1)
reverse_count(5)
