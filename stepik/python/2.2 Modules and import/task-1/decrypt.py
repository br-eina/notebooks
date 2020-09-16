import simplecrypt
from datetime import datetime

start_time = datetime.now()


path_encrypted = "2.2/task-1/encrypted.bin"
path_passwords = "2.2/task-1/passwords.txt"

with open(path_encrypted, "rb") as data_file:
    encrypted = data_file.read()

pw_file = open(path_passwords, 'r')
passwords = [line.strip() for line in pw_file]


# decr_list = []
for password in passwords:
    try:
        decrypted = simplecrypt.decrypt(password, encrypted)
        break
    except simplecrypt.DecryptionException:
        pass

answer_file = open('2.2/task-1/answer.txt', 'w')
answer_file.write(decrypted.decode('utf8'))

print(datetime.now() - start_time)