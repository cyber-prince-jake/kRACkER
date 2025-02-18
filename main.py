import argparse
import os
from rich.console import Console
from modules.brute_force import brute_force_attack  # ✅ Added Brute Force module
from modules.dictionary_attack import dictionary_attack  # Ensure this exists
from modules.hybrid_attack import hybrid_attack
from modules.rainbow_attack import rainbow_attack
from modules.multi_thread_brute import multi_thread_brute_force_attack


console = Console()

def banner():
    console.print(r"""
[bold red]    
██   ██ ██████  ██████   █████   ██████  ██   ██ ███████ ██████  
██   ██ ██   ██ ██   ██ ██   ██ ██       ██   ██ ██      ██   ██ 
███████ ██████  ██████  ███████ ██   ███ ███████ █████   ██████  
██   ██ ██      ██      ██   ██ ██    ██ ██   ██ ██      ██   ██ 
██   ██ ██      ██   ██  ██████  ██   ██ ███████ ██   ██ 

[/bold red][bold cyan]kRACkER - Advanced Password Cracker 🚀[/bold cyan]
    """, style="bold yellow")

def parse_arguments():
    parser = argparse.ArgumentParser(description="kRACkER - Advanced Password Cracker")

    parser.add_argument("-m", "--mode", choices=["brute", "dict", "hybrid", "rainbow", "multithread"],
                        required=True, help="Choose attack mode: brute, dict, hybrid, rainbow, or multithread")
    
    parser.add_argument("-t", "--target", required=True, help="Target hash to crack")
    
    parser.add_argument("-w", "--wordlist", help="Path to wordlist (for dictionary & hybrid attack)")

    # New: Select hash algorithm (default md5)
    parser.add_argument("-a", "--algorithm", choices=["md5", "sha256", "bcrypt"],
                        default="md5", help="Hash algorithm to use (default: md5)")
    
    return parser.parse_args()


if __name__ == "__main__":
    banner()
    args = parse_arguments()

    console.print(f"[bold yellow]🛠 Selected Mode:[/bold yellow] [cyan]{args.mode}[/cyan]")
    console.print(f"[bold yellow]🎯 Target Hash:[/bold yellow] [cyan]{args.target}[/cyan]")
    console.print(f"[bold yellow]🔑 Algorithm:[/bold yellow] [cyan]{args.algorithm}[/cyan]")

    if args.mode == "brute":
        brute_force_attack(args.target, hash_type=args.algorithm)
    elif args.mode == "dict":
        if not args.wordlist or not os.path.exists(args.wordlist):
            console.print("[bold red]❌ Error:[/bold red] Wordlist file not found!")
        else:
            console.print(f"[bold yellow]📜 Using Wordlist:[/bold yellow] [cyan]{args.wordlist}[/cyan]")
            dictionary_attack(args.target, args.wordlist, hash_type=args.algorithm)
    elif args.mode == "hybrid":
        if not args.wordlist or not os.path.exists(args.wordlist):
            console.print("[bold red]❌ Error:[/bold red] Wordlist file not found!")
        else:
            console.print(f"[bold yellow]📜 Using Wordlist:[/bold yellow] [cyan]{args.wordlist}[/cyan]")
            hybrid_attack(args.target, args.wordlist, hash_type=args.algorithm)
    elif args.mode == "rainbow":
        if not args.wordlist or not os.path.exists(args.wordlist):
            console.print("[bold red]❌ Error:[/bold red] Wordlist file not found!")
        else:
            console.print(f"[bold yellow]📜 Using Wordlist:[/bold yellow] [cyan]{args.wordlist}[/cyan]")
            rainbow_attack(args.target, args.wordlist, hash_type=args.algorithm)
    elif args.mode == "multithread":
        multi_thread_brute_force_attack(args.target, hash_type=args.algorithm)
    else:
        console.print("[bold red]❌ Error:[/bold red] Attack mode not implemented yet!")
