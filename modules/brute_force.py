import itertools
import string
import hashlib
from rich.console import Console
from modules.verify import verify_candidate

console = Console()

def hash_password(password, hash_type="md5"):
    """ Hashes the given password using the specified algorithm. """
    hash_func = getattr(hashlib, hash_type, None)
    if not hash_func:
        console.print("[bold red]❌ Unsupported hash type![/bold red]")
        return None
    return hash_func(password.encode()).hexdigest()

def brute_force_attack(target_hash, max_length=6, hash_type="md5"):
    """
    Perform a brute force attack on the target hash.
    
    :param target_hash: The hashed password to crack.
    :param max_length: Maximum password length to attempt.
    :param hash_type: Hashing algorithm used (md5, sha256, etc.).
    """
    # Validate input
    if not target_hash:
        console.print("[bold red]❌ Error: No target hash provided![/bold red]")
        return None
    if not isinstance(max_length, int) or max_length < 1:
        console.print("[bold red]❌ Error: Invalid maximum length provided! It must be a positive integer.[/bold red]")
        return None
    if hash_type not in hashlib.algorithms_available:
        console.print(f"[bold red]❌ Unsupported hash type: {hash_type}[/bold red]")
        return None
    
    console.print(f"[bold cyan]🚀 Starting Brute Force Attack with {hash_type} hash...[/bold cyan]")

    charset = string.ascii_lowercase + string.digits  # a-z + 0-9

    # Inform user about the max password length
    console.print(f"[bold yellow]🔍 Attempting passwords up to {max_length} characters long.[/bold yellow]")
    
    for length in range(1, max_length + 1):
        console.print(f"[bold cyan]🔄 Trying passwords of length {length}...[/bold cyan]")

        for attempt in itertools.product(charset, repeat=length):
            password = ''.join(attempt)
            hashed_attempt = hash_password(password, hash_type)

            if hashed_attempt is None:
                console.print(f"[bold red]❌ Error hashing password: {password}[/bold red]")
                return None

            console.print(f"[yellow]🔍 Trying:[/yellow] {password}", end="\r")

            # Verify if the hash matches
            if verify_candidate(password, target_hash, hash_type):
                console.print(f"\n[bold green]✅ Password Found:[/bold green] {password}")
                return password

    console.print("[bold red]❌ Password Not Found within the specified attempts.[/bold red]")
    return None
