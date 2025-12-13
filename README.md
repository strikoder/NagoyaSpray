# NagoyaSpray

![NagoyaSpray](https://github.com/user-attachments/assets/4e727676-aa68-48b7-b8f7-8c7e0c99d7f3)


## The Problem
You're mid-exam - OSCP, PNPT, CPTS, whatever - and you need to spray some passwords. Clock's ticking. Your options suck:
1. **Grab a massive wordlist** - Spray 50k passwords, lock accounts, waste time
2. **Write regex on the spot** - Spend 10 minutes fighting with `sedawkgrep` while your brain rots

Neither option is good when you're already stressed and every minute matters.

## Why I Built This
Hit this exact problem several times, for example: on Nagoya from Proving Grounds. Needed seasonal passwords fast. Started with a quick bash one-liner that worked great for that box.

Then I kept running into the same situation on other machines. Kept rewriting similar regex patterns every time. So I rewrote it in Python. Now it's reusable, no regex required, generates what you need in seconds.

When you need `Winter2024!` or `Spring2024!` during an exam, you shouldn't waste mental energy on wordlist generation. Just run the tool and get back to actually breaking stuff.

## Use Cases
Built with cert labs in mind (OSCP, PNPT, CPTS) but works anywhere you need clean spray lists:
- AD password spraying
- CTF boxes
- Any time you need realistic date-based passwords

## Installation (No requirements needed!!)
**Clone the repo:**
```bash
git clone https://github.com/strikoder/NagoyaSpray.git
cd NagoyaSpray
python3 nagoyaspray.py -h
```

**Or grab the file directly:**
```bash
wget https://raw.githubusercontent.com/strikoder/NagoyaSpray/refs/heads/main/nagoyaspray.py
chmod +x nagoyaspray.py
python3 nagoyaspray.py -h
```

## Usage
![nagoyaspray.py](https://github.com/user-attachments/assets/259dcf00-e1bb-47d5-8ca1-f631320e8ddc)


```bash
# No arguments? See the help
python3 nagoyaspray.py

# Example output
Example: python3 nagoyaspray.py --seasons --months --start 2020 --end 2025 -s "!" -o passwords.txt
```

**Basic Examples:**
```bash
# Seasons + months with suffix (default: first letter capitalized)
python3 nagoyaspray.py --seasons --months --start 2020 --end 2025 -s "!" -o passwords.txt

# All word types with multiple suffixes
python3 nagoyaspray.py --all --start 2023 --end 2024 -s "!,123,@" -o passwords.txt

# Add prefix instead
python3 nagoyaspray.py --months --start 2024 --end 2024 -p "!" -o passwords.txt

# Generate only passwords between 8-12 characters
python3 nagoyaspray.py --seasons --start 2024 --end 2024 -s "!" --min 8 --max 12 -o passwords.txt

# All lowercase passwords (no capitalization)
python3 nagoyaspray.py --months --start 2024 --end 2024 -s "!" --cap lower -o passwords.txt

# Custom words
python3 nagoyaspray.py -w "Company,Admin" --start 2023 --end 2024 -s "!" -o passwords.txt

# Both prefix and suffix
python3 nagoyaspray.py --seasons --start 2024 --end 2024 -b "!" -o passwords.txt
```

**Flags:**
- `--months` - Include months
- `--seasons` - Include seasons  
- `--days` - Include days of the week
- `--common` - Include common words
- `--all` - Include everything
- `-w` - Custom comma-separated words
- `--start` / `--end` - Year range
- `-s` - Suffix (add at end)
- `-p` - Prefix (add at start)
- `-b` - Both (add at start and end)
- `--cap` - Capitalization mode: `first` (default - first letter capitalized), `lower` (all lowercase), `upper` (all uppercase), `last` (last letter capitalized), `all` (all variations)
- `--min` - Minimum password length (default: 1)
- `--max` - Maximum password length (default: 100)
- `-o` - Output file (required)
- `--print` - Print to stdout instead

**Note:** By default, all passwords have their first letter capitalized (e.g., `Winter2024!`). Use `--cap lower` for all lowercase or `--cap upper` for all uppercase.

## Shoutout
Props to [spraygen](https://github.com/3ndG4me/spraygen) for inspiration. This is basically the diet version - same idea, way less calories.

**Key Differences:**
| Feature | spraygen | NagoyaSpray |
|---------|----------|-------------|
| **Dependencies** | Requires external libraries | Zero dependencies - pure Python |
| **Complexity** | 10+ modes, sports teams, iterative keyspaces | Simple and focused - just what you need for an exam/CTF |
| **Capitalization** |  cannot capitalize last letter only | First letter capitalized by default + 5 modes (first, last, lower, upper, all) |
| **Target Use Case** | General purpose with tons of options | Built specifically for quick CTF/exam spraying |
| **Speed** | Heavier and slower | Lightweight and fast - generate in seconds |

---
**v1.1** - Does what it says on the tin.
