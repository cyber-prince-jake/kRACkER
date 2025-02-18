import hashlib
from rich.console import Console
from modules.verify import verify_candidate  # Import the verify_candidate function

console = Console()

def hash_password(password, hash_type="md5"):
    """
    Hashes a password using the specified algorithm.
    """
    if hash_type == "md5":
        return hashlib.md5(password.encode()).hexdigest()
    elif hash_type == "sha256":
        return hashlib.sha256(password.encode()).hexdigest()
    else:
        raise ValueError("Unsupported hash type!")

def rainbow_attack(target_hash, wordlist_path, hash_type="md5"):
    """
    Rainbow Table Attack:
    Precompute hash values for each word in the wordlist and then look up the target hash.
    
    :param target_hash: The hash to crack.
    :param wordlist_path: Path to the dictionary file.
    :param hash_type: The hash algorithm (default "md5").
    """
    try:
        with open(wordlist_path, "r", encoding="utf-8") as file:
            words = [line.strip() for line in file]
    except FileNotFoundError:
        console.print("[bold red]❌ Wordlist file not found![/bold red]")
        return None

    console.print("[bold cyan]📜 Generating Rainbow Table...[/bold cyan]")
    rainbow_table = {}
    
    # Precompute hashes and store them in the rainbow table
    for word in words:
        hash_value = hash_password(word, hash_type)
        rainbow_table[hash_value] = word

    console.print("[bold cyan]🔍 Looking up target hash in Rainbow Table...[/bold cyan]")
    
    # Instead of directly comparing the hash, use the verify_candidate function
    for candidate_hash, candidate_word in rainbow_table.items():
        if verify_candidate(candidate_word, target_hash, hash_type):  # Verify with hash_type
            console.print(f"\n[bold green]✅ Password Found:[/bold green] {candidate_word}")
            return candidate_word
    
    console.print("[bold red]❌ Password Not Found in Rainbow Table[/bold red]")
    return None
