from util.csv_reader import writeCSV


def populate():
    userDB = [["id", "username", "password", "role", "image"]]
    userDB.append([0, "admin", "admin", "admin", "none"])
    userDB.append([1, "user1", "hehe", "dosen", "none"])
    writeCSV("../db/user.csv", userDB, "w")
