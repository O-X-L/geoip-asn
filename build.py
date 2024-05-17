# LICENSE: GPLv3
# COPYRIGHT: Rath Rene

# DATA sources:
#  IP to ASN
#    https://thyme.apnic.net/.combined/
#    https://bgp.nsrc.org/REN/.combined/
#  ASN infos
#    https://www.peeringdb.com/

import logging
from pathlib import Path
from urllib.request import urlretrieve
from os import remove as remove_file
from os import getcwd

from netaddr import IPSet
from mmdb_writer import MMDBWriter
from peeringdb import resource
from peeringdb.client import Client as PeeringDBClient
from peeringdb.commands import Sync
from peeringdb.cli import check_load_config

IPv4 = True
IPv6 = False
STATUS_INTERVAL = 10_000
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
REFRESH_DATA = False
DATA_FILE_IP4 = 'data-raw-table_ip4.tsv'
DATA_FILE_IP6 = 'data-raw-table_ip6.tsv'
pdb = PeeringDBClient()
DESCRIPTION = 'OXL ASN Database (BSD 3-Clause License)'
mmdb_ip4_full = MMDBWriter(ip_version=4, description=DESCRIPTION)
mmdb_ip6_full = MMDBWriter(ip_version=6, description=DESCRIPTION)
mmdb_ip4_small = MMDBWriter(ip_version=4, description=DESCRIPTION)
mmdb_ip6_small = MMDBWriter(ip_version=6, description=DESCRIPTION)


def _empty(v: any) -> any:
    if v is None:
        return ''

    return v


class ASN:
    def __init__(self, asn_id: int):
        self.id = asn_id
        self.ip4 = IPSet()
        self.ip6 = IPSet()
        self._info = pdb.all(resource.Network).filter(asn=asn_id).first()
        if self._info is None:
            self._org = None
            self._contacts = []

        else:
            self._org = pdb.all(resource.Organization).filter(id=self._info.org_id).first()
            self._contacts = [
                contact for contact in
                pdb.all(resource.NetworkContact).filter(net_id=self._info.id)
            ]

    @property
    def info(self) -> dict:
        # from django_peeringdb.models.concrete import Network
        if self._info is None:
            return {}

        rir_updated = ''
        if self._info.rir_status_updated is not None:
            rir_updated = self._info.rir_status_updated.strftime(DATETIME_FORMAT)

        return dict(
            status=_empty(self._info.status),
            name=_empty(self._info.name),
            aka=_empty(self._info.aka),
            name_long=_empty(self._info.name_long),
            irr_as_set=_empty(self._info.irr_as_set),
            website=_empty(self._info.website),
            social_media=_empty(self._info.social_media),
            looking_glass=_empty(self._info.looking_glass),
            route_server=_empty(self._info.route_server),
            notes=_empty(self._info.notes),
            info_traffic=_empty(self._info.info_traffic),
            info_ratio=_empty(self._info.info_ratio),
            info_scope=_empty(self._info.info_scope),
            info_types=_empty(self._info.info_types),
            info_prefixes4=_empty(self._info.info_prefixes4),
            info_prefixes6=_empty(self._info.info_prefixes6),
            info_unicast=_empty(self._info.info_unicast),
            info_multicast=_empty(self._info.info_multicast),
            info_ipv6=_empty(self._info.info_ipv6),
            info_never_via_route_servers=_empty(self._info.info_never_via_route_servers),
            policy_url=_empty(self._info.policy_url),
            policy_general=_empty(self._info.policy_general),
            policy_locations=_empty(self._info.policy_locations),
            policy_ratio=_empty(self._info.policy_ratio),
            policy_contracts=_empty(self._info.policy_contracts),
            status_dashboard=_empty(self._info.status_dashboard),
            rir_status=_empty(self._info.rir_status),
            rir_status_updated=rir_updated,
        )

    @property
    def info_small(self) -> dict:
        full = self.info
        return dict(
            name=full['name'],
            name_long=full['name_long'],
            website=full['website'],
        )

    @property
    def organization(self) -> dict:
        # from django_peeringdb.models.abstract import OrganizationBase
        if self._org is None:
            return {}

        lat = 0.0 if self._org.latitude is None else float(self._org.latitude)
        long = 0.0 if self._org.longitude is None else float(self._org.longitude)

        return dict(
            status=_empty(self._org.status),
            address1=_empty(self._org.address1),
            address2=_empty(self._org.address2),
            city=_empty(self._org.city),
            state=_empty(self._org.state),
            zipcode=_empty(self._org.zipcode),
            country=_empty(self._org.country.code),
            suite=_empty(self._org.suite),
            floor=_empty(self._org.floor),
            latitude=lat,
            longitude=long,
            name=_empty(self._org.name),
            aka=_empty(self._org.aka),
            name_long=_empty(self._org.name_long),
            website=_empty(self._org.website),
            social_media=_empty(self._org.social_media),
            notes=_empty(self._org.notes),
        )

    @property
    def organization_small(self) -> dict:
        full = self.organization
        return dict(
            name=full['name'],
            name_long=full['name_long'],
            country=full['country'],
            state=full['state'],
            city=full['city'],
            latitude=full['latitude'],
            longitude=full['longitude'],
            website=full['website'],
        )

    @property
    def contacts(self) -> dict:
        # from django_peeringdb.models.concrete import NetworkContact
        parsed_contacts = {}
        for contact in self._contacts:
            parsed_contacts[contact.role.lower()] = dict(
                name=_empty(contact.name),
                phone=_empty(contact.phone),
                email=_empty(contact.email),
                url=_empty(contact.url),
            )

        return parsed_contacts

    @property
    def contacts_small(self) -> dict:
        return {
            role: dict(
                name=contact['name'],
                email=contact['email'],
            ) for role, contact in self.contacts.items()
        }


def cleanup():
    try:
        remove_file(DATA_FILE_IP4)
        remove_file(DATA_FILE_IP6)

    except FileNotFoundError:
        pass


if not REFRESH_DATA and (
        Path('peeringdb.sqlite3').stat().st_size < 10_000_000 or
        (IPv4 and not Path(DATA_FILE_IP4).is_file()) or
        (IPv6 and not Path(DATA_FILE_IP6).is_file())
):
    REFRESH_DATA = True

if REFRESH_DATA:
    print('### DOWNLOADING DATA ###')

    cleanup()
    Sync().handle(
        check_load_config(getcwd()),
        verbose=False, quiet=False, init=False, since=-1,
        fetch_private=False,
    )
    if IPv4:
        urlretrieve('https://thyme.apnic.net/.combined/data-raw-table', DATA_FILE_IP4)

    if IPv6:
        urlretrieve('https://thyme.apnic.net/.combined/ipv6-raw-table', DATA_FILE_IP6)

asn_nets = {}
if IPv4:
    c = 0
    print('### PARSING IPv4 ###')
    with open(DATA_FILE_IP4, 'r', encoding='utf8') as f:
        for l in f.readlines():
            if c % STATUS_INTERVAL == 0:
                print('PARSING', c)

            net, asn = l.strip().split('\t')
            if asn not in asn_nets:
                asn_nets[asn] = ASN(asn)

            asn_nets[asn].ip4.add(net)
            c += 1


if IPv6:
    c = 0
    print('### PARSING IPv6 ###')
    with open(DATA_FILE_IP6, 'r', encoding='utf8') as f:
        for l in f.readlines():
            if c % STATUS_INTERVAL == 0:
                print('PARSING', c)

            net, asn = l.strip().split(' ', 1)
            asn = asn.strip()

            if not asn.isdigit():
                # some bad data
                continue

            if asn not in asn_nets:
                asn_nets[asn] = ASN(asn)

            asn_nets[asn].ip6.add(net)
            c += 1


print('### ADDING ###')
logging.getLogger('mmdb_writer').setLevel(logging.WARNING)
c = 0
for asn, data in asn_nets.items():
    if c % STATUS_INTERVAL == 0:
        print('ADDING', c)

    # add additional ASN info below
    dump_full = {'asn': asn, 'organization': data.organization, 'info': data.info, 'contacts': data.contacts}
    dump_small = {
        'asn': asn,
        'organization': data.organization_small,
        'info': data.info_small,
        'contacts': data.contacts_small,
    }
    if IPv4:
        mmdb_ip4_full.insert_network(data.ip4, dump_full)
        mmdb_ip4_small.insert_network(data.ip4, dump_small)

    if IPv6:
        mmdb_ip6_full.insert_network(data.ip6, dump_full)
        mmdb_ip6_small.insert_network(data.ip6, dump_small)

    c += 1

print('### WRITING ###')
# todo: implement CSV
if IPv4:
    mmdb_ip4_full.to_db_file('asn_ipv4_full.mmdb')
    mmdb_ip4_full.to_db_file('asn_ipv4_small.mmdb')

if IPv6:
    mmdb_ip6_full.to_db_file('asn_ipv6_full.mmdb')
    mmdb_ip6_full.to_db_file('asn_ipv6_small.mmdb')

print('### DONE ###')
if REFRESH_DATA:
    cleanup()
