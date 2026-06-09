from apifreaks import ApifreaksApi
from apifreaks.core.api_error import ApiError

client = ApifreaksApi()

try:
    response = client.domain_whois_lookup(
        api_key="YOUR_API_KEY",
        domain_name="example.com"
    )

    response = {k: v for k, v in response.dict().items() if v is not None}

    print(response)

except ApiError as e:
    print(e.body)
