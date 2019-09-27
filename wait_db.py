#!/usr/bin/env python
import sys
import time

import MySQLdb
from world.settings import DATABASES

args = sys.argv

if __name__ == "__main__":
    _, db, user, password, host, port = tuple(DATABASES["default"].values())
    for i in range(int(args[1])):
        try:
            MySQLdb.connect(host=host,
                            user=user,
                            db=db,
                            password=password,
                            charset='utf8mb4'
                            )
            frag = "OK"

        except:
            time.sleep(1)
            print("waiting for db ...")
            frag = "NG"

    if frag == "NG":
        print("Please retry")
    else:
        print("OK")
