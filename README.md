# Open IP to ASN/Internet Provider Database

If you have an idea on how to improve this project: [feel free to start a discussion](https://github.com/O-X-L/geoip-asn/discussions)

Thanks go to the author of [hackitu.de](https://www.hackitu.de/geoip/) for sharing his knowledge about this topic.

If you don't care about the License restrictions - you may want to use the free [IPInfo](https://ipinfo.io/products/free-ip-database) or [MaxMind](https://dev.maxmind.com/geoip/geolite2-free-geolocation-data) databases. In comparison with these - the database provided by **this project has pretty much NO usage restrictions**.

## Data sources

IP to ASN:
* BGP routing data (https://thyme.apnic.net/.combined/ or https://bgp.nsrc.org/REN/.combined/)

ASN information:
* https://www.peeringdb.com/

----

## Databases

Data is updated daily.

### Download

Limit: 2 Downloads per day

Note: Databases in MMDB format might be faster and cheaper to query.

#### IPv4

* [IPv4 Stripped in MMDB format](https://geoip.oxl.at/file/asn_ipv4_small.mmdb.zip) (*recommended*)
* [IPv4 Full in MMDB format](https://geoip.oxl.at/file/asn_ipv4_full.mmdb.zip)
* [IPv4 Stripped in JSON format](https://geoip.oxl.at/file/asn_ipv4_small.json.zip)
* [IPv4 Full in JSON format](https://geoip.oxl.at/file/asn_ipv4_full.json.zip)


#### IPv6

* [IPv6 Stripped in MMDB format](https://geoip.oxl.at/file/asn_ipv6_small.mmdb.zip)
* [IPv6 Full in MMDB format](https://geoip.oxl.at/file/asn_ipv6_full.mmdb.zip)
* [IPv6 Stripped in JSON format](https://geoip.oxl.at/file/asn_ipv6_small.json.zip)
* [IPv6 Full in JSON format](https://geoip.oxl.at/file/asn_ipv6_full.json.zip)

#### IPv4 + IPv6

* [IPv4+IPv6 Stripped in JSON format](https://geoip.oxl.at/file/asn_small.json.zip)
* [IPv4+IPv6 Full in JSON format](https://geoip.oxl.at/file/asn_full.json.zip)


#### Schema Examples

* [MMDB Full](https://github.com/O-X-L/geoip-asn/blob/latest/example/mmdb_full.json)
* [MMDB Small](https://github.com/O-X-L/geoip-asn/blob/latest/example/mmdb_small.json)
* [JSON Full](https://github.com/O-X-L/geoip-asn/blob/latest/example/json_full.json)
* [JSON Small](https://github.com/O-X-L/geoip-asn/blob/latest/example/json_small.json)

----

### API

[IP-to-ASN API](https://geoip.oxl.at/api/ip)
[ASN Lookup API](https://geoip.oxl.at/api/asn)

```
# IP to ASN
curl -XGET https://geoip.oxl.at/api/ip/1.1.1.1

# ASN Lookup
curl -XGET https://geoip.oxl.at/api/asn/13335
```

Limits:

* 50 Requests per 10 min
* 200 Requests per day

----

## License(s)

### Databases

**[BSD-3-Clause](https://opensource.org/license/bsd-3-clause)**

Free to use.

If you are nice, you can **optionally** mention that you use this IP data: 

```html
<p>IP address data powered by <a href="https://geoip.oxl.at">OXL</a></p>
```

### Build Script (this repository)

**[GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html)**
