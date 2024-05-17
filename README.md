# Open IP to ASN/Internet Provider Database

If you have on how to improve this project: [feel free to start a discussion](https://github.com/O-X-L/geoip-asn/discussions)

## Data sources

IP to ASN:
* BGP routing data (https://thyme.apnic.net/.combined/ or https://bgp.nsrc.org/REN/.combined/)

ASN information:
* https://www.peeringdb.com/

----

## Databases

Data is updated daily.

### Download

* [IPv4 Full in MMDB format](https://geoip.oxl.at/file/asn_ipv4_full.mmdb.zip) (*recommended*)
* [IPv6 Full in MMDB format](https://geoip.oxl.at/file/asn_ipv6_full.mmdb.zip) (*recommended*)
<!--
* [IPv4 Full in CVS format](https://geoip.oxl.at/file/asn_ipv4_full.csv.zip)
* [IPv6 Full in CVS format](https://geoip.oxl.at/file/asn_ipv6_full.csv.zip)
-->
* [IPv4 Stripped in MMDB format](https://geoip.oxl.at/file/asn_ipv4_small.mmdb.zip)
* [IPv6 Stripped in MMDB format](https://geoip.oxl.at/file/asn_ipv6_small.mmdb.zip)
<!--
* [IPv4 Stripped in CSV format](https://geoip.oxl.at/file/asn_ipv4_small.csv.zip)
* [IPv6 Stripped in CSV format](https://geoip.oxl.at/file/asn_ipv4_small.csv.zip)
-->

Limit: 1 Download per day


#### Schema Examples

* [Full](https://github.com/O-X-L/geoip-asn/blob/latest/example/full.json)
* [Small](https://github.com/O-X-L/geoip-asn/blob/latest/example/small.json)

----

### API

[ASN API](https://geoip.oxl.at/api/asn)

```
curl -XGET https://geoip.oxl.at/api/asn/1.1.1.1
```

Limits:

* 10 Requests per min
* 50 Requests per 10 min
* 100 Requests per hour

----

## License(s)

### Databases

**[BSD-3-Clause](https://opensource.org/license/bsd-3-clause)**

Free to use.

If you are nice, you can optionally mention that you use this IP data: 

```html
<p>IP address data powered by <a href="https://geoip.oxl.at">OXL</a></p>
```

### Build Script (this repository)

**[GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html)**
