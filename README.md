# Open IP to ASN/Internet Provider Database

## Data sources

IP to ASN:
* BGP routing data (https://thyme.apnic.net/.combined/ or https://bgp.nsrc.org/REN/.combined/)

ASN information:
* https://www.peeringdb.com/

----

## Databases

### Download

* [Full in MMDB format](https://geoip.oxl.at/file/asn_full.mmdb.zip) (*recommended*)
<!--* [Full in CVS format](https://geoip.oxl.at/file/asn_full.csv.zip)-->
* [Stripped in MMDB format](https://geoip.oxl.at/file/asn_small.mmdb.zip)
<!--* [Stripped in CSV format](https://geoip.oxl.at/file/asn_small.csv.zip)-->

Limit: 1 Download per IP and day

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
