swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'api/spec_1',
            "route": '/api/spec_1.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/api/docs/static",
    # "static_folder": "static",  # must be set by user
    "swagger_ui": True,
    "specs_route": "/api/docs/"
}
swagger_template = template = {
  "swagger": "2.0",
  "info": {
    "title": "OXL GeoIP-Database API",
    "description": "API for GeoIP-Database",
    "contact": {
      "responsibleOrganization": "OXL IT Services",
      "responsibleDeveloper": "Pascal Rath",
      "email": "geoip@oxl.at",
      "url": "https://www.OXL.at",
    },
    "termsOfService": "http://github.com/O-X-L/geoip-asn",
    "version": "1.0.0"
  },
  # "host": "mysite.com",  # overrides localhost:500
  # "basePath": "/api",  # base bash for blueprint registration
  "schemes": [
    # "http",
    "https"
  ],
  # "operationId": "getmyData"
}
