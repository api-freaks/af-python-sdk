# Reference
<details><summary><code>client.<a href="src/apifreaks/client.py">geolocation_lookup</a>(...) -> GeolocationLookupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get detailed geolocation data for an IP address including country, city, timezone, currency, and optional security and user-agent information
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.geolocation_lookup(
    api_key="apiKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[GeolocationLookupRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**ip:** `typing.Optional[str]` — IPv4, IPv6, or hostname for geolocation lookup
    
</dd>
</dl>

<dl>
<dd>

**lang:** `typing.Optional[GeolocationLookupRequestLang]` — Response language for location fields
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Comma separated list of fields to include in response
    
</dd>
</dl>

<dl>
<dd>

**excludes:** `typing.Optional[str]` — Comma separated list of fields to exclude from response
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[str]` — Additional data to include (location, network, security, currency, time_zone, user_agent, country_metadata , hostname, liveHostname, hostnameFallbackLivet)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">bulk_geolocation_lookup</a>(...) -> typing.List[BulkGeolocationLookupResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve detailed geolocation data for multiple IP addresses in a single request.
Supports up to `50,000` IP-addresses/host-names per request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.bulk_geolocation_lookup(
    api_key="apiKey",
    ips=[
        "ips"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**ips:** `typing.List[str]` — List of IP addresses or hostnames to lookup
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[BulkGeolocationLookupRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**lang:** `typing.Optional[str]` — Language of the response.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Comma-separated list of fields to include in the response. Can include "geo".
    
</dd>
</dl>

<dl>
<dd>

**excludes:** `typing.Optional[str]` — Comma-separated list of fields to exclude from the response (except "ip").
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[str]` — Comma-separated list of additional information to include in the response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">ip_security_lookup</a>(...) -> IpSecurityLookupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get comprehensive security information for a given IP address. Detects VPNs, proxies, Tor nodes, and other security threats.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.ip_security_lookup(
    api_key="apiKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[IpSecurityLookupRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**ip:** `typing.Optional[str]` — A valid IPv4 or IPv6 address to look up. If omitted, the API uses the public IP of the requesting client.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Comma-separated list of fields to return. Supports dot notation (e.g. security.threat_score).
    
</dd>
</dl>

<dl>
<dd>

**excludes:** `typing.Optional[str]` — Comma-separated list of fields to remove from the response. Supports dot notation (e.g. security.is_tor).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">bulk_ip_security_lookup</a>(...) -> typing.List[BulkIpSecurityLookupResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Bulk IP Security Lookup API allows you to retrieve security details for up to `50,000` IP-addresses in a single request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.bulk_ip_security_lookup(
    api_key="apiKey",
    ips=[
        "ips"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**ips:** `typing.List[str]` — List of IP addresses to lookup
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[BulkIpSecurityLookupRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Comma-separated list of fields to return. Supports dot notation (e.g. security.threat_score).
    
</dd>
</dl>

<dl>
<dd>

**excludes:** `typing.Optional[str]` — Comma-separated list of fields to remove from the response. Supports dot notation (e.g. security.is_tor).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">geocoder_search</a>(...) -> typing.List[GeocoderSearchResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Convert a given address or place name into geographic coordinates (latitude and longitude).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.geocoder_search(
    api_key="apiKey",
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` — Free-form search query, e.g. Wembley Stadium, London
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[GeocoderSearchRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Max number of results to return (1–40). May return fewer if matches are weak.
    
</dd>
</dl>

<dl>
<dd>

**min_lat:** `typing.Optional[float]` — Minimum latitude for the viewbox. Must be ≤ max_lat and between -90 and 90.
    
</dd>
</dl>

<dl>
<dd>

**max_lat:** `typing.Optional[float]` — Maximum latitude for the viewbox. Must be ≥ min_lat and between -90 and 90.
    
</dd>
</dl>

<dl>
<dd>

**min_lon:** `typing.Optional[float]` — Minimum longitude for the viewbox. Must be ≤ max_lon and between -180 and 180.
    
</dd>
</dl>

<dl>
<dd>

**max_lon:** `typing.Optional[float]` — Maximum longitude for the viewbox. Must be ≥ min_lon and between -180 and 180.
    
</dd>
</dl>

<dl>
<dd>

**accept_language:** `typing.Optional[str]` — Preferred language order for showing search results. This may either be a simple comma-separated list of language codes or a single entry. The results will be in the 1st language which is matched from the header. As a fallback if the results are not supported in the given language, 'en' will be used.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">geocoder_reverse</a>(...) -> GeocoderReverseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Convert geographic coordinates (latitude and longitude) into a human-readable address or place name.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.geocoder_reverse(
    api_key="apiKey",
    lat=1.1,
    lon=1.1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**lat:** `float` — WGS84 latitude value ranging from -90 to 90.
    
</dd>
</dl>

<dl>
<dd>

**lon:** `float` — WGS84 longitude value ranging from -180 to 180.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[GeocoderReverseRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**accept_language:** `typing.Optional[str]` — Preferred language order for showing search results. This may either be a simple comma-separated list of language codes or a single entry. The results will be in the 1st language which is matched from the header. As a fallback if the results are not supported in the given language, en will be used.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">domain_whois_lookup</a>(...) -> DomainWhoisLookupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve current WHOIS information for a domain name.
This endpoint provides detailed registration information including registrar details,
dates, nameservers, and registrant information.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.domain_whois_lookup(
    api_key="apiKey",
    domain_name="domainName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**domain_name:** `str` — Domain name for WHOIS lookup
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[DomainWhoisLookupRequestFormat]` — Response format (defaults to json)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">bulk_domain_whois_lookup</a>(...) -> BulkDomainWhoisLookupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve WHOIS information for `100 Domains per Request`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.bulk_domain_whois_lookup(
    api_key="apiKey",
    domain_names=[
        "domainNames"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**domain_names:** `typing.List[str]` — A list of domain names for which WHOIS data is requested.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[BulkDomainWhoisLookupRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">ip_whois_lookup</a>(...) -> IpWhoisLookupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns WHOIS registration details for a specified IP address (IPv4 or IPv6).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.ip_whois_lookup(
    api_key="apiKey",
    ip="ip",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**ip:** `str` — The IP address (IPv4 or IPv6) for which WHOIS data is requested.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[IpWhoisLookupRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">asn_whois_lookup</a>(...) -> AsnWhoisLookupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns WHOIS registration details for a specified ASN, with or without the 'as' prefix.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.asn_whois_lookup(
    api_key="apiKey",
    asn="asn",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**asn:** `str` — The Autonomous System Number (ASN) to retrieve WHOIS data for. Can be prefixed with 'as' or not.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[AsnWhoisLookupRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">domain_whois_history</a>(...) -> DomainWhoisHistoryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve historical WHOIS records for a domain name.
This endpoint provides a timeline of all recorded changes in domain registration information.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.domain_whois_history(
    api_key="apiKey",
    domain_name="domainName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**domain_name:** `str` — Domain name for historical WHOIS lookup
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[DomainWhoisHistoryRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">domain_whois_reverse</a>(...) -> DomainWhoisReverseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Performs a reverse WHOIS search using one or more search parameters like keyword, email, owner, or company.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.domain_whois_reverse(
    api_key="apiKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[DomainWhoisReverseRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**keyword:** `typing.Optional[str]` — Keyword search term for reverse WHOIS by keyword (case-insensitive pattern matching).
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Email search term for reverse WHOIS by email address (case-insensitive exact or regex match; * wildcard supported).
    
</dd>
</dl>

<dl>
<dd>

**owner:** `typing.Optional[str]` — Registrant or owner name for reverse WHOIS (a full-text search phrase matching technique to retrieve results).
    
</dd>
</dl>

<dl>
<dd>

**company:** `typing.Optional[str]` — Organization or company name for reverse WHOIS (full-text search phrase matching technique to retrieve results).
    
</dd>
</dl>

<dl>
<dd>

**exact:** `typing.Optional[bool]` — Accepts 'true' or 'false'. "true" returns only records that exactly match the input (keyword, owner/registrant, or company). "false" returns all matches and is the default when omitted.
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[DomainWhoisReverseRequestMode]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number for paginated results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">domain_dns_lookup</a>(...) -> DomainDnsLookupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve real-time DNS records for any hostname. Supports multiple record types including A, AAAA, MX, NS, SOA, SPF, TXT, and CNAME records.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.domain_dns_lookup(
    api_key="apiKey",
    type=[
        "type"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[DomainDnsLookupRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**host_name:** `typing.Optional[str]` — Hostname or URL whose DNS records are required.
    
</dd>
</dl>

<dl>
<dd>

**ip_address:** `typing.Optional[str]` — The IP address for requested DNS's PTR record. 'type' parameter must be set to 'all'.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of DNS record types for lookup. Possible values: A, AAAA, MX, NS, SOA, SPF, TXT, CNAME, or all. When ipAddress is provided, type must be "all".
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">bulk_domain_dns_lookup</a>(...) -> BulkDomainDnsLookupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Perform DNS lookups for multiple hostnames in a single request. Supports up to `100 host-names per request`
and returns DNS records including A, AAAA, MX, NS, SOA, SPF, TXT, and CNAME records.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.bulk_domain_dns_lookup(
    api_key="apiKey",
    type=[
        "type"
    ],
    domain_names=[
        "domainNames"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**domain_names:** `typing.List[str]` — List of hostnames to lookup DNS records for
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[BulkDomainDnsLookupRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

A comma-separated list of DNS record types for lookup.
Possible values: A, AAAA, MX, NS, SOA, SPF, TXT, CNAME, or all
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">domain_dns_history</a>(...) -> DomainDnsHistoryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve historical DNS records for any hostname. Access unique historical data for A, AAAA, MX, NS, SOA, SPF, TXT, and CNAME records,
including subdomains. Results are paginated with up to 100 unique records per page.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.domain_dns_history(
    api_key="apiKey",
    host_name="host-name",
    type=[
        "type"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**host_name:** `str` — Hostname or URL whose historical DNS records are required
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[DomainDnsHistoryRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

A comma-separated list of DNS record types for lookup.
Possible values: A, AAAA, MX, NS, SOA, SPF, TXT, CNAME, or all
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number for paginated results
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">domain_dns_reverse</a>(...) -> DomainDnsReverseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all the hostnames associated with any particular A, AAAA, MX, NS, SOA, SPF, TXT, and CNAME DNS records. For instance, you can access all the hostnames hosted on any IP/CIDR notation, all the domain names using Cloudflare name servers, and all the domain names using Google Mailbox
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.domain_dns_reverse(
    api_key="apiKey",
    type="A",
    value="value",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**type:** `DomainDnsReverseRequestType` 

The type of reverse DNS lookup to perform. Determines how the value parameter is interpreted:
- A: IPv4 CIDR block
- AAAA: IPv6 CIDR block
- MX: Mail provider domain
- NS: Name server provider hostname
- SOA: SOA record admin domain
- SPF/TXT: Target verification strings
- CNAME: Target hostname
    
</dd>
</dl>

<dl>
<dd>

**value:** `str` — Provide an IP or CIDR for A/AAAA lookups, or a hostname/selector for MX, NS, SOA, SPF, TXT, and CNAME queries. Wildcard regex patterns are also supported (e.g., mail.google.com, m*.google.com, _spf.g*.com, s*.g*.com).
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[DomainDnsReverseRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**exact:** `typing.Optional[bool]` — Accepts 'true' or 'false'. "true" returns only records that exactly match the input (NS, MX, CNAME, SOA, SPF, TXT). "false" returns all matches (default when omitted).
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number to paginate through results (defaults to 1).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">web_scrape</a>(...) -> WebScrapeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute a series of web scraping instructions on a target URL. 
Supports various operations like form filling, clicking, data extraction, and CAPTCHA solving.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi, WebScrapeRequestBodyBlockUrl, WebScrapeRequestBodyBlockUrlCookiesItem, WebScrapeRequestBodyBlockUrlInstructionsItemFill, WebScrapeRequestBodyBlockUrlInstructionsItemFillFill, WebScrapeRequestBodyBlockUrlInstructionsItemClick, WebScrapeRequestBodyBlockUrlInstructionsItemWait, WebScrapeRequestBodyBlockUrlInstructionsItemExtract, WebScrapeRequestBodyBlockUrlInstructionsItemExtractExtract, WebScrapeRequestBodyBlockUrlInstructionsItemBlockElement, WebScrapeRequestBodyBlockUrlInstructionsItemGeneralImageCaptcha, WebScrapeRequestBodyBlockUrlInstructionsItemGeneralImageCaptchaGeneralImageCaptchaItem
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.web_scrape(
    api_key="apiKey",
    url="https://example.com",
    request=WebScrapeRequestBodyBlockUrl(
        block_url=[
            "https://example.com/ads.js",
            "https://tracker.example.com/*"
        ],
        cookies=[
            WebScrapeRequestBodyBlockUrlCookiesItem(
                name="sessionid",
                value="abc123",
            ),
            WebScrapeRequestBodyBlockUrlCookiesItem(
                name="user_pref",
                value="darkmode",
            )
        ],
        instructions=[
            WebScrapeRequestBodyBlockUrlInstructionsItemFill(
                fill=WebScrapeRequestBodyBlockUrlInstructionsItemFillFill(
                    place="#username",
                    value="myuser",
                ),
            ),
            WebScrapeRequestBodyBlockUrlInstructionsItemFill(
                fill=WebScrapeRequestBodyBlockUrlInstructionsItemFillFill(
                    place="#password",
                    value="mypassword",
                ),
            ),
            WebScrapeRequestBodyBlockUrlInstructionsItemClick(
                click="#loginButton",
            ),
            WebScrapeRequestBodyBlockUrlInstructionsItemWait(
                wait=2000,
            ),
            WebScrapeRequestBodyBlockUrlInstructionsItemExtract(
                extract=WebScrapeRequestBodyBlockUrlInstructionsItemExtractExtract(
                    html="#profile",
                    text="#welcome-message",
                    user_data="#user-info",
                ),
            ),
            WebScrapeRequestBodyBlockUrlInstructionsItemBlockElement(
                block_element=[
                    ".ad-banner",
                    "//div[@class=\'popup\']"
                ],
            ),
            WebScrapeRequestBodyBlockUrlInstructionsItemGeneralImageCaptcha(
                general_image_captcha=[
                    WebScrapeRequestBodyBlockUrlInstructionsItemGeneralImageCaptchaGeneralImageCaptchaItem(
                        image_path="#captcha-img",
                        text_field="#captcha-input",
                        image_update_path="#refresh-captcha",
                        captcha_failed_path="#captcha-error",
                        model="mini-ocr-v1",
                    )
                ],
            )
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — Target URL to scrape
    
</dd>
</dl>

<dl>
<dd>

**request:** `WebScrapeRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[WebScrapeRequestFormat]` — Response format returned by the API.
    
</dd>
</dl>

<dl>
<dd>

**text:** `typing.Optional[bool]` — Set to `true` to return the data in text format else `false` for data in html format with tags.
    
</dd>
</dl>

<dl>
<dd>

**js_enabled:** `typing.Optional[bool]` 

Set  `true` to handle websites with JavaScript. Set `false` to handle static html websites.


 Default value is `true`.
    
</dd>
</dl>

<dl>
<dd>

**proxy:** `typing.Optional[WebScrapeRequestProxy]` — Use proxy for requests
    
</dd>
</dl>

<dl>
<dd>

**ssl_ignore:** `typing.Optional[bool]` 

Ignore SSL certificate errors.


 Only works if **jsEnabled** is **true**.
    
</dd>
</dl>

<dl>
<dd>

**window_size:** `typing.Optional[str]` 

Specify the browser window size in the format 'width,height' (e.g., "1920w,1080h"). Default value is the default resolutions provided by web/browser.


 Only works if **jsEnabled** is **true**.
    
</dd>
</dl>

<dl>
<dd>

**ad_block:** `typing.Optional[bool]` 

Set to `true` to apply ad-blocker to the specified URL else false or ignore to not apply.


 Only works if **jsEnabled** is **true**.
    
</dd>
</dl>

<dl>
<dd>

**captcha:** `typing.Optional[bool]` 

if true user can provide captcha instructions in the instructions to solve image captchas.


  Only works if **jsEnabled** is **true**.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">email_validate</a>(...) -> EmailValidateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Validates a single email address and returns result.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.email_validate(
    api_key="apiKey",
    email="email",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — Email address to validate
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[EmailValidateRequestFormat]` — Format of the response
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the email address
    
</dd>
</dl>

<dl>
<dd>

**ip:** `typing.Optional[str]` — IP address of the email address
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">bulk_email_validate</a>(...) -> BulkEmailValidateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Validates a bulk of email addresses and returns result for each. Maximum `10` email addresses per request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi, BulkEmailValidateRequestEmailDataItem
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.bulk_email_validate(
    api_key="apiKey",
    email_data=[
        BulkEmailValidateRequestEmailDataItem(
            email="email",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**email_data:** `typing.List[BulkEmailValidateRequestEmailDataItem]` — Array of email objects for bulk validation
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[BulkEmailValidateRequestFormat]` — Format of the response
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">phone_validate</a>(...) -> PhoneValidateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Validates a single phone number and returns detailed metadata including carrier, line type, geolocation, time zones, and standardized formats.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.phone_validate(
    api_key="apiKey",
    number="+14155552671",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**number:** `str` — Phone number to validate. Accepts international format (+14155552671), local format (4155552671) with region, or IDD format (0014155552671) with dialer_region.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[PhoneValidateRequestFormat]` — Specifies the desired format for the API response. Choose 'json' for a JSON object. If not provided, the API defaults to JSON format.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — Two-letter ISO country code (e.g., US, GB). Required when number is in local format without + prefix. Cannot be used together with dialer_region.
    
</dd>
</dl>

<dl>
<dd>

**dialer_region:** `typing.Optional[str]` — Two-letter ISO country code indicating the country the number is being dialed from. Required when number uses IDD exit code. Cannot be used together with region.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">bulk_phone_validate</a>(...) -> typing.List[BulkPhoneValidateResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Validates up to 100 phone numbers in a single request. Each number is processed independently — invalid entries return per-number errors without affecting the rest of the batch.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi, BulkPhoneValidateRequestNumbersItem
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.bulk_phone_validate(
    api_key="apiKey",
    numbers=[
        BulkPhoneValidateRequestNumbersItem(
            number="+14155552671",
        ),
        BulkPhoneValidateRequestNumbersItem(
            number="+447911123456",
        ),
        BulkPhoneValidateRequestNumbersItem(
            number="+919876543210",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**numbers:** `typing.List[BulkPhoneValidateRequestNumbersItem]` — Array of phone number objects. Maximum 100 per request.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[BulkPhoneValidateRequestFormat]` — Specifies the desired format for the API response. Choose 'json' for a JSON object. If not provided, the API defaults to JSON format.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">domain_ssl_lookup</a>(...) -> DomainSslLookupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve comprehensive SSL certificate information without the certificate chain.
This endpoint provides detailed information about the SSL certificate including expiry dates, issuer details, and encryption methods.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.domain_ssl_lookup(
    api_key="apiKey",
    domain_name="domainName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**domain_name:** `str` — Domain name or URL whose SSL certificate lookup is required
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[DomainSslLookupRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**ssl_raw:** `typing.Optional[bool]` — Set to true to get the raw openSSL response of the domain
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">domain_ssl_chain_lookup</a>(...) -> DomainSslChainLookupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the complete SSL certificate chain from root Certificate Authority (CA) to end-user certificate.
This endpoint provides comprehensive information about each certificate in the chain.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.domain_ssl_chain_lookup(
    api_key="apiKey",
    domain_name="domainName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**domain_name:** `str` — Domain name or URL whose SSL certificate chain lookup is required
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[DomainSslChainLookupRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**ssl_raw:** `typing.Optional[bool]` — Set to true to get the raw openSSL response for each certificate in the chain
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">domain_availability_check</a>(...) -> DomainAvailabilityCheckResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Domain Search API is designed to simplify the process of finding available domain names across all top-level domains (TLDs) and second-level domains (SLDs).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.domain_availability_check(
    api_key="apiKey",
    domain="domain",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**domain:** `str` — Domain name whose availability is to be checked.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[DomainAvailabilityCheckRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[DomainAvailabilityCheckRequestSource]` — Specify the data source for domain availability checks. Use "dns" for DNS-based lookups or "whois" for WHOIS-based lookups. By default, "dns" is used.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">bulk_domain_availability_check</a>(...) -> BulkDomainAvailabilityCheckResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Perform Bulk Domain Availability checks using a list of domains. Supports upto `100 Domains Per Request`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.bulk_domain_availability_check(
    api_key="apiKey",
    domain_names=[
        "domainNames"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**domain_names:** `typing.List[str]` — List of domain names to check.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[BulkDomainAvailabilityCheckRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[BulkDomainAvailabilityCheckRequestSource]` — Specify the data source for domain availability checks. Use "dns" for DNS-based lookups or "whois" for WHOIS-based lookups. By default, "dns" is used.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">domain_availability_suggestions</a>(...) -> DomainAvailabilitySuggestionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Domain Search API is designed to simplify the process of finding available domain names across all top-level domains (TLDs) and second-level domains (SLDs).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.domain_availability_suggestions(
    api_key="apiKey",
    domain="domain",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**domain:** `str` — Domain name for availability and suggestions.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[DomainAvailabilitySuggestionsRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[DomainAvailabilitySuggestionsRequestSource]` — Specify the data source for domain availability checks. Use "dns" for DNS-based lookups or "whois" for WHOIS-based lookups. By default, "dns" is used.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — Number of suggestions to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">subdomains_lookup</a>(...) -> SubdomainsLookupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Subdomain Lookup API is designed to retrieve subdomains related to the given domain name. It helps you explore subdomains that are available for registration or usage.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.subdomains_lookup(
    api_key="apiKey",
    domain="domain",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**domain:** `str` — Domain name for availability and suggestions.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[SubdomainsLookupRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[datetime.date]` — Filter subdomains seen after this date (format YYYY-MM-DD).
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[datetime.date]` — Filter subdomains seen before this date( format YYYY-MM-DD).
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[SubdomainsLookupRequestStatus]` — Filter subdomains by status (active or inactive).
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[str]` — Page number for paginated results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">pdf_merge</a>(...) -> PdfMergeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API merges multiple PDF files into a single PDF, in the order they are provided
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.pdf_merge(
    api_key="apiKey",
    file=["example_file"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[PdfMergeRequestFormat]` — Specifies the desired format for the API response. Choose 'json' for a JSON object or 'xml' for an XML structure.
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — An array of unique file IDs referencing PDF files previously uploaded to the API Freaks server. Use this parameter to merge existing files without re-uploading them. Provide multiple IDs to merge files in the specified order.
    
</dd>
</dl>

<dl>
<dd>

**destroy:** `typing.Optional[bool]` — If set to `true`, the input file(s) will be permanently deleted from the server immediately after the output PDF is generated.
    
</dd>
</dl>

<dl>
<dd>

**output:** `typing.Optional[str]` — Specifies the desired name for the resulting merged PDF file. If not provided, a default name will be assigned.
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — The URL to which the webhook notification will be sent after the task is completed.
    
</dd>
</dl>

<dl>
<dd>

**webhook_failure_notification:** `typing.Optional[bool]` — If true, a notification will also be sent by email in case the webhook request fails all the retries.  The email notification will be sent to the requesting user or their organization’s admin if part of one.
    
</dd>
</dl>

<dl>
<dd>

**webhook_authorization:** `typing.Optional[str]` — Optional custom header for webhook requests. Format: `Key:Value` (e.g., `Authorization:Bearer token123`). This will be sent as an HTTP header in the webhook call.
    
</dd>
</dl>

<dl>
<dd>

**file:** `typing.Optional[typing.List[core.File]]` — The PDF file(s) to be processed. If this parameter is not provided, you must specify `file_id` to use previously uploaded files.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">pdf_remove_pages</a>(...) -> PdfRemovePagesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API removes a selection or range of pages from a PDF file.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.pdf_remove_pages(
    api_key="apiKey",
    pages="pages",
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**pages:** `str` — Specifies which pages to remove from the PDF. Accepts individual page numbers (e.g., '1,7') and/or ascending page ranges (e.g., '3-5'). Use commas to separate entries and hyphens for ranges. Reverse ranges (e.g., '5-3') are not allowed. Alternatively, you may provide only one of the following keywords: 'even' (removes all even-numbered pages), 'odd' (removes all odd-numbered pages), or 'last' (removes only the last page). The keyword 'all' is not supported for this operation. Examples: '1,3-5', 'even'. Mixing special keywords with specific pages/ranges is not allowed.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[PdfRemovePagesRequestFormat]` — Specifies the desired format for the API response. Choose 'json' for a JSON object or 'xml' for an XML structure.
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `typing.Optional[str]` — The unique identifier of a PDF file already uploaded to the API Freaks server. Use this as an alternative to uploading a new file directly.
    
</dd>
</dl>

<dl>
<dd>

**destroy:** `typing.Optional[bool]` — If set to `true`, the input file(s) will be permanently deleted from the server immediately after the output PDF is generated.
    
</dd>
</dl>

<dl>
<dd>

**output:** `typing.Optional[str]` — The desired name for the output PDF file after pages have been removed. If not provided, a default name will be assigned.
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — The URL to which the webhook notification will be sent after the task is completed.
    
</dd>
</dl>

<dl>
<dd>

**webhook_failure_notification:** `typing.Optional[bool]` — If true, a notification will also be sent by email in case the webhook request fails all the retries.  The email notification will be sent to the requesting user or their organization’s admin if part of one.
    
</dd>
</dl>

<dl>
<dd>

**webhook_authorization:** `typing.Optional[str]` — Optional custom header for webhook requests. Format: `Key:Value` (e.g., `Authorization:Bearer token123`). This will be sent as an HTTP header in the webhook call.
    
</dd>
</dl>

<dl>
<dd>

**file:** `typing.Optional[core.File]` — The PDF file to be processed. If this parameter is not provided, you must specify `file_id` to use a previously uploaded file.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">pdf_split</a>(...) -> PdfSplitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API splits a PDF into multiple parts based on specified page numbers or ranges.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.pdf_split(
    api_key="apiKey",
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[PdfSplitRequestFormat]` — Specifies the desired format for the API response. Choose 'json' for a JSON object or 'xml' for an XML structure.
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `typing.Optional[str]` — The unique ID of a PDF file already uploaded to the API Freaks server. Use this as an alternative to uploading a new file directly.
    
</dd>
</dl>

<dl>
<dd>

**destroy:** `typing.Optional[bool]` — If set to `true`, the input file(s) will be permanently deleted from the server immediately after the output PDF is generated.
    
</dd>
</dl>

<dl>
<dd>

**output:** `typing.Optional[str]` — The desired base name for the output PDF files after splitting. If not provided, a default naming convention will be used.
    
</dd>
</dl>

<dl>
<dd>

**pages:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Defines the page numbers or ranges where the PDF should be split. Provide individual pages and/or ranges in any order (for example: "1-4,9-5,16-last"). Separate entries with commas and use hyphens for ranges.

Special keywords (use alone):

• `even` — split at every even-numbered page

• `odd` — split at every odd-numbered page

• `all` — split the PDF into single-page files

The keyword `last` can be used anywhere in the string, in combination with page numbers or ranges (for example: "5-last", "last-2", "1,last,9").

Examples:
- "1,4-2,last"
- "odd"
- "all"
- "last,2-5"

Invalid example: "1,odd" (mixing a keyword other than "last" with specific pages/ranges is not allowed). You can pass multiple pages entries to produce multiple output files.
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — The URL to which the webhook notification will be sent after the task is completed.
    
</dd>
</dl>

<dl>
<dd>

**webhook_failure_notification:** `typing.Optional[bool]` — If true, a notification will also be sent by email in case the webhook request fails all the retries.  The email notification will be sent to the requesting user or their organization’s admin if part of one.
    
</dd>
</dl>

<dl>
<dd>

**webhook_authorization:** `typing.Optional[str]` — Optional custom header for webhook requests. Format: `Key:Value` (e.g., `Authorization:Bearer token123`). This will be sent as an HTTP header in the webhook call.
    
</dd>
</dl>

<dl>
<dd>

**file:** `typing.Optional[core.File]` — The PDF file to be processed. If this parameter is not provided, you must specify `file_id` to use a previously uploaded file.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">pdf_rotate</a>(...) -> PdfRotateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API rotates pages of a PDF by a specified angle (in multiples of 90 degrees).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.pdf_rotate(
    api_key="apiKey",
    rotate=1,
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**rotate:** `int` — The angle in degrees to rotate the selected pages. Must be one of the following values: 0, 90, 180, 270, -90, -180, or -270. All rotations are applied clockwise.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[PdfRotateRequestFormat]` — Specifies the desired format for the API response. Choose 'json' for a JSON object or 'xml' for an XML structure.
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `typing.Optional[str]` — The unique ID of a PDF file already uploaded to the API Freaks server. Use this as an alternative to uploading a new file directly.
    
</dd>
</dl>

<dl>
<dd>

**destroy:** `typing.Optional[bool]` — If set to `true`, the input file(s) will be permanently deleted from the server immediately after the output PDF is generated.
    
</dd>
</dl>

<dl>
<dd>

**output:** `typing.Optional[str]` — The desired name for the output PDF file after rotation. If not provided, a default name will be assigned.
    
</dd>
</dl>

<dl>
<dd>

**pages:** `typing.Optional[str]` — Specifies which pages to rotate. Accepts individual page numbers (e.g., '1,7') and/or ascending page ranges (e.g., '3-5'). Use commas to separate entries and hyphens for ranges. Reverse ranges (e.g., '5-3') are not allowed. Alternatively, provide only one of the following keywords: 'even' (rotate all even-numbered pages), 'odd' (rotate all odd-numbered pages), 'last' (rotate only the last page), or 'all' (rotate all pages). Examples: '1,3-5', 'odd', 'all'. Mixing special keywords with specific pages/ranges is not allowed.
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — The URL to which the webhook notification will be sent after the task is completed.
    
</dd>
</dl>

<dl>
<dd>

**webhook_failure_notification:** `typing.Optional[bool]` — If true, a notification will also be sent by email in case the webhook request fails all the retries.  The email notification will be sent to the requesting user or their organization’s admin if part of one.
    
</dd>
</dl>

<dl>
<dd>

**webhook_authorization:** `typing.Optional[str]` — Optional custom header for webhook requests. Format: `Key:Value` (e.g., `Authorization:Bearer token123`). This will be sent as an HTTP header in the webhook call.
    
</dd>
</dl>

<dl>
<dd>

**file:** `typing.Optional[core.File]` — The PDF file to be processed. If this parameter is not provided, you must specify `file_id` to use a previously uploaded file.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">pdf_compress</a>(...) -> PdfCompressResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API compresses a given PDF file to reduce its file size.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.pdf_compress(
    api_key="apiKey",
    compression_level="low",
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**compression_level:** `PdfCompressRequestCompressionLevel` — Controls how aggressively the PDF is compressed. Lower levels preserve more quality, while higher levels reduce file size more.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[PdfCompressRequestFormat]` — Specifies the desired format for the API response. Choose 'json' for a JSON object or 'xml' for an XML structure.
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `typing.Optional[str]` — The unique ID of a PDF file already uploaded to the API Freaks server. Use this as an alternative to uploading a new file.
    
</dd>
</dl>

<dl>
<dd>

**output:** `typing.Optional[str]` — Name of the output PDF.
    
</dd>
</dl>

<dl>
<dd>

**destroy:** `typing.Optional[bool]` — If set to true, the input file(s) will be deleted from the server immediately after the output is generated.
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — The URL to which the webhook notification will be sent after the task is completed.
    
</dd>
</dl>

<dl>
<dd>

**webhook_failure_notification:** `typing.Optional[bool]` — If true, a notification will also be sent by email in case the webhook request fails all the retries.  The email notification will be sent to the requesting user or their organization’s admin if part of one.
    
</dd>
</dl>

<dl>
<dd>

**webhook_authorization:** `typing.Optional[str]` — Optional custom header for webhook requests. Format: `Key:Value` (e.g., `Authorization:Bearer token123`). This will be sent as an HTTP header in the webhook call.
    
</dd>
</dl>

<dl>
<dd>

**file:** `typing.Optional[core.File]` — The PDF file to be processed. If this parameter is not provided, you must specify `file_id` to use a previously uploaded file.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">pdf_extract_pages</a>(...) -> PdfExtractPagesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API extracts specific pages or page ranges from a PDF file and returns them as a new PDF.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.pdf_extract_pages(
    api_key="apiKey",
    pages="pages",
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**pages:** `str` — Specifies which pages to extract from the PDF. You can provide individual page numbers (e.g., '2') and/or page ranges in any order, including descending (e.g., '9-5', '16-last'). Use commas to separate entries and hyphens for ranges. You may alternatively pass only one of the special keywords: 'even' (extracts all even-numbered pages), 'odd' (extracts all odd-numbered pages), 'last' (extracts only the last page), or 'all' (extracts all pages into individual files). Examples: '2,6-3', 'even', 'all'. Mixing special keywords with specific pages/ranges is not allowed.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[PdfExtractPagesRequestFormat]` — Specifies the desired format for the API response. Choose 'json' for a JSON object or 'xml' for an XML structure.
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `typing.Optional[str]` — The unique ID of a PDF file already uploaded to the API Freaks server. Use this as an alternative to uploading a new file directly.
    
</dd>
</dl>

<dl>
<dd>

**destroy:** `typing.Optional[bool]` — If set to `true`, the input file(s) will be permanently deleted from the server immediately after the output PDF is generated.
    
</dd>
</dl>

<dl>
<dd>

**output:** `typing.Optional[str]` — The desired name for the output PDF file after pages have been extracted. If not provided, a default name will be assigned.
    
</dd>
</dl>

<dl>
<dd>

**separated:** `typing.Optional[bool]` — If set to `true`, each of the specified pages will be extracted and returned as a separate PDF file.
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — The URL to which the webhook notification will be sent after the task is completed.
    
</dd>
</dl>

<dl>
<dd>

**webhook_failure_notification:** `typing.Optional[bool]` — If true, a notification will also be sent by email in case the webhook request fails all the retries.  The email notification will be sent to the requesting user or their organization’s admin if part of one.
    
</dd>
</dl>

<dl>
<dd>

**webhook_authorization:** `typing.Optional[str]` — Optional custom header for webhook requests. Format: `Key:Value` (e.g., `Authorization:Bearer token123`). This will be sent as an HTTP header in the webhook call.
    
</dd>
</dl>

<dl>
<dd>

**file:** `typing.Optional[core.File]` — The PDF file to be processed. If this parameter is not provided, you must specify `file_id` to use a previously uploaded file.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">pdf_linearize</a>(...) -> PdfLinearizeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

API endpoint that linearizes any given PDF, restructuring it for faster loading and page-by-page viewing in web browsers.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.pdf_linearize(
    api_key="apiKey",
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[PdfLinearizeRequestFormat]` — Specifies the desired format for the API response. Choose 'json' for a JSON object or 'xml' for an XML structure.
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `typing.Optional[str]` — The unique ID of a PDF file already uploaded to the API Freaks server. Use this as an alternative to uploading a new file directly.
    
</dd>
</dl>

<dl>
<dd>

**destroy:** `typing.Optional[bool]` — If set to `true`, the input file(s) will be permanently deleted from the server immediately after the output PDF is generated.
    
</dd>
</dl>

<dl>
<dd>

**output:** `typing.Optional[str]` — The desired name for the output PDF file after pages have been extracted. If not provided, a default name will be assigned.
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — The URL to which the webhook notification will be sent after the task is completed.
    
</dd>
</dl>

<dl>
<dd>

**webhook_failure_notification:** `typing.Optional[bool]` — If true, a notification will also be sent by email in case the webhook request fails all the retries.  The email notification will be sent to the requesting user or their organization’s admin if part of one.
    
</dd>
</dl>

<dl>
<dd>

**webhook_authorization:** `typing.Optional[str]` — Optional custom header for webhook requests. Format: `Key:Value` (e.g., `Authorization:Bearer token123`). This will be sent as an HTTP header in the webhook call.
    
</dd>
</dl>

<dl>
<dd>

**file:** `typing.Optional[core.File]` — The PDF file to be processed. If this parameter is not provided, you must specify `file_id` to use a previously uploaded file.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">pdf_encrypt</a>(...) -> PdfEncryptResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API encrypts a PDF file by setting a password required to open it.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.pdf_encrypt(
    api_key="apiKey",
    user_password="user_password",
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**user_password:** `str` — Sets the user password required to open and view the encrypted PDF file. Password Length should be between 6 and 128 characters.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[PdfEncryptRequestFormat]` — Specifies the desired format for the API response. Choose 'json' for a JSON object or 'xml' for an XML structure.
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `typing.Optional[str]` — The unique ID of a PDF file already uploaded to the API Freaks server. Use this as an alternative to uploading a new file directly.
    
</dd>
</dl>

<dl>
<dd>

**destroy:** `typing.Optional[bool]` — If set to `true`, the input file(s) will be permanently deleted from the server immediately after the output PDF is generated.
    
</dd>
</dl>

<dl>
<dd>

**output:** `typing.Optional[str]` — The desired name for the output encrypted PDF file. If not provided, a default name will be assigned.
    
</dd>
</dl>

<dl>
<dd>

**file_password:** `typing.Optional[str]` — The password to unlock the input file if it is already protected. Either the owner password or user password can be provided. The owner password takes precedence. Password Length should be between 6 and 128 characters.
    
</dd>
</dl>

<dl>
<dd>

**owner_password:** `typing.Optional[str]` — Sets the owner password for the PDF file. This password provides full access, including the ability to remove restrictions. If not provided, the `user_password` will also be used as the owner password. Password Length should be between 6 and 128 characters.
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — The URL to which the webhook notification will be sent after the task is completed.
    
</dd>
</dl>

<dl>
<dd>

**webhook_failure_notification:** `typing.Optional[bool]` — If true, a notification will also be sent by email in case the webhook request fails all the retries.  The email notification will be sent to the requesting user or their organization’s admin if part of one.
    
</dd>
</dl>

<dl>
<dd>

**webhook_authorization:** `typing.Optional[str]` — Optional custom header for webhook requests. Format: `Key:Value` (e.g., `Authorization:Bearer token123`). This will be sent as an HTTP header in the webhook call.
    
</dd>
</dl>

<dl>
<dd>

**file:** `typing.Optional[core.File]` — The PDF file to be processed. If this parameter is not provided, you must specify `file_id` to use a previously uploaded file.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">pdf_decrypt</a>(...) -> PdfDecryptResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API decrypts PDF files, removing all encryption, including open passwords and permission restrictions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.pdf_decrypt(
    api_key="apiKey",
    file_password="file_password",
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**file_password:** `str` — The password to unlock the input file if it is protected. Either the owner password or user password can be provided. The owner password takes precedence. Password Length should be between 6 and 128 characters.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[PdfDecryptRequestFormat]` — Specifies the desired format for the API response. Choose 'json' for a JSON object or 'xml' for an XML structure.
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `typing.Optional[str]` — The unique ID of a PDF file already uploaded to the API Freaks server. Use this as an alternative to uploading a new file directly.
    
</dd>
</dl>

<dl>
<dd>

**destroy:** `typing.Optional[bool]` — If set to `true`, the input file(s) will be permanently deleted from the server immediately after the output PDF is generated.
    
</dd>
</dl>

<dl>
<dd>

**output:** `typing.Optional[str]` — The desired name for the output decrypted PDF file. If not provided, a default name will be assigned.
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — The URL to which the webhook notification will be sent after the task is completed.
    
</dd>
</dl>

<dl>
<dd>

**webhook_failure_notification:** `typing.Optional[bool]` — If true, a notification will also be sent by email in case the webhook request fails all the retries.  The email notification will be sent to the requesting user or their organization’s admin if part of one.
    
</dd>
</dl>

<dl>
<dd>

**webhook_authorization:** `typing.Optional[str]` — Optional custom header for webhook requests. Format: `Key:Value` (e.g., `Authorization:Bearer token123`). This will be sent as an HTTP header in the webhook call.
    
</dd>
</dl>

<dl>
<dd>

**file:** `typing.Optional[core.File]` — The PDF file to be processed. If this parameter is not provided, you must specify `file_id` to use a previously uploaded file.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">pdf_restrict</a>(...) -> PdfRestrictResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API applies permission restrictions on a PDF file, such as disabling printing, copying, or editing. This can include password protection to enforce restrictions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.pdf_restrict(
    api_key="apiKey",
    user_password="user_password",
    restrictions=[
        "print_high"
    ],
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**user_password:** `str` — Sets the password users will use to open the PDF. If this is not set, only the owner password will be configured, and anyone can open the PDF file with the provided restrictions enabled. Password Length should be between 6 and 128 characters.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[PdfRestrictRequestFormat]` — Specifies the desired format for the API response. Choose 'json' for a JSON object or 'xml' for an XML structure.
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `typing.Optional[str]` — The unique ID of a PDF file already uploaded to the API Freaks server. Use this as an alternative to uploading a new file directly.
    
</dd>
</dl>

<dl>
<dd>

**destroy:** `typing.Optional[bool]` — If set to `true`, the input file(s) will be permanently deleted from the server immediately after the output PDF is generated.
    
</dd>
</dl>

<dl>
<dd>

**output:** `typing.Optional[str]` — The desired name for the output restricted PDF file. If not provided, a default name will be assigned.
    
</dd>
</dl>

<dl>
<dd>

**file_password:** `typing.Optional[str]` — The password to unlock the input file if it is already secured. Provide the owner password if available; otherwise, the user password. The owner password takes precedence. Password Length should be between 6 and 128 characters.
    
</dd>
</dl>

<dl>
<dd>

**owner_password:** `typing.Optional[str]` — Sets the password that allows full access to the PDF (e.g., removing restrictions). If not provided, the `user_password` (if set) will also be used as the owner password. Password Length should be between 6 and 128 characters.
    
</dd>
</dl>

<dl>
<dd>

**restrictions:** `typing.Optional[typing.Union[PdfRestrictRequestRestrictionsItem, typing.Sequence[PdfRestrictRequestRestrictionsItem]]]` 

A comma-separated list of restrictions to apply to the PDF. These define what the end-user is *not* allowed to do with the PDF. Available options are:


* **print_high** – Disables high-quality printing.
* **print_low** – Disables low-resolution printing.
* **edit_document_assembly** – Prevents reordering or inserting pages.
* **fill_form_fields** – Disallows filling in PDF form fields.
* **edit_annotations** – Disables adding or modifying annotations or comments.
* **modify_content** – Prevents modifying existing content in the PDF.
* **copy_and_extract_content** – Disables copying text or images from the PDF.
* **use_accessibility** – Prevents screen readers or accessibility tools from accessing content.
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — The URL to which the webhook notification will be sent after the task is completed.
    
</dd>
</dl>

<dl>
<dd>

**webhook_failure_notification:** `typing.Optional[bool]` — If true, a notification will also be sent by email in case the webhook request fails all the retries.  The email notification will be sent to the requesting user or their organization’s admin if part of one.
    
</dd>
</dl>

<dl>
<dd>

**webhook_authorization:** `typing.Optional[str]` — Optional custom header for webhook requests. Format: `Key:Value` (e.g., `Authorization:Bearer token123`). This will be sent as an HTTP header in the webhook call.
    
</dd>
</dl>

<dl>
<dd>

**file:** `typing.Optional[core.File]` — The PDF file to be processed. If this parameter is not provided, you must specify `file_id` to use a previously uploaded file.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">pdf_unrestrict</a>(...) -> PdfUnrestrictResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API removes permission restrictions from a PDF while keeping it encrypted. If you want to remove all security (including encryption), use the `/pdf/decrypt` endpoint instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.pdf_unrestrict(
    api_key="apiKey",
    file_password="file_password",
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**file_password:** `str` — The password to unlock the input file. Either the owner password or user password can be provided. The owner password takes precedence. Password Length should be between 6 and 128 characters.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[PdfUnrestrictRequestFormat]` — Specifies the desired format for the API response. Choose 'json' for a JSON object or 'xml' for an XML structure.
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `typing.Optional[str]` — The unique ID of a PDF file already uploaded to the API Freaks server. Use this as an alternative to uploading a new file directly.
    
</dd>
</dl>

<dl>
<dd>

**destroy:** `typing.Optional[bool]` — If set to `true`, the input file(s) will be permanently deleted from the server immediately after the output PDF is generated.
    
</dd>
</dl>

<dl>
<dd>

**output:** `typing.Optional[str]` — The desired name for the output unrestricted PDF file. If not provided, a default name will be assigned.
    
</dd>
</dl>

<dl>
<dd>

**user_password:** `typing.Optional[str]` — Sets the user password for the PDF file. Password Length should be between 6 and 128 characters.
    
</dd>
</dl>

<dl>
<dd>

**owner_password:** `typing.Optional[str]` — Sets the owner password for the PDF file. If the owner password is not provided, the `user_password` will also be used as the owner password. Password Length should be between 6 and 128 characters.
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — The URL to which the webhook notification will be sent after the task is completed.
    
</dd>
</dl>

<dl>
<dd>

**webhook_failure_notification:** `typing.Optional[bool]` — If true, a notification will also be sent by email in case the webhook request fails all the retries.  The email notification will be sent to the requesting user or their organization’s admin if part of one.
    
</dd>
</dl>

<dl>
<dd>

**webhook_authorization:** `typing.Optional[str]` — Optional custom header for webhook requests. Format: `Key:Value` (e.g., `Authorization:Bearer token123`). This will be sent as an HTTP header in the webhook call.
    
</dd>
</dl>

<dl>
<dd>

**file:** `typing.Optional[core.File]` — The PDF file to be processed. If this parameter is not provided, you must specify `file_id` to use a previously uploaded file.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">pdf_convert_to_png</a>(...) -> PdfConvertToPngResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API converts a given PDF file into a sequence of PNG images.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.pdf_convert_to_png(
    api_key="apiKey",
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[PdfConvertToPngRequestFormat]` — Specifies the desired format for the API response. Choose 'json' for a JSON object or 'xml' for an XML structure.
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `typing.Optional[str]` — The unique ID of a PDF file already uploaded to the API Freaks server. Use this as an alternative to uploading a new file directly.
    
</dd>
</dl>

<dl>
<dd>

**destroy:** `typing.Optional[bool]` — If set to `true`, the input file(s) will be permanently deleted from the server immediately after the output PDF is generated.
    
</dd>
</dl>

<dl>
<dd>

**output:** `typing.Optional[str]` — The desired name for the output unrestricted PDF file. If not provided, a default name will be assigned.
    
</dd>
</dl>

<dl>
<dd>

**pages:** `typing.Optional[str]` — Specifies the pages or ranges at which to split the PDF. Accepts individual page numbers (e.g., '1') and/or page ranges (e.g., '4-2', 'last'). Ranges can be ascending or descending. Use commas to separate entries and hyphens for ranges. Alternatively, provide only one of the following keywords: 'even' (split at every even-numbered page), 'odd' (split at every odd-numbered page), 'last' (split at the last page only), or 'all' (split into single pages). Examples: '1,4-2,last', 'odd', 'all'. Mixing special keywords with specific pages/ranges is not allowed.
    
</dd>
</dl>

<dl>
<dd>

**resolution:** `typing.Optional[int]` — Specifies the resolution (in DPI) for the output images. Acceptable Range is from 20 to 1200.
    
</dd>
</dl>

<dl>
<dd>

**image_smoothing:** `typing.Optional[str]` — Determines the smoothing options to apply during image conversion. Valid values are 'none', 'all' or a combination of 'text', 'line', and 'image' (comma-separated).If not provided, no smoothing will be applied.
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[PdfConvertToPngRequestProfile]` — Specifies the color profile for the output PNG images. Acceptable values: bw (1-bit black & white, smallest size, no grayscale or color), gray (8-bit grayscale), rgb (24-bit RGB color, default), rgba (32-bit RGB color with alpha channel for transparency), 4-bit (4-bit indexed color, up to 16 colors, smaller size), or 8-bit (8-bit indexed color, up to 256 colors).
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — The URL to which the webhook notification will be sent after the task is completed.
    
</dd>
</dl>

<dl>
<dd>

**webhook_failure_notification:** `typing.Optional[bool]` — If true, a notification will also be sent by email in case the webhook request fails all the retries.  The email notification will be sent to the requesting user or their organization’s admin if part of one.
    
</dd>
</dl>

<dl>
<dd>

**webhook_authorization:** `typing.Optional[str]` — Optional custom header for webhook requests. Format: `Key:Value` (e.g., `Authorization:Bearer token123`). This will be sent as an HTTP header in the webhook call.
    
</dd>
</dl>

<dl>
<dd>

**file:** `typing.Optional[core.File]` — The PDF file to be processed. If this parameter is not provided, you must specify `file_id` to use a previously uploaded file.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">pdf_convert_to_jpg</a>(...) -> PdfConvertToJpgResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API converts a given PDF file into a sequence of JPG images.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.pdf_convert_to_jpg(
    api_key="apiKey",
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[PdfConvertToJpgRequestFormat]` — Specifies the desired format for the API response. Choose 'json' for a JSON object or 'xml' for an XML structure.
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `typing.Optional[str]` — The unique ID of a PDF file already uploaded to the API Freaks server. Use this as an alternative to uploading a new file directly.
    
</dd>
</dl>

<dl>
<dd>

**destroy:** `typing.Optional[bool]` — If set to `true`, the input file(s) will be permanently deleted from the server immediately after the output PDF is generated.
    
</dd>
</dl>

<dl>
<dd>

**output:** `typing.Optional[str]` — The desired name for the output unrestricted PDF file. If not provided, a default name will be assigned.
    
</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[int]` — Controls JPG compression quality. Higher values yield sharper images with larger file sizes.
    
</dd>
</dl>

<dl>
<dd>

**pages:** `typing.Optional[str]` — Specifies the pages or ranges at which to split the PDF. Accepts individual page numbers (e.g., '1') and/or page ranges (e.g., '4-2', 'last'). Ranges can be ascending or descending. Use commas to separate entries and hyphens for ranges. Alternatively, provide only one of the following keywords: 'even' (split at every even-numbered page), 'odd' (split at every odd-numbered page), 'last' (split at the last page only), or 'all' (split into single pages). Examples: '1,4-2,last', 'odd', 'all'. Mixing special keywords with specific pages/ranges is not allowed.
    
</dd>
</dl>

<dl>
<dd>

**resolution:** `typing.Optional[int]` — Specifies the resolution (in DPI) for the output images. Acceptable Range is from 20 to 1200.
    
</dd>
</dl>

<dl>
<dd>

**image_smoothing:** `typing.Optional[str]` — Determines the smoothing options to apply during image conversion. Valid values are 'none', 'all' or a combination of 'text', 'line', and 'image' (comma-separated).If not provided, no smoothing will be applied.
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[PdfConvertToJpgRequestProfile]` — Specifies the color profile for the output PNG images. Acceptable values: bw (1-bit black & white, smallest size, no grayscale or color), gray (8-bit grayscale), rgb (24-bit RGB color, default), rgba (32-bit RGB color with alpha channel for transparency), 4-bit (4-bit indexed color, up to 16 colors, smaller size), or 8-bit (8-bit indexed color, up to 256 colors).
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — The URL to which the webhook notification will be sent after the task is completed.
    
</dd>
</dl>

<dl>
<dd>

**webhook_failure_notification:** `typing.Optional[bool]` — If true, a notification will also be sent by email in case the webhook request fails all the retries.  The email notification will be sent to the requesting user or their organization’s admin if part of one.
    
</dd>
</dl>

<dl>
<dd>

**webhook_authorization:** `typing.Optional[str]` — Optional custom header for webhook requests. Format: `Key:Value` (e.g., `Authorization:Bearer token123`). This will be sent as an HTTP header in the webhook call.
    
</dd>
</dl>

<dl>
<dd>

**file:** `typing.Optional[core.File]` — The PDF file to be processed. If this parameter is not provided, you must specify `file_id` to use a previously uploaded file.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">pdf_convert_to_tiff</a>(...) -> PdfConvertToTiffResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API converts a given PDF file into a sequence of TIFF images. The output images can be saved as a single TIFF file, or as a sequence of TIFF files.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.pdf_convert_to_tiff(
    api_key="apiKey",
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[PdfConvertToTiffRequestFormat]` — Specifies the desired format for the API response. Choose 'json' for a JSON object or 'xml' for an XML structure.
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `typing.Optional[str]` — The unique ID of a PDF file already uploaded to the API Freaks server. Use this as an alternative to uploading a new file directly.
    
</dd>
</dl>

<dl>
<dd>

**destroy:** `typing.Optional[bool]` — If set to `true`, the input file(s) will be permanently deleted from the server immediately after the output PDF is generated.
    
</dd>
</dl>

<dl>
<dd>

**output:** `typing.Optional[str]` — The desired name for the output unrestricted PDF file. If not provided, a default name will be assigned.
    
</dd>
</dl>

<dl>
<dd>

**pages:** `typing.Optional[str]` — Specifies the pages or ranges at which to split the PDF. Accepts individual page numbers (e.g., '1') and/or page ranges (e.g., '4-2', 'last'). Ranges can be ascending or descending. Use commas to separate entries and hyphens for ranges. Alternatively, provide only one of the following keywords: 'even' (split at every even-numbered page), 'odd' (split at every odd-numbered page), 'last' (split at the last page only), or 'all' (split into single pages). Examples: '1,4-2,last', 'odd', 'all'. Mixing special keywords with specific pages/ranges is not allowed.
    
</dd>
</dl>

<dl>
<dd>

**resolution:** `typing.Optional[int]` — Specifies the resolution (in DPI) for the output images. Acceptable Range is from 20 to 1200.
    
</dd>
</dl>

<dl>
<dd>

**image_smoothing:** `typing.Optional[str]` — Determines the smoothing options to apply during image conversion. Valid values are 'none', 'all' or a combination of 'text', 'line', and 'image' (comma-separated).If not provided, no smoothing will be applied.
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[PdfConvertToTiffRequestProfile]` — Specifies the color profile for the output PNG images. Acceptable values: bw (1-bit black & white, smallest size, no grayscale or color), gray (8-bit grayscale), rgb (24-bit RGB color, default), rgba (32-bit RGB color with alpha channel for transparency), 4-bit (4-bit indexed color, up to 16 colors, smaller size), or 8-bit (8-bit indexed color, up to 256 colors).
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — The URL to which the webhook notification will be sent after the task is completed.
    
</dd>
</dl>

<dl>
<dd>

**webhook_failure_notification:** `typing.Optional[bool]` — If true, a notification will also be sent by email in case the webhook request fails all the retries.  The email notification will be sent to the requesting user or their organization’s admin if part of one.
    
</dd>
</dl>

<dl>
<dd>

**webhook_authorization:** `typing.Optional[str]` — Optional custom header for webhook requests. Format: `Key:Value` (e.g., `Authorization:Bearer token123`). This will be sent as an HTTP header in the webhook call.
    
</dd>
</dl>

<dl>
<dd>

**file:** `typing.Optional[core.File]` — The PDF file to be processed. If this parameter is not provided, you must specify `file_id` to use a previously uploaded file.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">pdf_convert_to_bmp</a>(...) -> PdfConvertToBmpResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Converts a PDF file to a BMP image.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.pdf_convert_to_bmp(
    api_key="apiKey",
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[PdfConvertToBmpRequestFormat]` — Specifies the desired format for the API response. Choose 'json' for a JSON object or 'xml' for an XML structure.
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `typing.Optional[str]` — The unique ID of a PDF file already uploaded to the API Freaks server. Use this as an alternative to uploading a new file directly.
    
</dd>
</dl>

<dl>
<dd>

**destroy:** `typing.Optional[bool]` — If set to `true`, the input file(s) will be permanently deleted from the server immediately after the output PDF is generated.
    
</dd>
</dl>

<dl>
<dd>

**output:** `typing.Optional[str]` — The desired name for the output unrestricted PDF file. If not provided, a default name will be assigned.
    
</dd>
</dl>

<dl>
<dd>

**pages:** `typing.Optional[str]` — Specifies the pages or ranges at which to split the PDF. Accepts individual page numbers (e.g., '1') and/or page ranges (e.g., '4-2', 'last'). Ranges can be ascending or descending. Use commas to separate entries and hyphens for ranges. Alternatively, provide only one of the following keywords: 'even' (split at every even-numbered page), 'odd' (split at every odd-numbered page), 'last' (split at the last page only), or 'all' (split into single pages). Examples: '1,4-2,last', 'odd', 'all'. Mixing special keywords with specific pages/ranges is not allowed.
    
</dd>
</dl>

<dl>
<dd>

**resolution:** `typing.Optional[int]` — Specifies the resolution (in DPI) for the output images. Acceptable Range is from 20 to 1200.
    
</dd>
</dl>

<dl>
<dd>

**image_smoothing:** `typing.Optional[str]` — Determines the smoothing options to apply during image conversion. Valid values are 'none', 'all' or a combination of 'text', 'line', and 'image' (comma-separated).If not provided, no smoothing will be applied.
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[PdfConvertToBmpRequestProfile]` — Specifies the color profile for the output PNG images. Acceptable values: bw (1-bit black & white, smallest size, no grayscale or color), gray (8-bit grayscale), rgb (24-bit RGB color, default), rgba (32-bit RGB color with alpha channel for transparency), 4-bit (4-bit indexed color, up to 16 colors, smaller size), or 8-bit (8-bit indexed color, up to 256 colors).
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — The URL to which the webhook notification will be sent after the task is completed.
    
</dd>
</dl>

<dl>
<dd>

**webhook_failure_notification:** `typing.Optional[bool]` — If true, a notification will also be sent by email in case the webhook request fails all the retries.  The email notification will be sent to the requesting user or their organization’s admin if part of one.
    
</dd>
</dl>

<dl>
<dd>

**webhook_authorization:** `typing.Optional[str]` — Optional custom header for webhook requests. Format: `Key:Value` (e.g., `Authorization:Bearer token123`). This will be sent as an HTTP header in the webhook call.
    
</dd>
</dl>

<dl>
<dd>

**file:** `typing.Optional[core.File]` — The PDF file to be processed. If this parameter is not provided, you must specify `file_id` to use a previously uploaded file.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">pdf_convert_to_gif</a>(...) -> PdfConvertToGifResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API converts a given PDF file into a sequence of GIF images.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.pdf_convert_to_gif(
    api_key="apiKey",
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[PdfConvertToGifRequestFormat]` — Specifies the desired format for the API response. Choose 'json' for a JSON object or 'xml' for an XML structure.
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `typing.Optional[str]` — The unique ID of a PDF file already uploaded to the API Freaks server. Use this as an alternative to uploading a new file directly.
    
</dd>
</dl>

<dl>
<dd>

**destroy:** `typing.Optional[bool]` — If set to `true`, the input file(s) will be permanently deleted from the server immediately after the output PDF is generated.
    
</dd>
</dl>

<dl>
<dd>

**output:** `typing.Optional[str]` — The desired name for the output unrestricted PDF file. If not provided, a default name will be assigned.
    
</dd>
</dl>

<dl>
<dd>

**pages:** `typing.Optional[str]` — Specifies the pages or ranges at which to split the PDF. Accepts individual page numbers (e.g., '1') and/or page ranges (e.g., '4-2', 'last'). Ranges can be ascending or descending. Use commas to separate entries and hyphens for ranges. Alternatively, provide only one of the following keywords: 'even' (split at every even-numbered page), 'odd' (split at every odd-numbered page), 'last' (split at the last page only), or 'all' (split into single pages). Examples: '1,4-2,last', 'odd', 'all'. Mixing special keywords with specific pages/ranges is not allowed.
    
</dd>
</dl>

<dl>
<dd>

**resolution:** `typing.Optional[int]` — Specifies the resolution (in DPI) for the output images. Acceptable Range is from 20 to 1200.
    
</dd>
</dl>

<dl>
<dd>

**image_smoothing:** `typing.Optional[str]` — Determines the smoothing options to apply during image conversion. Valid values are 'none', 'all' or a combination of 'text', 'line', and 'image' (comma-separated).If not provided, no smoothing will be applied.
    
</dd>
</dl>

<dl>
<dd>

**profile:** `typing.Optional[PdfConvertToGifRequestProfile]` — Specifies the color profile for the output PNG images. Acceptable values: bw (1-bit black & white, smallest size, no grayscale or color), gray (8-bit grayscale), rgb (24-bit RGB color, default), rgba (32-bit RGB color with alpha channel for transparency), 4-bit (4-bit indexed color, up to 16 colors, smaller size), or 8-bit (8-bit indexed color, up to 256 colors).
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — The URL to which the webhook notification will be sent after the task is completed.
    
</dd>
</dl>

<dl>
<dd>

**webhook_failure_notification:** `typing.Optional[bool]` — If true, a notification will also be sent by email in case the webhook request fails all the retries.  The email notification will be sent to the requesting user or their organization’s admin if part of one.
    
</dd>
</dl>

<dl>
<dd>

**webhook_authorization:** `typing.Optional[str]` — Optional custom header for webhook requests. Format: `Key:Value` (e.g., `Authorization:Bearer token123`). This will be sent as an HTTP header in the webhook call.
    
</dd>
</dl>

<dl>
<dd>

**file:** `typing.Optional[core.File]` — The PDF file to be processed. If this parameter is not provided, you must specify `file_id` to use a previously uploaded file.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">pdf_upload_resources</a>(...) -> PdfUploadResourcesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API uploads multiple PDF files to the API Freaks server and generates their unique file IDs.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.pdf_upload_resources(
    api_key="apiKey",
    file=["example_file"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[PdfUploadResourcesRequestFormat]` — Specifies the desired format for the API response. Choose 'json' for a JSON object or 'xml' for an XML structure.
    
</dd>
</dl>

<dl>
<dd>

**file:** `typing.Optional[typing.List[core.File]]` — The PDF files to be uploaded to the API Freaks server. Multiple files can be provided in an array.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">pdf_upload_binary</a>(...) -> PdfUploadBinaryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API uploads PDF files to the API Freaks server in binary format.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.pdf_upload_binary(...)
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**file_name:** `str` 

The desired name for the uploaded PDF file. This name will be used for storage on the server.


 **NOTE**: Please ensure file_name has extension `.pdf`.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[PdfUploadBinaryRequestFormat]` — Specifies the desired format for the API response. Choose 'json' for a JSON object or 'xml' for an XML structure.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">pdf_download_resource</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API downloads PDF files or ZIP archives from the server using their unique resource ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.pdf_download_resource(
    api_key="apiKey",
    resource_id="resource_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**resource_id:** `str` — The unique identifier of the file or ZIP archive to download.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[PdfDownloadResourceRequestFormat]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">pdf_get_task_status</a>(...) -> PdfGetTaskStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API checks the status of a previously initiated PDF processing task using its unique task ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.pdf_get_task_status(
    api_key="apiKey",
    task_id="task_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**task_id:** `str` — The unique ID of the PDF processing task for which the status is requested.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[PdfGetTaskStatusRequestFormat]` — Specifies the desired format for the API response. Choose 'json' for a JSON object or 'xml' for an XML structure.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">pdf_get_file_status</a>(...) -> PdfGetFileStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API checks the status of a PDF file using its unique file ID, providing information about its creation and potential deletion time.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.pdf_get_file_status(
    api_key="apiKey",
    file_id="file_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `str` — The unique ID of the file whose status is requested.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[PdfGetFileStatusRequestFormat]` — Specifies the desired format for the API response. Choose 'json' for a JSON object or 'xml' for an XML structure.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">pdf_list_files</a>(...) -> PdfListFilesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API retrieves a list of all PDF files uploaded and generated by a specific user. Please note that if the user is part of an organization, only the Organization Administrator can access this endpoint. Organization Members cannot access this endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.pdf_list_files(
    api_key="apiKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[PdfListFilesRequestFormat]` — Specifies the desired format for the API response. Choose 'json' for a JSON object or 'xml' for an XML structure.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">pdf_delete_file</a>(...) -> PdfDeleteFileResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API deletes a PDF file using its unique file ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.pdf_delete_file(
    api_key="apiKey",
    file_id="file_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `str` — The unique ID of the file to be deleted.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[PdfDeleteFileRequestFormat]` — Specifies the desired format for the API response. Choose 'json' for a JSON object or 'xml' for an XML structure.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">screenshot_capture</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Capture full-page screenshots and videos of websites with advanced options like device simulation, custom code injection, cookie banner blocking, and scrollable content recording.
Supports multiple output formats including JSON, image, GIF, MP4, and WebM.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.screenshot_capture(
    api_key="apiKey",
    url="url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — URLs to capture screenshots of
    
</dd>
</dl>

<dl>
<dd>

**output:** `typing.Optional[ScreenshotCaptureRequestOutput]` — Output format for screenshot results
    
</dd>
</dl>

<dl>
<dd>

**file_type:** `typing.Optional[ScreenshotCaptureRequestFileType]` — File type for screenshot output
    
</dd>
</dl>

<dl>
<dd>

**width:** `typing.Optional[int]` — Browser viewport width in pixels
    
</dd>
</dl>

<dl>
<dd>

**height:** `typing.Optional[int]` — Browser viewport height in pixels
    
</dd>
</dl>

<dl>
<dd>

**full_page:** `typing.Optional[bool]` — Capture a full-page screenshot
    
</dd>
</dl>

<dl>
<dd>

**fresh:** `typing.Optional[bool]` — Bypass cache and take a fresh screenshot
    
</dd>
</dl>

<dl>
<dd>

**no_cookie_banners:** `typing.Optional[bool]` — Remove cookie banners from the screenshot
    
</dd>
</dl>

<dl>
<dd>

**enable_caching:** `typing.Optional[bool]` — Enable caching for repeated requests
    
</dd>
</dl>

<dl>
<dd>

**block_ads:** `typing.Optional[bool]` — Block advertisements on the page
    
</dd>
</dl>

<dl>
<dd>

**block_chat_widgets:** `typing.Optional[bool]` — Block chat widget scripts from loading
    
</dd>
</dl>

<dl>
<dd>

**extract_text:** `typing.Optional[bool]` — Extract visible text from the page
    
</dd>
</dl>

<dl>
<dd>

**extract_html:** `typing.Optional[bool]` — Extract HTML content of the page
    
</dd>
</dl>

<dl>
<dd>

**destroy_screenshot:** `typing.Optional[bool]` — Auto-destroy screenshot after fetch
    
</dd>
</dl>

<dl>
<dd>

**lazy_load:** `typing.Optional[bool]` — Enable lazy-loading content before screenshot
    
</dd>
</dl>

<dl>
<dd>

**retina:** `typing.Optional[bool]` — Capture screenshot in high-DPI (Retina) mode
    
</dd>
</dl>

<dl>
<dd>

**dark_mode:** `typing.Optional[bool]` — Render page in dark mode
    
</dd>
</dl>

<dl>
<dd>

**block_tracking:** `typing.Optional[bool]` — Block common user-tracking scripts
    
</dd>
</dl>

<dl>
<dd>

**enable_incognito:** `typing.Optional[bool]` — Enable private/incognito mode for browser session
    
</dd>
</dl>

<dl>
<dd>

**omit_background:** `typing.Optional[bool]` — Omit background color (transparent background)
    
</dd>
</dl>

<dl>
<dd>

**thumbnail_width:** `typing.Optional[int]` — Thumbnail width in pixels
    
</dd>
</dl>

<dl>
<dd>

**adjust_top:** `typing.Optional[int]` — Adjust top in pixels
    
</dd>
</dl>

<dl>
<dd>

**wait_for_event:** `typing.Optional[ScreenshotCaptureRequestWaitForEvent]` — Wait for a specific load event before capturing the screenshot.
    
</dd>
</dl>

<dl>
<dd>

**grayscale:** `typing.Optional[int]` — Range:0 to 100 for grayscale filter
    
</dd>
</dl>

<dl>
<dd>

**delay:** `typing.Optional[int]` — How many milliseconds to wait before taking the screenshot
    
</dd>
</dl>

<dl>
<dd>

**timeout:** `typing.Optional[int]` — Maximum timeout in milliseconds. Defalut is `10,000`
    
</dd>
</dl>

<dl>
<dd>

**ttl:** `typing.Optional[int]` — Number of seconds the screenshot should be cached
    
</dd>
</dl>

<dl>
<dd>

**clip_x:** `typing.Optional[int]` — X position of the clipping rectangle in pixels
    
</dd>
</dl>

<dl>
<dd>

**clip_y:** `typing.Optional[int]` — Y position of the clipping rectangle in pixels
    
</dd>
</dl>

<dl>
<dd>

**clip_width:** `typing.Optional[int]` — Width of the clipping rectangle in pixels
    
</dd>
</dl>

<dl>
<dd>

**clip_height:** `typing.Optional[int]` — Height of the clipping rectangle in pixels
    
</dd>
</dl>

<dl>
<dd>

**css_url:** `typing.Optional[str]` — URL to CSS file
    
</dd>
</dl>

<dl>
<dd>

**css:** `typing.Optional[str]` — Your custom CSS code
    
</dd>
</dl>

<dl>
<dd>

**js_url:** `typing.Optional[str]` — URL to JS file
    
</dd>
</dl>

<dl>
<dd>

**js:** `typing.Optional[str]` — Your JS code
    
</dd>
</dl>

<dl>
<dd>

**block_js:** `typing.Optional[bool]` — Block Scripts
    
</dd>
</dl>

<dl>
<dd>

**block_stylesheets:** `typing.Optional[bool]` — Block Stylesheets
    
</dd>
</dl>

<dl>
<dd>

**block_images:** `typing.Optional[bool]` — Block Images
    
</dd>
</dl>

<dl>
<dd>

**block_media:** `typing.Optional[bool]` — Block Media
    
</dd>
</dl>

<dl>
<dd>

**block_font:** `typing.Optional[bool]` — Block Fonts
    
</dd>
</dl>

<dl>
<dd>

**block_text_track:** `typing.Optional[bool]` — Block Text Tracks
    
</dd>
</dl>

<dl>
<dd>

**block_xhr:** `typing.Optional[bool]` — Block XHR Requests
    
</dd>
</dl>

<dl>
<dd>

**block_fetch:** `typing.Optional[bool]` — Block Fetch Requests
    
</dd>
</dl>

<dl>
<dd>

**block_event_source:** `typing.Optional[bool]` — Block Event Source
    
</dd>
</dl>

<dl>
<dd>

**block_web_socket:** `typing.Optional[bool]` — Block Web Sockets
    
</dd>
</dl>

<dl>
<dd>

**block_manifest:** `typing.Optional[bool]` — Block Manifest
    
</dd>
</dl>

<dl>
<dd>

**block_specific_requests:** `typing.Optional[str]` — Comma- or newline-separated list of specific requests to block. Each line and comma are treated as separate requests for processing. Example: https://example.com, https://example.js
    
</dd>
</dl>

<dl>
<dd>

**blur_selector:** `typing.Optional[str]` 

Comma-separated list of indexed CSS selectors to blur.
Format: `index:<selector>`, e.g., `0:.banner,1:#ads`.
    
</dd>
</dl>

<dl>
<dd>

**remove_selector:** `typing.Optional[str]` 

Comma-separated list of indexed CSS selectors to blur.
Format: `index:<selector>`, e.g., `0:.banner,1:#ads`.
    
</dd>
</dl>

<dl>
<dd>

**result_file_name:** `typing.Optional[str]` 

Specify a meaningful & unique file name to easily identify the screenshot result.
Avoid using spaces or special characters; use hyphens or underscores to separate words.
    
</dd>
</dl>

<dl>
<dd>

**scrolling_screenshot:** `typing.Optional[bool]` — **`Scrolling Screenshot`**: Capture a long scrolling screenshot. When true, disable `fullPage` and `freshScreenshot`.
    
</dd>
</dl>

<dl>
<dd>

**scroll_speed:** `typing.Optional[ScreenshotCaptureRequestScrollSpeed]` — Speed of scrolling during the screenshot.
    
</dd>
</dl>

<dl>
<dd>

**scroll_back:** `typing.Optional[bool]` — If true, the scroll will reverse back to the top after reaching the bottom.
    
</dd>
</dl>

<dl>
<dd>

**start_immediately:** `typing.Optional[bool]` — If true, the scrolling capture will start immediately upon page load.
    
</dd>
</dl>

<dl>
<dd>

**multiple_scrolling:** `typing.Optional[bool]` — If true, multiple scrolling screenshots will be taken at different viewport sizes.
    
</dd>
</dl>

<dl>
<dd>

**sizes:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma-separated list of viewport sizes in the format index:XXw:YYh. Example: sizes=0:120w:300h,1:240w:500h
    
</dd>
</dl>

<dl>
<dd>

**duration:** `typing.Optional[float]` — Duration in seconds for the scrolling capture. Acceptable range: 0 to 100 seconds.
    
</dd>
</dl>

<dl>
<dd>

**fail_on_error:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**longitude:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**latitude:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**proxy:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cookies:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**scroll_to_element:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**selector:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**user_agent:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**accept_languages:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**custom_html:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**image_quality:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">bulk_screenshot_capture</a>(...) -> BulkScreenshotCaptureResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Our Bulk Screenshot API allows you to capture screenshots of multiple webpages simultaneously, saving you time and effort. Instead of manually capturing each page one by one, you can batch process URLs and receive high-quality screenshots in the format you choose.
 Maximum `50 URLs` per request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi, BulkScreenshotCaptureRequestUrlsItem
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.bulk_screenshot_capture(
    api_key="apiKey",
    urls=[
        BulkScreenshotCaptureRequestUrlsItem(
            url="url",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**urls:** `typing.List[BulkScreenshotCaptureRequestUrlsItem]` — List of website URLs to capture screenshots of
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[BulkScreenshotCaptureRequestFormat]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">currency_latest_rates</a>(...) -> CurrencyLatestRatesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get live forex rates for all world currencies with customizable update frequency
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.currency_latest_rates(
    api_key="apiKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[CurrencyLatestRatesRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**base:** `typing.Optional[str]` — Base currency for rate calculations
    
</dd>
</dl>

<dl>
<dd>

**symbols:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma separated list of desired currency codes
    
</dd>
</dl>

<dl>
<dd>

**updates:** `typing.Optional[CurrencyLatestRatesRequestUpdates]` — Exchange rates update period (1d=daily, 1h=hourly, 10m=10 minutes, 1m=1 minute)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">currency_historical_rates</a>(...) -> CurrencyHistoricalRatesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get historical exchange rates for any specific date
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment
import datetime

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.currency_historical_rates(
    api_key="apiKey",
    date=datetime.date.fromisoformat("2023-01-15"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**date:** `datetime.date` — Specific date in YYYY-MM-DD format
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[CurrencyHistoricalRatesRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**base:** `typing.Optional[str]` — Base currency for rate calculations
    
</dd>
</dl>

<dl>
<dd>

**symbols:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma separated list of desired currency codes
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">currency_convert_latest</a>(...) -> CurrencyConvertLatestResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Convert amount between currencies using the latest exchange rates
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.currency_convert_latest(
    api_key="apiKey",
    from_="from",
    to="to",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**from:** `str` — Source currency code
    
</dd>
</dl>

<dl>
<dd>

**to:** `str` — Target currency code
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[CurrencyConvertLatestRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**amount:** `typing.Optional[float]` — Amount to convert
    
</dd>
</dl>

<dl>
<dd>

**updates:** `typing.Optional[CurrencyConvertLatestRequestUpdates]` — Exchange rates update period (1d=daily, 1h=hourly, 10m=10 minutes, 1m=1 minute)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">currency_convert_historical</a>(...) -> CurrencyConvertHistoricalResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Convert amount between currencies using historical rates
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment
import datetime

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.currency_convert_historical(
    api_key="apiKey",
    from_="from",
    to="to",
    date=datetime.date.fromisoformat("2023-01-15"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**from:** `str` — From currency symbol
    
</dd>
</dl>

<dl>
<dd>

**to:** `str` — To currency symbol
    
</dd>
</dl>

<dl>
<dd>

**date:** `datetime.date` — specific date (format YYYY-MM-DD) of which exchange rates is used.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[CurrencyConvertHistoricalRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**amount:** `typing.Optional[float]` — The Amount to be converted
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">currency_time_series</a>(...) -> CurrencyTimeSeriesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get exchange rates for a time range
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment
import datetime

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.currency_time_series(
    api_key="apiKey",
    start_date=datetime.date.fromisoformat("2023-01-15"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `datetime.date` — Start date (format YYYY-MM-DD) of the preferred time frame
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[CurrencyTimeSeriesRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.date]` — End date (format YYYY-MM-DD) of the preferred time frame
    
</dd>
</dl>

<dl>
<dd>

**base:** `typing.Optional[str]` — Base currency
    
</dd>
</dl>

<dl>
<dd>

**symbols:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — comma separated list of desired currencies/ commodities symbols
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">currency_fluctuation</a>(...) -> CurrencyFluctuationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get currency fluctuation data for a time period
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment
import datetime

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.currency_fluctuation(
    api_key="apiKey",
    start_date=datetime.date.fromisoformat("2023-01-15"),
    base="USD",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `datetime.date` — Start date (format YYYY-MM-DD) of the preferred time frame
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[CurrencyFluctuationRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.date]` — End date (format YYYY-MM-DD) of the preferred time frame
    
</dd>
</dl>

<dl>
<dd>

**base:** `typing.Optional[str]` — Base currency
    
</dd>
</dl>

<dl>
<dd>

**symbols:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — comma separated list of desired currencies/ commodities symbols
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">currency_convert_by_ip</a>(...) -> CurrencyConvertByIpResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Convert amount using user's location
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.currency_convert_by_ip(
    api_key="apiKey",
    from_="from",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**from:** `str` — From currency symbol
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[CurrencyConvertByIpRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**updates:** `typing.Optional[CurrencyConvertByIpRequestUpdates]` — Exchange rates update period (1d=daily, 1h=hourly, 10m=10 minutes, 1m=1 minute)
    
</dd>
</dl>

<dl>
<dd>

**ip:** `typing.Optional[str]` — IPv4 or IPv6 geolocated currency
    
</dd>
</dl>

<dl>
<dd>

**amount:** `typing.Optional[float]` — Amount to convert
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">currency_supported</a>(...) -> CurrencySupportedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get list of all supported currencies with their metadata
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.currency_supported(
    api_key="apiKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[CurrencySupportedRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">currency_symbols</a>(...) -> CurrencySymbolsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get currency symbols and codes
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.currency_symbols(
    api_key="apiKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[CurrencySymbolsRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">currency_historical_limits</a>(...) -> CurrencyHistoricalLimitsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about historical data availability and limits
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.currency_historical_limits(
    api_key="apiKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[CurrencyHistoricalLimitsRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">commodity_latest_rates</a>(...) -> CommodityLatestRatesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get live commodity rates with customizable update frequency
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.commodity_latest_rates(
    api_key="apiKey",
    symbols=[
        "symbols"
    ],
    updates="10m",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**updates:** `CommodityLatestRatesRequestUpdates` — Exchange rates update period. Possible values are: (1) `10m` - 10 minute update (2) `1m` - 1 minute update **Required**
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[CommodityLatestRatesRequestFormat]` — Format of the Response
    
</dd>
</dl>

<dl>
<dd>

**symbols:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma separated list of desired commodities symbols *(e.g. XAU,XAG,WTI,BRENT)* **Required**
    
</dd>
</dl>

<dl>
<dd>

**quote:** `typing.Optional[str]` — Specifies the target currency for the exchange rate; default quote currency is the market currency of commodity *(e.g. USD, EUR, INR)*
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">commodity_historical_rates</a>(...) -> CommodityHistoricalRatesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get historical commodity rates for a specific date
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment
import datetime

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.commodity_historical_rates(
    api_key="apiKey",
    date=datetime.date.fromisoformat("2023-01-15"),
    symbols=[
        "symbols"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**date:** `datetime.date` — Historical date (YYYY-MM-DD)
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[CommodityHistoricalRatesRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**symbols:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma-separated list of commodity symbols
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">commodity_fluctuation</a>(...) -> CommodityFluctuationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get commodity price fluctuation data for a time period
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment
import datetime

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.commodity_fluctuation(
    api_key="apiKey",
    symbols=[
        "symbols"
    ],
    start_date=datetime.date.fromisoformat("2023-01-15"),
    end_date=datetime.date.fromisoformat("2023-01-15"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `datetime.date` — Start date (YYYY-MM-DD)
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `datetime.date` — End date (YYYY-MM-DD)
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[CommodityFluctuationRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**symbols:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma-separated list of commodity symbols
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">commodity_time_series</a>(...) -> CommodityTimeSeriesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get commodity rates for a time range
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment
import datetime

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.commodity_time_series(
    api_key="apiKey",
    symbols=[
        "symbols"
    ],
    start_date=datetime.date.fromisoformat("2023-01-15"),
    end_date=datetime.date.fromisoformat("2023-01-15"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `datetime.date` — Start date (YYYY-MM-DD)
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `datetime.date` — End date (YYYY-MM-DD)
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[CommodityTimeSeriesRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**symbols:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma-separated list of commodity symbols
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">commodity_symbols</a>(...) -> CommoditySymbolsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get list of supported commodities
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.commodity_symbols(
    api_key="apiKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[CommoditySymbolsRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">vat_supported_countries</a>(...) -> VatSupportedCountriesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a list of supported countries.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.vat_supported_countries(
    api_key="apiKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[VatSupportedCountriesRequestFormat]` — Format of the response. Default is JSON.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[VatSupportedCountriesRequestType]` — Type of supported country. Supported values: IBAN, SWIFT, VAT. By default, it returns all supported countries for all types.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">vat_rate_by_ip</a>(...) -> typing.List[VatRateByIpResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches VAT rate based on the specified or originating IP address.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.vat_rate_by_ip(
    api_key="apiKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[VatRateByIpRequestFormat]` — Specify the desired response format. Options: 'json' (default) or 'xml'.
    
</dd>
</dl>

<dl>
<dd>

**ip_address:** `typing.Optional[str]` — IPv4 or IPv6 address to look up VAT rate for. If omitted, the originating IP address will be used.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">vat_rate_by_country</a>(...) -> typing.List[VatRateByCountryResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches VAT rates for a single country or state provided via query parameters.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.vat_rate_by_country(
    api_key="apiKey",
    country="country",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**country:** `str` — Country identifier in Alpha-2 (PK), Alpha-3 (PAK), or full name (Pakistan). Combine with the optional "state" query for sub-national VAT; values are case-insensitive and may use underscores instead of spaces.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[VatRateByCountryRequestFormat]` — Specify the desired response format. Options: 'json' (default) or 'xml'.
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[str]` — Optional state or region in Alpha-2 (NY) or full name (New_York). Use with "country" for state-level VAT; values are case-insensitive and may use underscores.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">bulk_vat_rate_by_country</a>(...) -> BulkVatRateByCountryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves VAT details for multiple countries or country-state combinations in a single request. Maximum of `100` entries per request are allowed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi, BulkVatRateByCountryRequestCountriesItem
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.bulk_vat_rate_by_country(
    api_key="apiKey",
    countries=[
        BulkVatRateByCountryRequestCountriesItem(
            country="PAK",
        ),
        BulkVatRateByCountryRequestCountriesItem(
            country="United_States",
            state="New_York",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**countries:** `typing.List[BulkVatRateByCountryRequestCountriesItem]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[BulkVatRateByCountryRequestFormat]` — Specify the desired response format. Options: 'json' (default) or 'xml'.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">vat_validate</a>(...) -> VatValidateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Validates an EU or UK VAT number and returns registration status details.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.vat_validate(
    api_key="apiKey",
    vat_number="vatNumber",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**vat_number:** `str` — EU or UK VAT number to validate.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[VatValidateRequestFormat]` — Specify the desired response format. Options: 'json' (default) or 'xml'.
    
</dd>
</dl>

<dl>
<dd>

**requester_vat_number:** `typing.Optional[str]` — Requester EU or UK VAT number.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">iban_validate</a>(...) -> IbanValidateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Checks an IBAN for structural validity, checksum accuracy, and bank metadata.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.iban_validate(
    api_key="apiKey",
    iban="iban",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**iban:** `str` — IBAN to validate.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[IbanValidateRequestFormat]` — Specify the desired response format. Options: 'json' (default) or 'xml'.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">swift_code_find</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches SWIFT codes for a given country, bank, and city.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.swift_code_find(
    api_key="apiKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[SwiftCodeFindRequestFormat]` — Specify the desired response format. Options: 'json' (default) or 'xml'.
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` — Country name (accepts full name, e.g., Pakistan, United States). If only the country parameter is supplied, lists all banks in the country.
    
</dd>
</dl>

<dl>
<dd>

**bank:** `typing.Optional[str]` — Bank name (upper case) used to filter SWIFT codes. Should be used together with the country parameter. If only country and bank are provided (without city), returns the list of cities for that bank.
    
</dd>
</dl>

<dl>
<dd>

**city:** `typing.Optional[str]` — Gives SWIFT codes for a bank. Optionally specify the city (upper case) to narrow results to a specific city for that bank.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">swift_code_lookup</a>(...) -> SwiftCodeLookupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches detailed information about a SWIFT code.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.swift_code_lookup(
    api_key="apiKey",
    swift_code="swiftCode",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**swift_code:** `str` — SWIFT/BIC code to lookup (must be 8 or 11 characters).
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[SwiftCodeLookupRequestFormat]` — Specify the desired response format. Options: 'json' (default) or 'xml'.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">zipcode_lookup</a>(...) -> ZipcodeLookupResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.zipcode_lookup(
    api_key="apiKey",
    code="code",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**code:** `str` — Comma separated list of postal / zip codes. Max. 100 values.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[ZipcodeLookupRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` — Country code in ISO 3166-1 alpha-2 format. If not provided, search results will be returned from all countries.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">bulk_zipcode_lookup</a>(...) -> BulkZipcodeLookupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Validates a bulk of ZIP/postal codes and returns result for each. Maximum `100` ZIP/postal codes per request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.bulk_zipcode_lookup(
    api_key="apiKey",
    codes=[
        "codes"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**codes:** `typing.List[str]` — Comma separated list of postal / zip codes. Max. 100 values.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[BulkZipcodeLookupRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` — Country code in ISO 3166-1 alpha-2 format. If not provided, search results will be returned from all countries.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">zipcode_search_by_city</a>(...) -> ZipcodeSearchByCityResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.zipcode_search_by_city(
    api_key="apiKey",
    city="city",
    country="country",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**city:** `str` — Name of the city in which we want to find zipcodes in.
    
</dd>
</dl>

<dl>
<dd>

**country:** `str` — Country code in ISO 3166-1 alpha-2 format.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[ZipcodeSearchByCityRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**state_name:** `typing.Optional[str]` — Name of the state or province associated with the country.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number to retrieve paginated results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">zipcode_search_by_region</a>(...) -> ZipcodeSearchByRegionResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.zipcode_search_by_region(
    api_key="apiKey",
    country="country",
    region="region",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**country:** `str` — Country code in ISO 3166-1 alpha-2 format.
    
</dd>
</dl>

<dl>
<dd>

**region:** `str` — Name of the region, state or province associated with the country.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[ZipcodeSearchByRegionRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page no. to retrieve paginated results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">zipcode_search_by_radius</a>(...) -> ZipcodeSearchByRadiusResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.zipcode_search_by_radius(
    api_key="apiKey",
    radius=1.1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**radius:** `float` — Search radius for the query. The maximum allowed values are: - 100 km - 100 mi - 109361 yd - 100000 m - 328084 ft - 3937007.75 in
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[ZipcodeSearchByRadiusRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` — Postal/Zip code to be used as the center point for the search.
    
</dd>
</dl>

<dl>
<dd>

**lat:** `typing.Optional[float]` — Latitude coordinate for the base location.
    
</dd>
</dl>

<dl>
<dd>

**long:** `typing.Optional[float]` — Longitude coordinate for the base location.
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` — Country code in ISO 3166-1 alpha-2 format. Required only when using the code parameter.
    
</dd>
</dl>

<dl>
<dd>

**unit:** `typing.Optional[ZipcodeSearchByRadiusRequestUnit]` — Supported distance units are m, km, mi, ft, yd, in.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page no. to retrieve paginated results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">zipcode_distance</a>(...) -> ZipcodeDistanceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get distance between postal codes. Maximum `100` postal codes per request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.zipcode_distance(
    api_key="apiKey",
    compare=[
        "compare"
    ],
    country="country",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**compare:** `typing.List[str]` — Comma separated list of postal / zip codes with which base point is compared w.r.t. Max 100 zip codes can be provided.
    
</dd>
</dl>

<dl>
<dd>

**country:** `str` — Country code in ISO 3166-1 alpha-2 format.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[ZipcodeDistanceRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` — Postal/Zip code to be used as the base point.
    
</dd>
</dl>

<dl>
<dd>

**lat:** `typing.Optional[float]` — Latitude coordinate for the base location.
    
</dd>
</dl>

<dl>
<dd>

**long:** `typing.Optional[float]` — Longitude coordinate for the base location.
    
</dd>
</dl>

<dl>
<dd>

**unit:** `typing.Optional[ZipcodeDistanceRequestUnit]` — Supported distance units are m, km, mi, ft, yd, in.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">zipcode_distance_match</a>(...) -> ZipcodeDistanceMatchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get matching ZIP/postal code pairs within a specified distance. Maximum `100` postal codes per request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.zipcode_distance_match(
    api_key="apiKey",
    codes=[
        "codes"
    ],
    country="country",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**codes:** `typing.List[str]` — Comma-separated list of postal/zip codes. Maximum 100 values allowed.
    
</dd>
</dl>

<dl>
<dd>

**country:** `str` — Country code in ISO 3166-1 alpha-2 format.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[ZipcodeDistanceMatchRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**distance:** `typing.Optional[float]` — Maximum allowed distance between postal code pairs.
    
</dd>
</dl>

<dl>
<dd>

**unit:** `typing.Optional[ZipcodeDistanceMatchRequestUnit]` — Supported distance units are m, km, mi, ft, yd, in.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">current_weather</a>(...) -> CurrentWeatherResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get current weather data including temperature, humidity, precipitation, wind conditions, atmospheric pressure, and air quality for any location. Accepts city names, coordinates, or IP addresses. Also includes astronomy data and timezone-aware timestamps.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.current_weather(
    api_key="apiKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[CurrentWeatherRequestFormat]` — Response format returned by the API.
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[str]` — City name, place name, or full address.
    
</dd>
</dl>

<dl>
<dd>

**lat:** `typing.Optional[float]` — Latitude of the location.
    
</dd>
</dl>

<dl>
<dd>

**long:** `typing.Optional[float]` — Longitude of the location.
    
</dd>
</dl>

<dl>
<dd>

**ip:** `typing.Optional[str]` — IP(v4 or v6) address for location inference.
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` — Timezone for the results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">bulk_current_weather</a>(...) -> BulkCurrentWeatherResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve current weather conditions for up to `50 locations` in a single request. A maximum of 50 locations (city names, IP addresses, or geographic coordinates) can be included in the request body.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi, BulkCurrentWeatherRequestLocationsItem
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.bulk_current_weather(
    api_key="apiKey",
    locations=[
        BulkCurrentWeatherRequestLocationsItem(
            location="lahore",
        ),
        BulkCurrentWeatherRequestLocationsItem(
            lat=32.5,
            long_=74.5,
        ),
        BulkCurrentWeatherRequestLocationsItem(
            ip="8.8.8.8",
        ),
        BulkCurrentWeatherRequestLocationsItem(
            location="seoul",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**locations:** `typing.List[BulkCurrentWeatherRequestLocationsItem]` — Array of locations to fetch weather data for
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[BulkCurrentWeatherRequestFormat]` — Response format returned by the API.
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` — Timezone for the results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">weather_forecast</a>(...) -> WeatherForecastResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Access comprehensive weather forecasts with customizable precision - choose from daily overviews, hourly breakdowns, or even minute-by-minute data. Configure your date ranges or use the default 7-day forecast for standard weather planning.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.weather_forecast(
    api_key="apiKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[WeatherForecastRequestFormat]` — Response format returned by the API.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.date]` — Start date for the forecast in YYYY-MM-DD format. Forecast dates must be current or future dates only. Past dates are not allowed for forecast data. The difference between startDate and endDate must not exceed 16 days.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.date]` — End date for the forecast in YYYY-MM-DD format. Forecast dates must be current or future dates only. Past dates are not allowed for forecast data. The difference between startDate and endDate must not exceed 16 days.
    
</dd>
</dl>

<dl>
<dd>

**forecast_days:** `typing.Optional[int]` — Number of days for the forecast, from 1 to 16. Default is 7. Maximum value is 16.
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[str]` — City name, place name, or full address.
    
</dd>
</dl>

<dl>
<dd>

**lat:** `typing.Optional[float]` — Latitude of the location.
    
</dd>
</dl>

<dl>
<dd>

**long:** `typing.Optional[float]` — Longitude of the location.
    
</dd>
</dl>

<dl>
<dd>

**ip:** `typing.Optional[str]` — IP(v4 or v6) address for location inference.
    
</dd>
</dl>

<dl>
<dd>

**precision:** `typing.Optional[WeatherForecastRequestPrecision]` — Precision of the forecast data.
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` — Timezone for the results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">historical_weather</a>(...) -> HistoricalWeatherResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Access past weather conditions for specific dates with records going back to 1940. Retrieve comprehensive historical data with both daily and hourly precision options.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment
import datetime

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.historical_weather(
    api_key="apiKey",
    date=datetime.date.fromisoformat("2023-01-15"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**date:** `datetime.date` — Specific date for which to fetch weather data in YYYY-MM-DD format. Historical dates must be past dates only. Current or future dates are not allowed for historical data. Data available from 1940 onwards.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[HistoricalWeatherRequestFormat]` — Response format returned by the API.
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[str]` — City name, place name, or full address.
    
</dd>
</dl>

<dl>
<dd>

**lat:** `typing.Optional[float]` — Latitude of the location.
    
</dd>
</dl>

<dl>
<dd>

**long:** `typing.Optional[float]` — Longitude of the location.
    
</dd>
</dl>

<dl>
<dd>

**ip:** `typing.Optional[str]` — IP(v4 or v6) address for location inference.
    
</dd>
</dl>

<dl>
<dd>

**precision:** `typing.Optional[HistoricalWeatherRequestPrecision]` — Precision of the historical data. **Note:** 'daily' returns daily aggregates, 'hourly' returns hourly data.
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` — Timezone for the results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">weather_time_series</a>(...) -> WeatherTimeSeriesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Pull historical weather information for date ranges up to 90 days (daily data) or 7 days (hourly data). Get consistent formatting across your specified date range with reliable historical weather patterns.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment
import datetime

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.weather_time_series(
    api_key="apiKey",
    start_date=datetime.date.fromisoformat("2023-01-15"),
    end_date=datetime.date.fromisoformat("2023-01-15"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `datetime.date` — Starting date for the data in YYYY-MM-DD format. Historical dates must be past dates only. Current or future dates are not allowed for historical data. Data available from 1940 onwards. For precision=daily, the difference between endDate and startDate must not exceed 90 days. For precision=hourly, the difference must not exceed 7 days.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `datetime.date` — End date for the data in YYYY-MM-DD format. Historical dates must be past dates only. Current or future dates are not allowed for historical data. Data available from 1940 onwards. For precision=daily, the difference between endDate and startDate must not exceed 90 days. For precision=hourly, the difference must not exceed 7 days.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[WeatherTimeSeriesRequestFormat]` — Response format returned by the API.
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[str]` — City name, place name, or full address.
    
</dd>
</dl>

<dl>
<dd>

**lat:** `typing.Optional[float]` — Latitude of the location.
    
</dd>
</dl>

<dl>
<dd>

**long:** `typing.Optional[float]` — Longitude of the location.
    
</dd>
</dl>

<dl>
<dd>

**ip:** `typing.Optional[str]` — IP(v4 or v6) address for location inference.
    
</dd>
</dl>

<dl>
<dd>

**precision:** `typing.Optional[WeatherTimeSeriesRequestPrecision]` — Precision of the data.
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` — Timezone for the results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">marine_weather</a>(...) -> MarineWeatherResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provides hourly forecasts of marine conditions including wave heights, wave directions, wave periods, swell info, sea surface temperatures, and ocean currents. Supports multiple geographical points and returns daily max wave statistics for up to 7 days. Ideal for maritime planning, navigation, and coastal activities.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.marine_weather(
    api_key="apiKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[MarineWeatherRequestFormat]` — Response format returned by the API.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.date]` — Starting date for marine forecast data in YYYY-MM-DD format. Forecast dates must be current or future dates only. Past dates are not allowed for forecast data. The difference between endDate and startDate must not exceed 16 days.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.date]` — End date for marine forecast data in YYYY-MM-DD format. Forecast dates must be current or future dates only. Past dates are not allowed for forecast data. The difference between endDate and startDate must not exceed 16 days.
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[str]` — City name, place name, or full address.
    
</dd>
</dl>

<dl>
<dd>

**lat:** `typing.Optional[float]` — Latitude of the location.
    
</dd>
</dl>

<dl>
<dd>

**long:** `typing.Optional[float]` — Longitude of the location.
    
</dd>
</dl>

<dl>
<dd>

**ip:** `typing.Optional[str]` — IP(v4 or v6) address for location inference.
    
</dd>
</dl>

<dl>
<dd>

**precision:** `typing.Optional[MarineWeatherRequestPrecision]` — Precision of the marine data.
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` — Timezone for the results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">air_quality</a>(...) -> AirQualityResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Monitor and predict air quality conditions using European and US AQI standards. Track pollutant concentrations including PM10, PM2.5, carbon monoxide, nitrogen dioxide, sulfur dioxide, ozone, and dust particles. Get current readings plus hourly forecasts up to 5 days ahead, complete with UV index and aerosol measurements for comprehensive air quality assessment.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.air_quality(
    api_key="apiKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[AirQualityRequestFormat]` — Response format returned by the API.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.date]` — Starting date for AQI forecast data in YYYY-MM-DD format. Forecast dates must be current or future dates only. Past dates are not allowed for forecast data. The difference between endDate and startDate must not exceed 5 days.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.date]` — End date for AQI forecast data in YYYY-MM-DD format. Forecast dates must be current or future dates only. Past dates are not allowed for forecast data. The difference between endDate and startDate must not exceed 5 days.
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[str]` — City name, place name, or full address.
    
</dd>
</dl>

<dl>
<dd>

**lat:** `typing.Optional[float]` — Latitude of the location.
    
</dd>
</dl>

<dl>
<dd>

**long:** `typing.Optional[float]` — Longitude of the location.
    
</dd>
</dl>

<dl>
<dd>

**ip:** `typing.Optional[str]` — IP(v4 or v6) address for location inference.
    
</dd>
</dl>

<dl>
<dd>

**precision:** `typing.Optional[AirQualityRequestPrecision]` — Only hourly precision is supported; returns hourly AQI data for the selected date range.
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` — Timezone for the results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">flood_forecast</a>(...) -> FloodForecastResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provides flood forecast data for a given location, including river discharge metrics such as mean, median, maximum, minimum, and percentile values (p25, p75). Requires a startDate and endDate, with the date range limited to 16 days. Location can be specified using city name, latitude/longitude, or IP address.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment
import datetime

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.flood_forecast(
    api_key="apiKey",
    start_date=datetime.date.fromisoformat("2023-01-15"),
    end_date=datetime.date.fromisoformat("2023-01-15"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `datetime.date` — Starting date for flood forecast data in YYYY-MM-DD format. Forecast dates must be current or future dates only. Past dates are not allowed for forecast data. The difference between endDate and startDate must not exceed 16 days.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `datetime.date` — End date for flood forecast data in YYYY-MM-DD format. Forecast dates must be current or future dates only. Past dates are not allowed for forecast data. The difference between endDate and startDate must not exceed 16 days.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[FloodForecastRequestFormat]` — Response format returned by the API.
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[str]` — City name, place name, or full address.
    
</dd>
</dl>

<dl>
<dd>

**lat:** `typing.Optional[float]` — Latitude of the location.
    
</dd>
</dl>

<dl>
<dd>

**long:** `typing.Optional[float]` — Longitude of the location.
    
</dd>
</dl>

<dl>
<dd>

**ip:** `typing.Optional[str]` — IP(v4 or v6) address for location inference.
    
</dd>
</dl>

<dl>
<dd>

**precision:** `typing.Optional[FloodForecastRequestPrecision]` — Only daily precision is supported; returns flood forecast data for the selected date range.
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` — Timezone for the results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">get_countries</a>(...) -> GetCountriesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve countries, optionally filtered by region or subregion.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.get_countries(
    api_key="apiKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[GetCountriesRequestFormat]` — Format of the response
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — Optional filter to return countries within a specific region from the region endpoint.
    
</dd>
</dl>

<dl>
<dd>

**subregion:** `typing.Optional[str]` — Optional filter to return countries within a specific subregion from the subregion endpoint.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">get_country_details</a>(...) -> GetCountryDetailsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.get_country_details(
    api_key="apiKey",
    country="country",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**country:** `str` — Country code in ISO 3166-1 alpha-2 format.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[GetCountryDetailsRequestFormat]` — Format of the response
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">get_regions</a>(...) -> GetRegionsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.get_regions(
    api_key="apiKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[GetRegionsRequestFormat]` — Format of the response
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">get_subregions</a>(...) -> GetSubregionsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.get_subregions(
    api_key="apiKey",
    region="region",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**region:** `str` — Name of the region.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[GetSubregionsRequestFormat]` — Format of the response
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">get_admin_levels</a>(...) -> GetAdminLevelsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve administrative units based on ISO 3166-1 alpha-2 country code.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.get_admin_levels(
    api_key="apiKey",
    country="country",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**country:** `str` — Country code in ISO 3166-1 alpha-2 format
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[GetAdminLevelsRequestFormat]` — Format of the response
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">get_admin_units</a>(...) -> GetAdminUnitsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve administrative divisions for a given country using ISO 3166-1 alpha-2 country codes. You can optionally filter by administrative levels.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.get_admin_units(
    api_key="apiKey",
    country="country",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**country:** `str` — Country code in ISO 3166-1 alpha-2 format.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[GetAdminUnitsRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**admin_levels:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Comma-separated list to filter results by one or more administrative levels.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">get_admin_unit_details</a>(...) -> GetAdminUnitDetailsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve detailed administrative unit information by country and optionally filtered by admin code.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.get_admin_unit_details(
    api_key="apiKey",
    country="country",
    admin_unit="admin_unit",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**country:** `str` — Country code in ISO 3166-1 alpha-2 format.
    
</dd>
</dl>

<dl>
<dd>

**admin_unit:** `str` — Optional admin code to fetch details for a specific administrative unit.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[GetAdminUnitDetailsRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">get_cities</a>(...) -> GetCitiesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of cities within a country, optionally filtered by an administrative unit code.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.get_cities(
    api_key="apiKey",
    country="country",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**country:** `str` — Country code in ISO 3166-1 alpha-2 format.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[GetCitiesRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**admin_unit:** `typing.Optional[str]` — Administrative unit code used to filter cities within a specific region.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">get_supported_flags</a>(...) -> typing.List[GetSupportedFlagsResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get list of all supported flags with their metadata
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.get_supported_flags(
    api_key="apiKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">get_flags</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the flag for a specific country
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.get_flags(
    api_key="apiKey",
    name="name",
    shape="flat",
    type="country",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Country code in ISO 3166-1 alpha-2 format.
    
</dd>
</dl>

<dl>
<dd>

**shape:** `GetFlagsRequestShape` — Flag shape. One of: `'flat'` or `'round'`.
    
</dd>
</dl>

<dl>
<dd>

**type:** `GetFlagsRequestType` — Type of flag. One of: `country` or `organization`.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[GetFlagsRequestFormat]` — Flag format. Applicable only for PNG or WEBP formats. Default is png.
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[GetFlagsRequestSize]` — Flag size in pixels. Valid options: `16px`, `24px`, `32px`, `48px`, `64px`. Applicable only for PNG or WEBP formats.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">timezone_lookup</a>(...) -> TimezoneLookupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve current time, date, and timezone-related information by specifying a timezone name, location address, location coordinates, IP address, or use the client IP address if no parameter is passed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.timezone_lookup(
    api_key="apiKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[TimezoneLookupRequestFormat]` — Format of the response
    
</dd>
</dl>

<dl>
<dd>

**ip:** `typing.Optional[str]` — IPv4 or IPv6 address to extract timezone information.
    
</dd>
</dl>

<dl>
<dd>

**tz:** `typing.Optional[str]` — Timezone name (e.g., "Asia/Kolkata") to retrieve information directly.
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[str]` — Location string (preferably city and country) to extract timezone.
    
</dd>
</dl>

<dl>
<dd>

**lat:** `typing.Optional[float]` — Latitude for geolocation lookup.
    
</dd>
</dl>

<dl>
<dd>

**long:** `typing.Optional[float]` — Longitude for geolocation lookup.
    
</dd>
</dl>

<dl>
<dd>

**lang:** `typing.Optional[TimezoneLookupRequestLang]` — Language code for response localization (default is "en").
    
</dd>
</dl>

<dl>
<dd>

**iata_code:** `typing.Optional[str]` — 3-letter IATA airport code (e.g., JFK).
    
</dd>
</dl>

<dl>
<dd>

**icao_code:** `typing.Optional[str]` — 4-letter ICAO airport code (e.g., KJFK).
    
</dd>
</dl>

<dl>
<dd>

**lo_code:** `typing.Optional[str]` — 5-letter UN/LO city code.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">timezone_convert</a>(...) -> TimezoneConvertResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Converts a given time from one timezone to another using various input types like timezone name, coordinates, location, or codes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.timezone_convert(
    api_key="apiKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[TimezoneConvertRequestFormat]` — Format of the response .
    
</dd>
</dl>

<dl>
<dd>

**time:** `typing.Optional[str]` — Time to convert in `yyyy-MM-dd HH:mm` or `yyyy-MM-dd HH:mm:ss` format.
    
</dd>
</dl>

<dl>
<dd>

**tz_from:** `typing.Optional[str]` — Source timezone name (e.g., `Asia/Kolkata`).
    
</dd>
</dl>

<dl>
<dd>

**tz_to:** `typing.Optional[str]` — Target timezone name (e.g., `America/New_York`).
    
</dd>
</dl>

<dl>
<dd>

**lat_from:** `typing.Optional[float]` — Latitude of source location.
    
</dd>
</dl>

<dl>
<dd>

**long_from:** `typing.Optional[float]` — Longitude of source location.
    
</dd>
</dl>

<dl>
<dd>

**lat_to:** `typing.Optional[float]` — Latitude of target location.
    
</dd>
</dl>

<dl>
<dd>

**long_to:** `typing.Optional[float]` — Longitude of target location.
    
</dd>
</dl>

<dl>
<dd>

**location_from:** `typing.Optional[str]` — From location (city/country).
    
</dd>
</dl>

<dl>
<dd>

**location_to:** `typing.Optional[str]` — To location (city/country).
    
</dd>
</dl>

<dl>
<dd>

**iata_from:** `typing.Optional[str]` — From IATA airport code (e.g., JFK).
    
</dd>
</dl>

<dl>
<dd>

**iata_to:** `typing.Optional[str]` — To IATA airport code.
    
</dd>
</dl>

<dl>
<dd>

**icao_from:** `typing.Optional[str]` — From ICAO airport code (e.g., KJFK).
    
</dd>
</dl>

<dl>
<dd>

**icao_to:** `typing.Optional[str]` — To ICAO airport code.
    
</dd>
</dl>

<dl>
<dd>

**locode_from:** `typing.Optional[str]` — From UN/LO CODE.
    
</dd>
</dl>

<dl>
<dd>

**locode_to:** `typing.Optional[str]` — To UN/LO CODE.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">user_agent_lookup</a>(...) -> UserAgentLookupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Parse User Agent string to get detailed browser, device, and operating system information
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.user_agent_lookup(
    api_key="apiKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[UserAgentLookupRequestFormat]` — Format of the response
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">bulk_user_agent_lookup</a>(...) -> typing.List[BulkUserAgentLookupResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Parse up to `50,000 User-Agent strings` at once in a single request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.bulk_user_agent_lookup(
    api_key="apiKey",
    ua_strings=[
        "uaStrings"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**ua_strings:** `typing.List[str]` — List of user agent strings to parse
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[BulkUserAgentLookupRequestFormat]` — Format of the response
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">ocr_predict</a>(...) -> OcrPredictResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Perform Optical Character Recognition (OCR) on images, PDFs, or ZIP archives. Supports two models: `mini-ocr-v1` for CAPTCHA-optimized OCR and `ocr-v1` for general-purpose document text extraction. Supports zonal OCR to extract text from specific regions of an image.

**Notes:**
- The `zone` query parameter cannot be given with .pdf and .zip types as it can only be applied to single image query.
- The `page_range` query parameter cannot be given in any other type except .pdf types.
- PDFs containing images in them are allowed only for processing.
- The `mini-ocr-v1` model doesn’t support the following query parameters:
    - `page_range` (.pdf types)
    - `zone`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.ocr_predict(
    api_key="apiKey",
    model="mini-ocr-v1",
    ocr_predict_request_model="mini-ocr-v1",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**model:** `OcrPredictRequestModel` — OCR model to use.
    
</dd>
</dl>

<dl>
<dd>

**ocr_predict_request_model:** `OcrPredictRequestModel` — OCR model to use. `mini-ocr-v1` for CAPTCHA OCR, `ocr-v1` for general OCR
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — URL of the image or PDF (required if `file` not provided)
    
</dd>
</dl>

<dl>
<dd>

**page_range:** `typing.Optional[str]` — Specify page range for multi-page PDFs (e.g., '1,3,5-10' or 'allpages'). **Note:** This parameter can only be used with .pdf file types.
    
</dd>
</dl>

<dl>
<dd>

**zone:** `typing.Optional[str]` — Define OCR zones using coordinates (top:left:height:width). Multiple zones can be defined using commas. Only available for model 'ocr-v1'. **Note:** This parameter cannot be used with .pdf and .zip file types as it can only be applied to single image queries.
    
</dd>
</dl>

<dl>
<dd>

**new_line:** `typing.Optional[int]` — Set to 1 to split output text into individual lines (default: 0)
    
</dd>
</dl>

<dl>
<dd>

**ocr_predict_request_url:** `typing.Optional[str]` — URL of the image or PDF (required if `file` not provided)
    
</dd>
</dl>

<dl>
<dd>

**ocr_predict_request_page_range:** `typing.Optional[str]` — Specify page range for multi-page PDFs (e.g., '1,3,5-10' or 'allpages'). **Note:** This parameter can only be used with .pdf file types.
    
</dd>
</dl>

<dl>
<dd>

**ocr_predict_request_zone:** `typing.Optional[str]` — Define OCR zones using coordinates (top:left:height:width). Multiple zones can be defined using commas. Only available for model 'ocr-v1'. **Note:** This parameter cannot be used with .pdf and .zip file types as it can only be applied to single image queries.
    
</dd>
</dl>

<dl>
<dd>

**ocr_predict_request_new_line:** `typing.Optional[int]` — Set to 1 to split output text into individual lines (default: 0)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">grammar_detect</a>(...) -> GrammarDetectResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Analyze text for grammar errors and return the exact words flagged as grammatically incorrect with zero-based word positions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.grammar_detect(
    api_key="apiKey",
    text="The global mental is health crisis is now a serious and compelex problem. It need quick and ongoing action from policymakers, healthcare workers, and the whole society.",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` — Text to analyze for grammar errors
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">grammar_correct</a>(...) -> GrammarCorrectResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submit text with grammatical issues and receive a clean grammar-corrected result for proofreading and content workflows.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.grammar_correct(
    api_key="apiKey",
    text="The global mental is health crisis is now a serious and compelex problem. It need quick and ongoing action from policymakers, healthcare workers, and the whole society.",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` — Text to correct
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">weak_words_detect</a>(...) -> WeakWordsDetectResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Analyze text and return weak, vague, or filler words with zero-based word positions to help writers produce clearer and more concise content.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.weak_words_detect(
    api_key="apiKey",
    text="Many people cannot get the support they need to handle their conditions well.",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` — Text to analyze for weak words
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">readability_score</a>(...) -> ReadabilityScoreResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Analyze text readability using industry-standard formulas including Flesch Reading Ease, Flesch-Kincaid Grade Level, Gunning Fog Index, SMOG Index, Coleman-Liau Index, and Automated Readability Index.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.readability_score(
    api_key="apiKey",
    text="The global mental is health crisis is now a serious and compelex problem. It needs quick and ongoing action from policymakers, healthcare workers, and the whole society.",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` — Text to analyze for readability
    
</dd>
</dl>

<dl>
<dd>

**target:** `typing.Optional[ReadabilityScoreRequestTarget]` — Target audience used to tune sentence difficulty levels
    
</dd>
</dl>

<dl>
<dd>

**exclude:** `typing.Optional[str]` — Comma-separated response sections to omit. Possible values are readability_scores, sentence_readability, readability_grade
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/apifreaks/client.py">astronomy_lookup</a>(...) -> AstronomyLookupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve sunrise and sunset times, current position of the moon, and other related information by specifying a location address, location coordinates, IP address, or using the client IP address if no parameter is passed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)

client.astronomy_lookup(
    api_key="apiKey",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` — Your API key
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[AstronomyLookupRequestFormat]` — Format of the response.
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[str]` — Location name or address
    
</dd>
</dl>

<dl>
<dd>

**lat:** `typing.Optional[float]` — Latitude for location coordinates
    
</dd>
</dl>

<dl>
<dd>

**long:** `typing.Optional[float]` — Longitude for location coordinates
    
</dd>
</dl>

<dl>
<dd>

**ip:** `typing.Optional[str]` — IP address for location detection
    
</dd>
</dl>

<dl>
<dd>

**lang:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**date:** `typing.Optional[datetime.date]` — Date for astronomy data (YYYY-MM-DD)
    
</dd>
</dl>

<dl>
<dd>

**elevation:** `typing.Optional[float]` — Timezone of the location for which astronomy data is required
    
</dd>
</dl>

<dl>
<dd>

**time_zone:** `typing.Optional[str]` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

