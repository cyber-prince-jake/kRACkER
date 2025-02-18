# kRACkER - Advanced Password Cracker 🚀

kRACkER is a powerful and flexible password cracking tool designed to demonstrate various attack methods for password hashes. It supports brute force, dictionary, hybrid, and rainbow table attacks. You can use it to crack passwords of various hash algorithms such as MD5, SHA-256, and more.

## Table of Contents

- [Features]
- [Installation]
- [Usage]
  - [Available Modes]
  - [Command Examples]
- [Wordlist Support]
  - [Adding More Wordlists]
  - [Wordlist Generation]
- [Hash Algorithm Support]
- [Error Handling]
- [Performance Optimizations]
- [Contributing]

## Features

- **Brute Force Attack**: Tries every possible combination of characters up to a defined length.
- **Dictionary Attack**: Uses an external wordlist to attempt cracking the hash.
- **Hybrid Attack**: Combines brute force and dictionary attacks for more efficient cracking.
- **Rainbow Table Attack**: Precomputes hash values for words in the wordlist for fast lookups.
- **Multiple Hash Algorithms**: Supports MD5, SHA-256, and more.
- **Multi-threading**: Speeds up attacks by using multiple CPU cores.
- **Wordlist Flexibility**: Can work with any wordlist, including popular ones like `rockyou.txt`.

## Installation

To install kRACkER on your system, follow these steps:

1. Clone the repository:
   
   ```
   git clone https://github.com/cyber-prince-jake/kRACkER.git
   cd kRACkER
   ```

2. Install the required Python dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

To run the tool, use the following command format:

```
python3 main.py -m [mode] -t [target_hash] -w [wordlist]
```

### Available Modes

- **brute**: Performs a brute force attack.
- **dict**: Uses a dictionary (wordlist) to crack the hash.
- **hybrid**: Combines brute force and dictionary attack for enhanced cracking.
- **rainbow**: Utilizes a precomputed rainbow table for fast hash lookup.

### Command Examples

#### Brute Force Attack

```
python3 main.py -m brute -t [target_hash]
```

#### Dictionary Attack

```
python3 main.py -m dict -t [target_hash] -w /path/to/wordlist.txt
```

#### Hybrid Attack

```
python3 main.py -m hybrid -t [target_hash] -w /path/to/wordlist.txt
```

#### Rainbow Table Attack

```
python3 main.py -m rainbow -t [target_hash] -w /path/to/wordlist.txt
```

## Wordlist Support

kRACkER supports any wordlist format, and you can specify the wordlist using the `-w` option. By default, it works with plain text wordlists where each word is on a new line.

### Adding More Wordlists

You can use any custom wordlist or download popular ones like `rockyou.txt`. Place the wordlist in the `wordlists/` directory or specify the full path using the `-w` option.

Example:

```
python3 main.py -m dict -t [target_hash] -w wordlists/rockyou.txt
```

### Wordlist Generation

You can also generate your own wordlist using the `generate_wordlist.py` script. It allows you to create wordlists with custom combinations.

```
python3 generate_wordlist.py
```

This will create a `common.txt` wordlist with 2000 common passwords.

## Hash Algorithm Support

kRACkER currently supports the following hash algorithms:

- **MD5**
- **SHA-256**

To specify the hash algorithm, use the `-h` option.

Example:
```
python3 main.py -m brute -t [target_hash] -h sha256
```

## Error Handling

kRACkER includes robust error handling to cover various edge cases:

- Missing or incorrect wordlist paths.
- Unsupported hash types.
- Invalid input parameters.
- File not found errors.

If any errors occur, appropriate messages will be displayed.

## Performance Optimizations

- **Multi-threading**: kRACkER uses multi-threading for faster brute force and hybrid attacks by leveraging multiple CPU cores.
- **Rainbow Table**: The rainbow table lookup is optimized for speed by precomputing hash values for words in the wordlist.

## Contributing

We welcome contributions! If you'd like to contribute to kRACkER, feel free to open an issue or submit a pull request.

### How to Contribute

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-xyz`).
3. Commit your changes (`git commit -m 'Add feature xyz'`).
4. Push to the branch (`git push origin feature-xyz`).
5. Open a pull request.




**This Tool Was Created by Prince Jake, an Ethical Hacker, in the year 2025** 🎯
