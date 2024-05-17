import maxminddb

m = maxminddb.open_database('asn_ipv4.mmdb')
r = m.get('17.100.1.1')
print(r)
