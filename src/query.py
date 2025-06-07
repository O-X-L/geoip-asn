#!/usr/bin/env python3

from sys import argv
from json import dumps

import maxminddb

if len(argv) == 1:
    raise SystemExit(
        "USAGE:\n"
        "  1 > IP\n"
        "  2 > Database (small/LARGE)"
    )


IP = argv[1]
DB = 'full'
if len(argv) == 3 and argv[2] in ['small', 'full']:
    DB = argv[2]

DB_FILE = f'asn_ipv4_{DB}.mmdb'
print('Using DB', DB_FILE)
with maxminddb.open_database(DB_FILE) as m:
    print(dumps(m.get(IP), indent=2))
