import hashlib
from rich.console import Console
from modules.verify import verify_candidate

console = Console()

def hash_password(password, hash_type="md5"):
    """
    Hashes a password using the specified algorithm.
    """
    hash_func = getattr(hashlib, hash_type, None)
    if not hash_func:
        console.print("[bold red]❌ Unsupported hash type![/bold red]")
        return None
    return hash_func(password.encode()).hexdigest()

def hybrid_attack(target_hash, wordlist_path, hash_type="md5", max_suffix_length=2):
    """
    Hybrid Attack:
    For each word in the wordlist, first try the word as is, then try appending numbers.
    
    :param target_hash: The hash to crack.
    :param wordlist_path: Path to the dictionary file.
    :param hash_type: The hash algorithm (default "md5").
    :param max_suffix_length: The maximum number of digits to append (e.g., 2 => tries 0 to 99).
    """
    # Validate input
    if not target_hash:
        console.print("[bold red]❌ Error: No target hash provided![/bold red]")
        return None
    if not isinstance(max_suffix_length, int) or max_suffix_length < 1:
        console.print("[bold red]❌ Error: Invalid maximum suffix length! It must be a positive integer.[/bold red]")
        return None
    if hash_type not in hashlib.algorithms_available:
        console.print(f"[bold red]❌ Unsupported hash type: {hash_type}[/bold red]")
        return None

    try:
        with open(wordlist_path, "r", encoding="utf-8") as file:
            words = [line.strip() for line in file]
    except FileNotFoundError:
        console.print("[bold red]❌ Wordlist file not found![/bold red]")
        return None

    console.print(f"[bold cyan]📜 Starting Hybrid Attack with {hash_type} hash...[/bold cyan]")

    # Try each word and its numeric variations.
    for word in words:
        # Try the original word.
        if verify_candidate(word, target_hash, hash_type):
            console.print(f"\n[bold green]✅ Password Found:[/bold green] {word}")
            return word

        # Try appending numbers (from 0 to 10^max_suffix_length - 1).
        for num in range(0, 10**max_suffix_length):
            variation = word + str(num)
            hashed_variation = hash_password(variation, hash_type)

            if hashed_variation == target_hash:
                console.print(f"\n[bold green]✅ Password Found:[/bold green] {variation}")
                return variation

    console.print("[bold red]❌ Password Not Found[/bold red]")
    return None
