# NagoyaSpray

![nagoya](https://github.com/strikoder/NagoyaSpray/blob/main/Nagoya.jpeg)

## The Problem

You're mid-exam - OSCP, PNPT, CPTS, whatever - and you need to spray some passwords. Clock's ticking. Your options suck:

1. **Grab a massive wordlist** - Spray 50k passwords, lock accounts, waste time
2. **Write regex on the spot** - Spend 10 minutes fighting with `sed`/`awk`/`grep` while your brain rots

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

![nagoyaspray.py](https://github.com/strikoder/NagoyaSpray/blob/main/nagoyaspray.gif)

```bash
# No arguments? See the help
python3 nagoyaspray.py

# Example output
Example: python3 nagoyaspray.py --seasons --months --start 2020 --end 2025 -s "!" -o passwords.txt
```

**Basic Examples:**
```bash
# Seasons + months with suffix
python3 nagoyaspray.py --seasons --months --start 2020 --end 2025 -s "!" -o passwords.txt

# All word types with multiple suffixes
python3 nagoyaspray.py --all --start 2023 --end 2024 -s "!,123,@" -o passwords.txt

# Add prefix instead
python3 nagoyaspray.py --months --start 2024 --end 2024 -p "!" -o passwords.txt

# Add prefix with Capitalization for the first letter
python3 nagoyaspray.py --months --start 2024 --end 2024 -p "!" --cap first -o passwords.txt

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
- `--cap` - Capitalization mode (first, last, normal, all)
- `-o` - Output file (required)
- `--print` - Print to stdout instead


## Shoutout

Props to [spraygen](https://github.com/3ndG4me/spraygen) for inspiration. This is basically the diet version - same idea, way less calories. Key differences: we capitalize words and let you add special characters at the start, end, or both. The thing you actually need for a CTF/exam environment.

---

**v1.0** - Does what it says on the tin.
