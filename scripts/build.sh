#!/usr/bin/env bash

set -eu

cd "$(dirname "$0")/.."

python3 build.py

rm -f *.zip

echo ''
echo '### PACKING ###'

zip -9 'asn_ipv4_full.mmdb.zip' 'asn_ipv4_full.mmdb' LICENSE_db.txt
zip -9 'asn_ipv4_small.mmdb.zip' 'asn_ipv4_small.mmdb' LICENSE_db.txt
zip -9 'asn_ipv6_full.mmdb.zip' 'asn_ipv6_full.mmdb' LICENSE_db.txt
zip -9 'asn_ipv6_small.mmdb.zip' 'asn_ipv6_small.mmdb' LICENSE_db.txt

echo '### DONE ###'
