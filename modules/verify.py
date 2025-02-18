import hashlib
import bcrypt

def verify_candidate(candidate, target_hash, hash_type="md5"):
    """
    Verifies if the candidate password matches the target hash using the specified algorithm.

    :param candidate: The candidate password (plaintext).
    :param target_hash: The hash to be matched.
    :param hash_type: The algorithm used ("md5", "sha256", "bcrypt").
    :return: True if the candidate matches the target hash, False otherwise.
    """
    try:
        if hash_type == "md5":
            candidate_hash = hashlib.md5(candidate.encode()).hexdigest()
            return candidate_hash == target_hash
        elif hash_type == "sha256":
            candidate_hash = hashlib.sha256(candidate.encode()).hexdigest()
            return candidate_hash == target_hash
        elif hash_type == "bcrypt":
            # bcrypt expects bytes for both the candidate and the stored hash.
            return bcrypt.checkpw(candidate.encode(), target_hash.encode())
        else:
            raise ValueError(f"Unsupported hash type: {hash_type}")
    except Exception as e:
        print(f"[bold red]❌ Error during hash comparison: {e}[/bold red]")
        return False
