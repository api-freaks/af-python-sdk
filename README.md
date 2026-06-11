# Apifreaks Python SDK

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=Apifreaks%2FPython)
[![pypi shield](https://img.shields.io/pypi/v/apifreaks)](https://pypi.org/project/apifreaks/)
[![python shield](https://img.shields.io/pypi/pyversions/apifreaks)](https://pypi.org/project/apifreaks/)

The Apifreaks Python library provides convenient access to the Apifreaks APIs from Python applications.

## Table of Contents

- [Installation](#installation)
- [Reference](#reference)
- [Usage](#usage)
- [Async Usage](#async-usage)
- [Environments](#environments)
- [Errors](#errors)
- [Request Types](#request-types)
- [Advanced](#advanced)
  - [Retries](#retries)
  - [Timeouts](#timeouts)
  - [Additional Headers](#additional-headers)
  - [Additional Query String Parameters](#additional-query-string-parameters)
  - [Raw Responses](#raw-responses)
- [Contributing](#contributing)

## Installation

Install the package from PyPI:

```sh
pip install apifreaks
```

Or add it with Poetry:

```sh
poetry add apifreaks
```

Or add it with uv:

```sh
uv add apifreaks
```

The package supports Python `>=3.8`.

## Reference

A full reference for this library is available [here](./reference.md).

## Usage

Instantiate and use the client with the following:

```python
import os

from apifreaks import ApifreaksApi
from apifreaks.core.api_error import ApiError

client = ApifreaksApi()

try:
    response = client.geolocation_lookup(
        api_key=os.environ["APIFREAKS_API_KEY"],
        ip="8.8.8.8",
    )
    print(response)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

Example domain WHOIS lookup:

```python
import os

from apifreaks import ApifreaksApi
from apifreaks.core.api_error import ApiError

client = ApifreaksApi()

try:
    response = client.domain_whois_lookup(
        api_key=os.environ["APIFREAKS_API_KEY"],
        domain_name="example.com",
    )
    print(response)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

Example bulk geolocation lookup:

```python
import os

from apifreaks import ApifreaksApi

client = ApifreaksApi()

response = client.bulk_geolocation_lookup(
    api_key=os.environ["APIFREAKS_API_KEY"],
    ips=["8.8.8.8", "1.1.1.1"],
)

print(response)
```

## Async Usage

The SDK also provides an async client:

```python
import asyncio
import os

from apifreaks import AsyncApifreaksApi
from apifreaks.core.api_error import ApiError

async def main() -> None:
    client = AsyncApifreaksApi()

    try:
        response = await client.geolocation_lookup(
            api_key=os.environ["APIFREAKS_API_KEY"],
            ip="8.8.8.8",
        )
        print(response)
    except ApiError as e:
        print(e.status_code)
        print(e.body)

asyncio.run(main())
```

## Environments

This SDK allows you to configure the API environment for requests.

```python
from apifreaks import ApifreaksApi
from apifreaks.environment import ApifreaksApiEnvironment

client = ApifreaksApi(
    environment=ApifreaksApiEnvironment.DEFAULT,
)
```

You can also override the base URL directly:

```python
from apifreaks import ApifreaksApi

client = ApifreaksApi(
    base_url="https://api.apifreaks.com",
)
```

## Errors

When the API returns a non-success status code, the SDK raises an API error.

```python
from apifreaks import ApifreaksApi
from apifreaks.core.api_error import ApiError

client = ApifreaksApi()

try:
    response = client.geolocation_lookup(
        api_key="your_api_key",
        ip="8.8.8.8",
    )
    print(response)
except ApiError as e:
    print(f"Status code: {e.status_code}")
    print(f"Response body: {e.body}")
```

## Request Types

The SDK exports generated request and response types from the `apifreaks` package.

```python
from apifreaks import GeolocationLookupResponse

# Returned from client.geolocation_lookup(...)
response: GeolocationLookupResponse
```

Most endpoints accept keyword arguments directly, so you usually do not need to manually instantiate request objects.

## Advanced

### Retries

The SDK is instrumented with automatic retries. By default, failed requests are retried up to `2` times when the request is considered retryable.

You can configure retries globally on the client:

```python
from apifreaks import ApifreaksApi

client = ApifreaksApi(max_retries=3)
```

You can also configure retries for a single request:

```python
from apifreaks import ApifreaksApi

client = ApifreaksApi()

response = client.geolocation_lookup(
    api_key="your_api_key",
    ip="8.8.8.8",
    request_options={"max_retries": 3},
)
```

### Timeouts

The SDK defaults to a `60` second timeout.

Configure the timeout globally:

```python
from apifreaks import ApifreaksApi

client = ApifreaksApi(timeout=30)
```

Configure the timeout for a single request:

```python
from apifreaks import ApifreaksApi

client = ApifreaksApi()

response = client.geolocation_lookup(
    api_key="your_api_key",
    ip="8.8.8.8",
    request_options={"timeout_in_seconds": 30},
)
```

### Additional Headers

You can add custom headers to a request using `request_options`.

```python
from apifreaks import ApifreaksApi

client = ApifreaksApi()

response = client.geolocation_lookup(
    api_key="your_api_key",
    ip="8.8.8.8",
    request_options={
        "additional_headers": {
            "X-Custom-Header": "custom-value",
        },
    },
)
```

### Additional Query String Parameters

You can add custom query parameters using `request_options`.

```python
from apifreaks import ApifreaksApi

client = ApifreaksApi()

response = client.geolocation_lookup(
    api_key="your_api_key",
    ip="8.8.8.8",
    request_options={
        "additional_query_parameters": {
            "filter": "active",
        },
    },
)
```

### Raw Responses

Use `with_raw_response` when you need access to raw response metadata.

```python
from apifreaks import ApifreaksApi

client = ApifreaksApi()

response = client.with_raw_response.geolocation_lookup(
    api_key="your_api_key",
    ip="8.8.8.8",
)

print(response.status_code)
print(response.headers)
print(response.data)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
