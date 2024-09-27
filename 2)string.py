def count_a(string):
    count = string.lower().count('a')
    if count > 0:
        return f"A letra 'a' aparece {count} vez(es) na string."
    else:
        return "A letra 'a' não está presente na string."

texto = input("Digite uma string: ")
print(count_a(texto))
