# **cmu pgp**

literally just a cmd line wrapper for gnupg.

### instaling cmupgp

ok first you have to clone the repository and run this

```bash
git clone https://github.com/manuanish/CMU-PGP && cd CMU-PGP
```

activate the venv using

```bash
source .venv/bin/activate
```

now run the program like this

```bash
python src/main.py
```

and in your terminal it should be working :O

### useage

we can use the program like this ...

#### get you frist key pair

run the command to create a public/private key pair

```bash
cgp --full-gen-key
```

#### signing messages

we can run this command to clear-sign a message

```bash
cgp --clear-sign *fiel name*
```

#### verifying signatures

to verify another message you can run

```bash
cgp --verify *file name*
```

this will return something like this

```
Signature made <time stamp>
cgp:                using <key type (usually RSA)> key <key id>
cgp: Good signature from "<name> (<comment>) <email>" [ultimate]
```

#### encrypting/decoding messages

we can also encrypt and decode message using

```bash
cgp --encrypt
```

and

```bash
cgp --decrypt
```

if you want to learn more about this, go the gnupg website over here https://www.gnupg.org/gph/en/manual/book1.html

thats all for today. thanks for reading guys!!!!
