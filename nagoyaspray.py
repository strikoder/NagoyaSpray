#!/usr/bin/env python3

import argparse
from datetime import datetime

# ASCII Art Banner
BANNER = """
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   ███╗   ██╗ █████╗  ██████╗  ██████╗ ██╗   ██╗ █████╗        ║
║   ████╗  ██║██╔══██╗██╔════╝ ██╔═══██╗╚██╗ ██╔╝██╔══██╗       ║
║   ██╔██╗ ██║███████║██║  ███╗██║   ██║ ╚████╔╝ ███████║       ║
║   ██║╚██╗██║██╔══██║██║   ██║██║   ██║  ╚██╔╝  ██╔══██║       ║
║   ██║ ╚████║██║  ██║╚██████╔╝╚██████╔╝   ██║   ██║  ██║       ║
║   ╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝   ╚═╝  ╚═╝       ║
║                                                               ║
║              ███████╗██████╗ ██████╗  █████╗ ██╗   ██╗        ║
║              ██╔════╝██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝        ║
║              ███████╗██████╔╝██████╔╝███████║ ╚████╔╝         ║
║              ╚════██║██╔═══╝ ██╔══██╗██╔══██║  ╚██╔╝          ║
║              ███████║██║     ██║  ██║██║  ██║   ██║           ║
║              ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝           ║
║                                                               ║
║                Developed by Strikoder | v1.1                  ║
║          Lightweight Wordlist Generator for Pentesting        ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
"""

# Base word lists (all lowercase)
MONTHS = [
    "january", "february", "march", "april", "may", "june",
    "july", "august", "september", "october", "november", "december"
]

SEASONS = ["winter", "spring", "summer", "autumn", "fall"]

DAYS = [
    "monday", "tuesday", "wednesday", "thursday", 
    "friday", "saturday", "sunday"
]

COMMON = ["welcome", "password", "company", "access"]


def capitalize_first_only(word):
    return word[0].upper() + word[1:].lower() if word else word


def capitalize_last_only(word):
    return word[:-1].lower() + word[-1].upper() if word else word


def generate_passwords(word_lists, years, attributes, position, cap_mode, min_length, max_length):
    passwords = set()
    
    # Combine all selected word lists
    all_words = []
    for word_list in word_lists:
        all_words.extend(word_list)
    
    year_start, year_end = years
    
    for word in all_words:
        for year in range(year_start, year_end + 1):
            # Full year
            year_str = str(year)
            # Short year (last 2 digits)
            year_short = str(year)[-2:]
            
            for y in [year_str, year_short]:
                # Base combination: word + year
                base = f"{word}{y}"
                
                # Apply capitalization (default is 'first')
                if cap_mode == 'first':
                    base = capitalize_first_only(base)
                elif cap_mode == 'last':
                    base = capitalize_last_only(base)
                elif cap_mode == 'lower':
                    base = base.lower()
                elif cap_mode == 'upper':
                    base = base.upper()
                elif cap_mode == 'all':
                    # Add multiple variations
                    variations = [
                        base.lower(),
                        base.upper(),
                        capitalize_first_only(base),
                        capitalize_last_only(base)
                    ]
                    for var in variations:
                        # Add with attributes
                        for attr in attributes:
                            if attr == '':
                                candidate = var
                            elif position == 'p':
                                candidate = f"{attr}{var}"
                            elif position == 's':
                                candidate = f"{var}{attr}"
                            elif position == 'b':
                                candidate = f"{attr}{var}{attr}"
                            
                            # Check length constraints
                            if min_length <= len(candidate) <= max_length:
                                passwords.add(candidate)
                    continue
                
                # Add with attributes based on position
                for attr in attributes:
                    if attr == '':
                        candidate = base
                    elif position == 'p':
                        candidate = f"{attr}{base}"
                    elif position == 's':
                        candidate = f"{base}{attr}"
                    elif position == 'b':
                        candidate = f"{attr}{base}{attr}"
                    
                    # Check length constraints
                    if min_length <= len(candidate) <= max_length:
                        passwords.add(candidate)
    
    return sorted(passwords)


def main():
    parser = argparse.ArgumentParser(
        description='Simple Password Spray List Generator',
        epilog='\nExample: python3 nagoyaspray.py --seasons --months --start 2020 --end 2025 -s "!" -o passwords.txt'
    )
    
    # Word list selection
    parser.add_argument('--months', action='store_true', help='Include months')
    parser.add_argument('--seasons', action='store_true', help='Include seasons')
    parser.add_argument('--days', action='store_true', help='Include days of week')
    parser.add_argument('--common', action='store_true', help='Include common words')
    parser.add_argument('--all', action='store_true', help='Include all word types')
    parser.add_argument('-w', '--words', type=str, help='Custom comma-separated words')
    
    # Year range
    parser.add_argument('--start', type=int, help='Start year (default: current year)')
    parser.add_argument('--end', type=int, help='End year (default: current year)')
    
    # Attributes
    parser.add_argument('-p', '--prefix', type=str, default='', 
                       help='Comma-separated prefixes to add at START (e.g., "!,@,#")')
    parser.add_argument('-s', '--suffix', type=str, default='',
                       help='Comma-separated suffixes to add at END (e.g., "!,123")')
    parser.add_argument('-b', '--both-attr', type=str, default='',
                       help='Comma-separated attributes to add at BOTH start and end (e.g., "!")')
    
    # Length constraints
    parser.add_argument('--min', type=int, default=1, 
                       help='Minimum password length (default: 1)')
    parser.add_argument('--max', type=int, default=100, 
                       help='Maximum password length (default: 100)')
    
    # Capitalization
    parser.add_argument('--cap', choices=['first', 'last', 'lower', 'upper', 'all'], 
                       default='first',
                       help='Capitalization mode: first=First letter capitalized (default), lower=all lowercase, upper=all uppercase, last=last letter capitalized, all=all variations')
    
    # Output
    parser.add_argument('-o', '--output', type=str, help='Output file (required unless --print is used)')
    parser.add_argument('--print', action='store_true', help='Print to stdout instead of file')
    
    args = parser.parse_args()
    
    # Print banner
    print(BANNER)
    
    # Validate output requirement
    if not args.print and not args.output:
        print("[!] Error: Output file required (-o) unless --print is specified")
        print("\nExample: python3 nagoyaspray.py --seasons --months --start 2020 --end 2025 -s \"!\" -o passwords.txt")
        return
    
    # Validate length constraints
    if args.min > args.max:
        print("[!] Error: Minimum length cannot be greater than maximum length")
        return
    
    # Set default years
    current_year = datetime.now().year
    year_start = args.start if args.start else current_year
    year_end = args.end if args.end else current_year
    
    # Select word lists
    word_lists = []
    if args.all:
        word_lists = [MONTHS, SEASONS, DAYS, COMMON]
    else:
        if args.months:
            word_lists.append(MONTHS)
        if args.seasons:
            word_lists.append(SEASONS)
        if args.days:
            word_lists.append(DAYS)
        if args.common:
            word_lists.append(COMMON)
    
    # Add custom words
    if args.words:
        custom_words = [w.strip().lower() for w in args.words.split(',')]
        word_lists.append(custom_words)
    
    if not word_lists:
        print("[!] Error: No word lists selected. Use --months, --seasons, --days, --common, or --all")
        return
    
    # Determine which attribute flag was used
    attributes = []
    position = None
    
    if args.prefix:
        attributes = [s.strip() for s in args.prefix.split(',')]
        position = 'p'
    elif args.suffix:
        attributes = [s.strip() for s in args.suffix.split(',')]
        position = 's'
    elif args.both_attr:
        attributes = [s.strip() for s in args.both_attr.split(',')]
        position = 'b'
    else:
        attributes = ['']
        position = 's'
    
    print(f"[*] Generating passwords...")
    print(f"[*] Year range: {year_start}-{year_end}")
    print(f"[*] Attributes: {attributes if attributes != [''] else 'None'}")
    print(f"[*] Position: {'PREFIX (start)' if position == 'p' else 'SUFFIX (end)' if position == 's' else 'BOTH'}")
    print(f"[*] Capitalization: {args.cap}")
    print(f"[*] Length range: {args.min}-{args.max}")
    
    # Generate passwords
    passwords = generate_passwords(
        word_lists=word_lists,
        years=(year_start, year_end),
        attributes=attributes,
        position=position,
        cap_mode=args.cap,
        min_length=args.min,
        max_length=args.max
    )
    
    print(f"[+] Generated {len(passwords)} unique passwords")
    
    # Output
    if args.output:
        with open(args.output, 'w') as f:
            for pwd in passwords:
                f.write(pwd + '\n')
        print(f"[+] Saved to {args.output}")
    
    if args.print:
        for pwd in passwords:
            print(pwd)


if __name__ == '__main__':
    main()
