#!/usr/bin/env python3

from json import loads as json_loads
from pathlib import Path

import maxminddb
from waitress import serve
from flasgger import swag_from, Swagger
from flask import Flask, Response, json, redirect
from oxl_utils.valid.net import valid_ip4, valid_public_ip, valid_asn

from docs import swagger_config, swagger_template

app = Flask('geoip')
swagger = Swagger(app, config=swagger_config, template=swagger_template)

BASE_DIR = Path('/var/local/geoip')
ASN_DB_FILE = {
    4: BASE_DIR / 'asn_ipv4_full.mmdb',
    6: BASE_DIR / 'asn_ipv6_full.mmdb',
}
ASN_JSON_FILE = BASE_DIR / 'asn_full.json'


def _response_json(code: int, data: dict) -> Response:
    return app.response_class(
        response=json.dumps(data, indent=2),
        status=code,
        mimetype='application/json'
    )


# IP to ASN
@app.route('/api/ip/<ip>', methods=['GET'])
@swag_from('apidocs/check_ip.yml')
def ip_to_asn(ip) -> Response:
    if ip.startswith('::ffff:'):
        ip = ip.replace('::ffff:', '')

    if not valid_public_ip(ip):
        return _response_json(code=400, data={'msg': 'Invalid IP provided'})

    if valid_ip4(ip):
        db_key = 4

    else:
        db_key = 6

    with maxminddb.open_database(ASN_DB_FILE[db_key]) as m:
        return _response_json(code=200, data=m.get(ip))


# ASN Lookup
@app.route('/api/asn/<nr>', methods=['GET'])
@swag_from('apidocs/check_asn.yml')
def asn_lookup(nr) -> Response:
    if not valid_asn(nr):
        return _response_json(code=400, data={'msg': 'Invalid ASN provided'})

    try:
        return _response_json(code=200, data=ASN_DATA[str(nr)])

    except KeyError:
        return _response_json(code=404, data={'msg': 'Provided ASN not found'})


@app.route('/')
def catch_base():
    return redirect(f"https://geoip.oxl.app/api/ip", code=302)


@app.route('/<path:path>')
def catch_all(path):
    del path
    return redirect(f"https://geoip.oxl.app/api/ip", code=302)


if __name__ == '__main__':
    with open(ASN_JSON_FILE, 'r', encoding='utf-8') as f:
        ASN_DATA = json_loads(f.read())

    serve(app, host='127.0.0.1', port=8000)
