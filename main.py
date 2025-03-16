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
        return [prefix + suffix]  # If prefix + suffix exceeds the limit, only check this single word
    
    return (prefix + "".join(combo) + suffix for combo in itertools.product(characters, repeat=remaining_length))

def check_github_username(username):
    url = f"https://github.com/{username}"
    response = requests.get(url)
    
    if response.status_code == 404:
        return True  # Available
    
    soup = BeautifulSoup(response.text, "html.parser")
    label = soup.find("label", {"for": "not-found-search"})
    return label is not None  # If the label exists, the name is available

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py {number_of_characters} {prefix} {suffix} [-a for letters] [-1 for numbers]")
        return
    
    length = int(sys.argv[1])
    prefix = sys.argv[2] if len(sys.argv) > 2 and sys.argv[2] not in ["-a", "-1"] else ""
    suffix = sys.argv[3] if len(sys.argv) > 3 and sys.argv[3] not in ["-a", "-1"] else ""
    
    use_letters = "-a" in sys.argv
    use_numbers = "-1" in sys.argv
    
    if not use_letters and not use_numbers:
        print("Error: You must select at least letters (-a) or numbers (-1).")
        return
    
    print("Checking usernames... Please wait.")
    available_names = []
    
    for name in generate_names(length, use_letters, use_numbers, prefix, suffix):
        is_available = check_github_username(name)
        status = "Available" if is_available else "Unavailable"
        print(f"Testing: {name} -> {status}")
        
        if is_available:
            available_names.append(name)
    
    print("\nSearch completed!")
    print("Available usernames:", available_names)

if __name__ == "__main__":
    main()
