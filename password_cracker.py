import hashlib
from hashlib import sha1

def crack_sha1_hash(hash, use_salts=False):
    try:
        password_found = False
        passwords = open("top-10000-passwords.txt", "r")
        for password in passwords:
            if use_salts is True:
                with open("known-salts.txt", "r") as salts:
                    for salt in salts:
                        salt = salt.splitlines()[0]
                        password = password.splitlines()[0]
                        prepend_digest = sha1(
                            (salt +
                             password).encode("UTF-8").strip()).hexdigest()
                        append_digest = sha1(
                            (password +
                             salt).encode("UTF-8").strip()).hexdigest()

                        if hash in (prepend_digest, append_digest):
                            salts.close()
                            passwords.close()

                            password_found = True

                            return password
            else:
                password = password.splitlines()[0]
                encoded_pass = password.encode("UTF-8")
                digest = sha1(encoded_pass.strip()).hexdigest()

                if digest == hash:
                    passwords.close()
                    password_found = True
                    return password

        if password_found is False:
            passwords.close()
            return "PASSWORD NOT IN DATABASE"

    except FileNotFoundError:
        print("Error: file not found")
        quit()
