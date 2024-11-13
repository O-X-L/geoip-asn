# Open IP to ASN/Internet Provider Database

[![Lint](https://github.com/O-X-L/geoip-asn/actions/workflows/lint.yml/badge.svg)](https://github.com/O-X-L/geoip-asn/actions/workflows/lint.yml)
[![API Uptime](https://status.oxl.at/api/v1/endpoints/2--oxl-apis_geoip-db/uptimes/7d/badge.svg
)](https://status.oxl.at/endpoints/2--oxl-apis_geoip-db)

If you have an idea on how to improve this project: [feel free to start a discussion](https://github.com/O-X-L/geoip-asn/discussions)

Thanks go to the author of [hackitu.de](https://www.hackitu.de/geoip/) for sharing his knowledge about this topic.

If you don't care about the License restrictions - you may get data of better quality by using the free [IPInfo](https://ipinfo.io/products/free-ip-database) or [MaxMind](https://dev.maxmind.com/geoip/geolite2-free-geolocation-data) databases. In comparison with these - the database provided by **this project has pretty much NO usage restrictions**.

Also check out our [Risk-Database](https://github.com/O-X-L/risk-db).

## Data sources

IP to ASN:
* BGP routing data (https://thyme.apnic.net/.combined/ or https://bgp.nsrc.org/REN/.combined/)

ASN information:
* https://www.peeringdb.com/

----

## Databases

[![Database Updated At](https://geoip.oxl.app/file/updated.svg)](https://geoip.oxl.app/file/updated.svg)

Data is updated daily.

### Download

Note: Databases in MMDB format might be faster and cheaper to query.

#### IPv4

* [IPv4 Stripped in MMDB format](https://geoip.oxl.app/file/asn_ipv4_small.mmdb.zip) (*recommended*)
* [IPv4 Full in MMDB format](https://geoip.oxl.app/file/asn_ipv4_full.mmdb.zip)
* [IPv4 Stripped in JSON format](https://geoip.oxl.app/file/asn_ipv4_small.json.zip)
* [IPv4 Full in JSON format](https://geoip.oxl.app/file/asn_ipv4_full.json.zip)


#### IPv6

* [IPv6 Stripped in MMDB format](https://geoip.oxl.app/file/asn_ipv6_small.mmdb.zip)
* [IPv6 Full in MMDB format](https://geoip.oxl.app/file/asn_ipv6_full.mmdb.zip)
* [IPv6 Stripped in JSON format](https://geoip.oxl.app/file/asn_ipv6_small.json.zip)
* [IPv6 Full in JSON format](https://geoip.oxl.app/file/asn_ipv6_full.json.zip)

#### IPv4 + IPv6

* [IPv4+IPv6 Stripped in JSON format](https://geoip.oxl.app/file/asn_small.json.zip)
* [IPv4+IPv6 Full in JSON format](https://geoip.oxl.app/file/asn_full.json.zip)


#### Schema Examples

* [MMDB Full](https://github.com/O-X-L/geoip-asn/blob/latest/example/mmdb_full.json)
* [MMDB Small](https://github.com/O-X-L/geoip-asn/blob/latest/example/mmdb_small.json)
* [JSON Full](https://github.com/O-X-L/geoip-asn/blob/latest/example/json_full.json)
* [JSON Small](https://github.com/O-X-L/geoip-asn/blob/latest/example/json_small.json)

**Limits**:

* Without token: 2 Downloads per IP & day
* With token: 5 Downloads per IP & day

----

### API

* [IP-to-ASN API](https://geoip.oxl.app/api/ip)
* [ASN Lookup API](https://geoip.oxl.app/api/asn/13335)

```
# IP to ASN
curl -XGET https://geoip.oxl.app/api/ip/1.1.1.1

# ASN Lookup
curl -XGET https://geoip.oxl.app/api/asn/13335
```

**Limits**:

* Without token:

  * 500 Requests per IP & 10 min
  * 5000 Requests per IP & day
  * Anti-DOS

* With token:

  * 5000 Requests per IP & 10 min
  * Anti-DOS

If you want to get a (free) token for your systems - feel free to contact us at: [geoip@oxl.at](mailto:risk-db@oxl.at)

----

## License(s)

### Databases

**[BSD-3-Clause](https://opensource.org/license/bsd-3-clause)**

Free to use.

If you are nice, you can **optionally** mention that you use this IP data: 

```html
<p>IP address data powered by <a href="https://geoip.oxl.app">OXL</a></p>
```

### Build Script (this repository)

**[GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html)**
