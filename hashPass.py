import hashlib
import uuid

def generate_salt():
    return str(uuid.uuid4())

def hash_password(password):
    salt = generate_salt()
    md5 = hashlib.md5()
    md5.update((salt + password).encode('ascii'))
    return salt, md5.hexdigest()

def store_password(plain_pass):
    salt, hsh = hash_password(plain_pass)
    with open('password_hashes.txt', 'a') as f:
        f.write(hsh + "\n")
    with open('password_salts.txt', 'a') as f:
        f.write(salt + "\n")

def check_password(plain_pass):
    hashes = []
    salts = []
    try:
        with open('password_hashes.txt', 'r+') as f:
            hashes = f.readlines()
        with open('password_salts.txt', 'r+') as f:
            salts = f.readlines()
    except Exception:
        print('no passwords')

    for i in range(len(hashes)):
        md5 = hashlib.md5()
        md5.update((salts[i].strip() + plain_pass).encode('ascii'))
        if md5.hexdigest().strip() == hashes[i].strip():
            print('User {} Authenticated'.format(i))
            return True

    print("No matching password found.")
    return False


