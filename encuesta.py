def get_age_input():
    while True:
        try:
            age = int(input("Por favor, ingresa tu edad: "))
            if age < 0:
                print("La edad no puede ser negativa. Inténtalo de nuevo.")
            else:
                return age
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

def categorize_age(age):
    if age < 18:
        return "Eres menor de edad."
    elif age < 65:
        return "Eres adulto."
    else:
        return "Eres mayor de edad."

def main():
    age = get_age_input()
    result = categorize_age(age)
    print(result)

if __name__ == "__main__":
    main()
