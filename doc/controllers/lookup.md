# Lookup

```python
lookup_controller = client.lookup
```

## Class Name

`LookupController`

## Methods

* [Get Case Categories](../../doc/controllers/lookup.md#get-case-categories)
* [Get Case Category Types](../../doc/controllers/lookup.md#get-case-category-types)
* [Get Case Reasons](../../doc/controllers/lookup.md#get-case-reasons)


# Get Case Categories

Get list of all active case categories from WolrdPay.

```python
def get_case_categories(self,
                       v_correlation_id=None,
                       country=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |
| `country` | [`CountryEnum`](../../doc/models/country-enum.md) | Query, Optional | country for retrieveing the categories, default is US if nothing is passed |

## Response Type

[`GetCaseCategoriesResponse`](../../doc/models/get-case-categories-response.md)

## Example Usage

```python
v_correlation_id = '24578e35-9bd2-238f-b4c2-0bc9ad9aed2b'

country = CountryEnum.US

result = lookup_controller.get_case_categories(
    v_correlation_id=v_correlation_id,
    country=country
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "categories": [
    "Account Management",
    "Collections",
    "Configuration/Downloads",
    "Contract Management",
    "Disputes"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorException`](../../doc/models/error-exception.md) |


# Get Case Category Types

Retrieve list of case types for specific case category with WolrdPay

```python
def get_case_category_types(self,
                           v_correlation_id=None,
                           category=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |
| `category` | `str` | Query, Optional | Case category. High level grouping of case types.<br>**Constraints**: *Maximum Length*: `70` |

## Response Type

[`GetCaseCategoryTypesResponse`](../../doc/models/get-case-category-types-response.md)

## Example Usage

```python
v_correlation_id = '24578e35-9bd2-238f-b4c2-0bc9ad9aed2b'

category = 'Account Management'

result = lookup_controller.get_case_category_types(
    v_correlation_id=v_correlation_id,
    category=category
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "category": "Account Management",
  "caseTypes": [
    "Add Location",
    "Authorized User Maintenance",
    "Close Account",
    "Dealer/Partner/RM Change"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorException`](../../doc/models/error-exception.md) |


# Get Case Reasons

Retrieve list of all case reasons from WolrdPay.

```python
def get_case_reasons(self,
                    v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |

## Response Type

[`GetCaseReasonsResponse`](../../doc/models/get-case-reasons-response.md)

## Example Usage

```python
v_correlation_id = '24578e35-9bd2-238f-b4c2-0bc9ad9aed2b'

result = lookup_controller.get_case_reasons(
    v_correlation_id=v_correlation_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "reasons": [
    "Escalation",
    "Repeat Call",
    "Service Activity",
    "Status Update"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorException`](../../doc/models/error-exception.md) |

