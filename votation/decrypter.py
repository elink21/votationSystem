import mysql.connector
import random
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="*v%_M_%m9S$4Y5+%",
    database="EncryptedVoting"
)

hashedStrings = {}


def randomString(key: str) -> str:
    generatedString = ""
    if(key in hashedStrings.keys()):
        return hashedStrings[key]

    length = random.randint(3, 40)
    for _ in range(length):
        generatedString += str(random.choice("abcdefghijklmnopqrstuvwxyz"))

    hashedStrings[key] = generatedString
    return generatedString


def decrypt(field: str, val: str) -> str:
    cursor = db.cursor()
    if(len(val) != 23):
        return "Length MUST be 23 characters"
    cursor.execute(
        f"select id from votation_userencrypted where {field}='{val}'")
    id = cursor.fetchone()
    if(id == None):
        return randomString("c")
    id = id[0]

    cursor.execute(
        f"select {field} from votation_django_system where id={id}"
    )

    res = cursor.fetchone()
    res = res[0]

    return str(res)


"""

"""
while(True):
    print()
    field = input(
        "Enter field to decrypt(since they all are using different keys): ")
    value = input("Now type the hashing value: ")
    print(f"Decrypted value is: < {decrypt(field,value)} >")
