import itertools
import string
import requests
import sys
from bs4 import BeautifulSoup

def generate_names(length, use_letters, use_numbers, prefix, suffix):
    characters = ""
    if use_letters:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    
    remaining_length = length - len(prefix) - len(suffix)
    
    if remaining_length < 0:
        return [prefix + suffix]  # Caso o prefixo + sufixo já ultrapasse o limite, apenas verifica essa única palavra
    
    return (prefix + "".join(combo) + suffix for combo in itertools.product(characters, repeat=remaining_length))

def check_github_username(username):
    url = f"https://github.com/{username}"
    response = requests.get(url)
    
    if response.status_code == 404:
        return True  # Disponível
    
    soup = BeautifulSoup(response.text, "html.parser")
    label = soup.find("label", {"for": "not-found-search"})
    return label is not None  # Se a label existir, o nome está disponível

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py {numero_de_caracteres} {prefixo} {sufixo} [-a para letras] [-1 para números]")
        return
    
    length = int(sys.argv[1])
    prefix = sys.argv[2] if len(sys.argv) > 2 and sys.argv[2] not in ["-a", "-1"] else ""
    suffix = sys.argv[3] if len(sys.argv) > 3 and sys.argv[3] not in ["-a", "-1"] else ""
    
    use_letters = "-a" in sys.argv
    use_numbers = "-1" in sys.argv
    
    if not use_letters and not use_numbers:
        print("Erro: Você deve selecionar pelo menos letras (-a) ou números (-1).")
        return
    
    print("Verificando nomes... Aguarde.")
    available_names = []
    
    for name in generate_names(length, use_letters, use_numbers, prefix, suffix):
        is_available = check_github_username(name)
        status = "Disponível" if is_available else "Indisponível"
        print(f"Testando: {name} -> {status}")
        
        if is_available:
            available_names.append(name)
    
    print("\nBusca finalizada!")
    print("Nomes disponíveis:", available_names)

if __name__ == "__main__":
    main()
