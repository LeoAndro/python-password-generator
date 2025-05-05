import random
import string
import argparse
import sys
import pyperclip

def generate_password(length=12, upper=True, lower=True, digits=True, special=True):
    characters = ''
    mandatory = []
    
    if upper:
        characters += string.ascii_uppercase
        mandatory.append(random.choice(string.ascii_uppercase))
    if lower:
        characters += string.ascii_lowercase
        mandatory.append(random.choice(string.ascii_lowercase))
    if digits:
        characters += string.digits
        mandatory.append(random.choice(string.digits))
    if special:
        characters += string.punctuation
        mandatory.append(random.choice(string.punctuation))

    if not characters:
        print("Error: Pilih setidaknya satu jenis karakter!")
        sys.exit(1)
        
    if length < len(mandatory):
        print(f"Error: Panjang minimum untuk kombinasi ini adalah {len(mandatory)}")
        sys.exit(1)

    password = mandatory + random.choices(characters, k=length - len(mandatory))
    random.shuffle(password)
    
    return ''.join(password)

def main():
    parser = argparse.ArgumentParser(description='Password Generator - by <｜end▁of▁thinking｜>')
    # Perubahan penting di sini (-l untuk length, -L untuk lower)
    parser.add_argument('-l', '--length', type=int, help='Panjang password')
    parser.add_argument('-u', '--upper', action='store_true', help='Sertakan huruf besar')
    parser.add_argument('-L', '--lower', action='store_true', help='Sertakan huruf kecil')  # Diubah ke -L
    parser.add_argument('-d', '--digits', action='store_true', help='Sertakan angka')
    parser.add_argument('-s', '--special', action='store_true', help='Sertakan karakter khusus')
    parser.add_argument('-c', '--copy', action='store_true', help='Salin ke clipboard')
    parser.add_argument('-q', '--quiet', action='store_true', help='Hanya tampilkan password')

    args = parser.parse_args()

    if not any(vars(args).values()):
        print("\n=== Password Generator ===")
        args.length = int(input("Panjang password: ") or 12)
        args.upper = input("Sertakan huruf besar? (y/n): ").lower() == 'y'
        args.lower = input("Sertakan huruf kecil? (y/n): ").lower() == 'y'  # Tetap pakai args.lower
        args.digits = input("Sertakan angka? (y/n): ").lower() == 'y'
        args.special = input("Sertakan karakter khusus? (y/n): ").lower() == 'y'
        args.copy = input("Salin ke clipboard? (y/n): ").lower() == 'y'

    password = generate_password(
        length=args.length or 12,
        upper=args.upper,
        lower=args.lower,  # Tetap sama
        digits=args.digits,
        special=args.special
    )

    if not args.quiet:
        print("\n=== Password yang Dihasilkan ===")
        print(f"Panjang   : {len(password)} karakter")
        print(f"Komposisi : {'✅' if args.upper else '❌'} Huruf Besar")
        print(f"           {'✅' if args.lower else '❌'} Huruf Kecil")  # Tetap sama
        print(f"           {'✅' if args.digits else '❌'} Angka")
        print(f"           {'✅' if args.special else '❌'} Karakter Khusus")
        print("\nPassword:")
    
    print(f"\033[92m{password}\033[0m")

    if args.copy:
        try:
            pyperclip.copy(password)
            if not args.quiet:
                print("\nPassword telah disalin ke clipboard!")
        except Exception as e:
            print("\nGagal menyalin ke clipboard. Pastikan pyperclip terinstall:")

if __name__ == "__main__":
    main()
