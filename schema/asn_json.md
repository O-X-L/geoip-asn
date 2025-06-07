# GeoIP-ASN Database - JSON-format

The ASN-information is queried from [PeeringDB](https://www.peeringdb.com/).

For the PeeringDB model-schema see: [peeringdb/django_peeringdb/models](https://github.com/peeringdb/django-peeringdb/blob/main/src/django_peeringdb/models) (*Network, Organization, NetworkContact*)

**Small databases**:
* `asn_ipv4_small.json`
* `asn_ipv6_small.json`
* `asn_small.json`

**Full databases**:
* `asn_ipv4_full.json`
* `asn_ipv6_full.json`
* `asn_full.json`

----

## V1.0

### Small

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "OXL GeoIP Database - JSON-Small - JSON Schema v1.0",
  "type": "object",
  "properties": {
    "^[0-9]*$": {
      "type": "object",
      "description": "AS Number",
      "properties": {
        "contacts": {
          "properties": {
            "abuse": {
              "properties": {
                "email": {
                  "type": "string"
                },
                "name": {
                  "type": "string"
                }
              },
              "type": "object"
            },
            "noc": {
              "properties": {
                "email": {
                  "type": "string"
                },
                "name": {
                  "type": "string"
                }
              },
              "type": "object"
            },
            "policy": {
              "properties": {
                "email": {
                  "type": "string"
                },
                "name": {
                  "type": "string"
                }
              },
              "type": "object"
            },
            "required": []
          },
          "type": "object"
        },
        "info": {
          "properties": {
            "name": {
              "type": "string"
            },
            "name_long": {
              "type": "string"
            },
            "website": {
              "type": "string"
            }
          },
          "required": [
            "website",
            "country"
          ],
          "type": "object"
        },
        "ipv4": {
          "description": "IPv4 network the AS announces via BGP",
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "ipv4_count": {
          "description": "Number of IPv4 addresses the AS announces via BGP",
          "type": "number"
        },
        "ipv6": {
          "description": "IPv6 network the AS announces via BGP",
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "ipv6_count": {
          "description": "Number of IPv6 addresses the AS announces via BGP",
          "type": "number"
        },
        "organization": {
          "properties": {
            "city": {
              "type": "string"
            },
            "country": {
              "type": "string"
            },
            "latitude": {
              "type": "number"
            },
            "longitude": {
              "type": "number"
            },
            "name": {
              "type": "string"
            },
            "name_long": {
              "type": "string"
            },
            "state": {
              "type": "string"
            },
            "website": {
              "type": "string"
            }
          },
          "required": [
            "name"
          ],
          "type": "object"
        }
      }
    }
  }
}
```

### Full

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "OXL GeoIP Database - JSON-Full - JSON Schema v1.0",
  "type": "object",
  "properties": {
    "^[0-9]*$": {
      "type": "object",
      "description": "AS Number",
      "properties": {
        "contacts": {
          "properties": {
            "abuse": {
              "properties": {
                "email": {
                  "type": "string"
                },
                "name": {
                  "type": "string"
                },
                "phone": {
                  "type": "string"
                },
                "url": {
                  "type": "string"
                }
              },
              "type": "object"
            },
            "noc": {
              "properties": {
                "email": {
                  "type": "string"
                },
                "name": {
                  "type": "string"
                },
                "phone": {
                  "type": "string"
                },
                "url": {
                  "type": "string"
                }
              },
              "type": "object"
            },
            "policy": {
              "properties": {
                "email": {
                  "type": "string"
                },
                "name": {
                  "type": "string"
                },
                "phone": {
                  "type": "string"
                },
                "url": {
                  "type": "string"
                }
              },
              "type": "object"
            },
            "required": []
          },
          "type": "object"
        },
        "info": {
          "properties": {
            "aka": {
              "type": "string"
            },
            "info_ipv6": {
              "type": "boolean"
            },
            "info_multicast": {
              "type": "boolean"
            },
            "info_never_via_route_servers": {
              "type": "boolean"
            },
            "info_prefixes4": {
              "type": "number"
            },
            "info_prefixes6": {
              "type": "number"
            },
            "info_ratio": {
              "type": "string"
            },
            "info_scope": {
              "type": "string"
            },
            "info_traffic": {
              "type": "string"
            },
            "info_types": {
              "items": {
                "type": "string"
              },
              "type": "array"
            },
            "info_unicast": {
              "type": "boolean"
            },
            "irr_as_set": {
              "type": "string"
            },
            "looking_glass": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "name_long": {
              "type": "string"
            },
            "notes": {
              "type": "string"
            },
            "policy_contracts": {
              "type": "string"
            },
            "policy_general": {
              "type": "string"
            },
            "policy_locations": {
              "type": "string"
            },
            "policy_ratio": {
              "type": "boolean"
            },
            "policy_url": {
              "type": "string"
            },
            "rir_status": {
              "type": "string"
            },
            "rir_status_updated": {
              "type": "string"
            },
            "route_server": {
              "type": "string"
            },
            "social_media": {
              "items": {
                "properties": {
                  "identifier": {
                    "type": "string"
                  },
                  "service": {
                    "type": "string"
                  }
                },
                "type": "object"
              },
              "type": "array"
            },
            "status": {
              "type": "string"
            },
            "status_dashboard": {
              "type": "string"
            },
            "website": {
              "type": "string"
            }
          },
          "required": [
            "website",
            "country"
          ],
          "type": "object"
        },
        "ipv4": {
          "description": "IPv4 network the AS announces via BGP",
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "ipv4_count": {
          "description": "Number of IPv4 addresses the AS announces via BGP",
          "type": "number"
        },
        "ipv6": {
          "description": "IPv6 network the AS announces via BGP",
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "ipv6_count": {
          "description": "Number of IPv6 addresses the AS announces via BGP",
          "type": "number"
        },
        "organization": {
          "properties": {
            "address1": {
              "type": "string"
            },
            "address2": {
              "type": "string"
            },
            "aka": {
              "type": "string"
            },
            "city": {
              "type": "string"
            },
            "country": {
              "type": "string"
            },
            "floor": {
              "type": "string"
            },
            "latitude": {
              "type": "number"
            },
            "longitude": {
              "type": "number"
            },
            "name": {
              "type": "string"
            },
            "name_long": {
              "type": "string"
            },
            "notes": {
              "type": "string"
            },
            "social_media": {
              "items": {
                "properties": {
                  "identifier": {
                    "type": "string"
                  },
                  "service": {
                    "type": "string"
                  }
                },
                "type": "object"
              },
              "type": "array"
            },
            "state": {
              "type": "string"
            },
            "status": {
              "type": "string"
            },
            "suite": {
              "type": "string"
            },
            "website": {
              "type": "string"
            },
            "zipcode": {
              "type": "string"
            }
          },
          "required": [
            "name"
          ],
          "type": "object"
        }
      }
    }
  }
}
```
