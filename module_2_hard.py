import random
def generate_password(n):
    password = ""
    for i in range(1, 21):
        for j in range(i, 21):
            pair_sum = i + j
            if n % pair_sum == 0:
                password += f"{i}{j}"
    return password
n = random.randint(3, 20)
result = generate_password(n)
print(f"Первое число: {n}")
print(f"Нужный пароль: {result}")

