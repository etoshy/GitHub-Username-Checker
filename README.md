# GitHub Username Checker ![Views Counter](https://views-counter.vercel.app/badge?pageId=https%3A%2F%2Fgithub%2Ecom%2Fetoshy%2FGitHub-Username-Checker&leftColor=000000&rightColor=ffffff&type=total&label=Viewers&style=none)

## Description
This project is a Python script that checks the availability of GitHub usernames. It generates name combinations based on user-defined parameters and tests whether the names are available or already in use.

## Technologies Used
- **Language:** Python 3
- **Libraries:**
  - `requests`: To make HTTP requests to GitHub
  - `beautifulsoup4`: To parse HTML pages
  - `itertools`: To generate character combinations

## Prerequisites
Before running the script, ensure you have Python 3 installed and the required libraries. To install them, use:

```bash
pip install requests beautifulsoup4
```

## How to Use
The script can be executed directly from the terminal. The command format is:

```bash
python main.py {number_of_characters} {prefix} {suffix} [-a for letters] [-1 for numbers]
```

### Examples
1. **Check 4-character usernames with the prefix "78kj" and suffix "kj", using letters and numbers:**
   ```bash
   python main.py 4 78kj kj -a -1
   ```

2. **Check 5-character usernames using only letters:**
   ```bash
   python main.py 5 "" "" -a
   ```

3. **Check 6-character usernames using only numbers, with the prefix "12" and suffix "34":**
   ```bash
   python main.py 6 12 34 -1
   ```

If you do not want a prefix or suffix, simply leave it blank (`""`).

## Creator
Project developed by [etoshy](https://github.com/etoshy).
