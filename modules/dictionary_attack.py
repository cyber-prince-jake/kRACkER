import hashlib
from rich.console import Console
from modules.verify import verify_candidate
import os

console = Console()

def hash_password(password, hash_type="md5"):
    """ Hashes the given password using the specified algorithm. """
    hash_func = getattr(hashlib, hash_type, None)
    if not hash_func:
        console.print("[bold red]❌ Unsupported hash type![/bold red]")
        return None
    return hash_func(password.encode()).hexdigest()

def dictionary_attack(target_hash, wordlist_path, hash_type="md5"):
    """
    Perform a dictionary attack using a wordlist.
    
    :param target_hash: The hashed password to crack.
    :param wordlist_path: Path to the wordlist file.
    :param hash_type: Hashing algorithm used (md5, sha256, etc.).
    """
    # Validate that the wordlist exists
    if not os.path.exists(wordlist_path):
        console.print(f"[bold red]❌ Error: Wordlist file not found at {wordlist_path}[/bold red]")
        return None

    try:
        with open(wordlist_path, "r", encoding="utf-8") as wordlist:
            console.print("[bold cyan]📜 Starting Dictionary Attack...[/bold cyan]")
            
            for word in wordlist:
                word = word.strip()
                hashed_attempt = hash_password(word, hash_type)
                
                if hashed_attempt is None:
                    continue  # Skip invalid hashes if they couldn't be generated

                console.print(f"[yellow]🔍 Trying:[/yellow] {word}", end="\r")

                if verify_candidate(word, target_hash, hash_type):  # Corrected variable name
                    console.print(f"\n[bold green]✅ Password Found:[/bold green] {word}")
                    return word

    except Exception as e:
        console.print(f"[bold red]❌ Error: {str(e)}[/bold red]")
    
    console.print("[bold red]❌ Password Not Found[/bold red]")
    return None
