import itertools
import string
import hashlib
from concurrent.futures import ProcessPoolExecutor, as_completed
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

def worker(candidate, target_hash, hash_type):
    """
    Worker function to check a candidate password.
    """
    password = ''.join(candidate)
    if verify_candidate(password, target_hash, hash_type):
        return password
    return None

def multi_thread_brute_force_attack(target_hash, max_length=6, hash_type="md5", chunk_size=1000, max_workers=4):
    """
    Perform a multi-threaded brute force attack on the target hash.
    
    :param target_hash: The hashed password to crack.
    :param max_length: Maximum password length to attempt.
    :param hash_type: Hashing algorithm used (md5, sha256, etc.).
    :param chunk_size: Number of candidates to process per chunk.
    :param max_workers: Number of parallel processes to use.
    """
    console.print("[bold cyan]🚀 Starting Multi-threaded Brute Force Attack...[/bold cyan]")
    
    charset = string.ascii_lowercase + string.digits  # a-z + 0-9
    
    for length in range(1, max_length + 1):
        console.print(f"[bold yellow]Trying passwords of length {length}...[/bold yellow]")
        candidate_iter = itertools.product(charset, repeat=length)
        
        # Process candidates in chunks.
        while True:
            chunk = list(itertools.islice(candidate_iter, chunk_size))
            if not chunk:
                break
            with ProcessPoolExecutor(max_workers=max_workers) as executor:
                # Submit each candidate in the current chunk.
                futures = {executor.submit(worker, candidate, target_hash, hash_type): candidate for candidate in chunk}
                for future in as_completed(futures):
                    result = future.result()
                    if result is not None:
                        console.print(f"\n[bold green]✅ Password Found:[/bold green] {result}")
                        return result
    console.print("[bold red]❌ Password Not Found[/bold red]")
    return None
