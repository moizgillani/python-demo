# Case

```python
case_controller = client.case
```

## Class Name

`CaseController`

## Methods

* [Create Case](../../doc/controllers/case.md#create-case)
* [Update Case](../../doc/controllers/case.md#update-case)
* [Get Case Details](../../doc/controllers/case.md#get-case-details)
* [Search Cases](../../doc/controllers/case.md#search-cases)
* [Create Attachments](../../doc/controllers/case.md#create-attachments)
* [Get Attachments](../../doc/controllers/case.md#get-attachments)


# Create Case

Create a new case in service cloud

```python
def create_case(self,
               v_correlation_id=None,
               body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |
| `body` | [`CreateCaseRequest`](../../doc/models/create-case-request.md) | Body, Optional | - |

## Response Type

[`CreateCaseResponse`](../../doc/models/create-case-response.md)

## Example Usage

```python
v_correlation_id = '24578e35-9bd2-238f-b4c2-0bc9ad9aed2b'

body = CreateCaseRequest(
    entity_info=EntityInfo(
        entity_value='0H9124',
        entity_type=EntityTypeEnum.CHAIN
    ),
    caller_info=CallerInfo(
        requestor='RequestorName',
        email='Requestors@email.com',
        phone_number='6789923328'
    ),
    case_info=CaseInfo(
        subject='Update Primary Contact',
        category='Account Management',
        reason='Service Activity',
        description='Detailed discription',
        origin='Web-eWPD',
        case_type='Authorized User Maintenance',
        priority=PriorityEnum.URGENT
    )
)

result = case_controller.create_case(
    v_correlation_id=v_correlation_id,
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorException`](../../doc/models/error-exception.md) |


# Update Case

Add comments for an existing service request case present with Worldpay.

```python
def update_case(self,
               case_number,
               v_correlation_id=None,
               body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `case_number` | `str` | Template, Required | Unique number assigned to the case (Auto generated once case is created)<br>**Constraints**: *Maximum Length*: `12` |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |
| `body` | [`CreateCommentRequest`](../../doc/models/create-comment-request.md) | Body, Optional | - |

## Response Type

`void`

## Example Usage

```python
case_number = '12376567'

v_correlation_id = '24578e35-9bd2-238f-b4c2-0bc9ad9aed2b'

body = CreateCommentRequest(
    comment='This is a new comment'
)

result = case_controller.update_case(
    case_number,
    v_correlation_id=v_correlation_id,
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorException`](../../doc/models/error-exception.md) |


# Get Case Details

Retrieve details for a specific service request case submitted with Worldpay.

```python
def get_case_details(self,
                    case_number,
                    v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `case_number` | `str` | Template, Required | Unique number assigned to the case (Auto generated once case is created)<br>**Constraints**: *Maximum Length*: `12` |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |

## Response Type

[`GetCaseDetailsResponseData`](../../doc/models/get-case-details-response-data.md)

## Example Usage

```python
case_number = '11111234'

v_correlation_id = '24578e35-9bd2-238f-b4c2-0bc9ad9aed2b'

result = case_controller.get_case_details(
    case_number,
    v_correlation_id=v_correlation_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorException`](../../doc/models/error-exception.md) |


# Search Cases

Search for service request cases  based on search parameters with Worldpay.

```python
def search_cases(self,
                v_correlation_id=None,
                body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |
| `body` | [`SearchCasesRequest`](../../doc/models/search-cases-request.md) | Body, Optional | - |

## Response Type

[`SearchCasesResponse`](../../doc/models/search-cases-response.md)

## Example Usage

```python
v_correlation_id = '24578e35-9bd2-238f-b4c2-0bc9ad9aed2b'

body = SearchCasesRequest(
    date_type=DateTypeEnum.OPENDATE,
    date_range=DateRangeSearch(
        from_date='2021-10-27',
        to_date='2021-12-27'
    )
)

result = case_controller.search_cases(
    v_correlation_id=v_correlation_id,
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorException`](../../doc/models/error-exception.md) |


# Create Attachments

Attach attachments for an existing service request case present with WorldPay.

```python
def create_attachments(self,
                      case_number,
                      v_correlation_id=None,
                      file=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `case_number` | `str` | Template, Required | Unique number assigned to the case (Auto generated once case is created)<br>**Constraints**: *Maximum Length*: `12` |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |
| `file` | `typing.BinaryIO` | Form, Optional | Attachment file |

## Response Type

`void`

## Example Usage

```python
case_number = '12376567'

v_correlation_id = '24578e35-9bd2-238f-b4c2-0bc9ad9aed2b'

result = case_controller.create_attachments(
    case_number,
    v_correlation_id=v_correlation_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorException`](../../doc/models/error-exception.md) |


# Get Attachments

Retrieve attachment of a case by attachment identifier with Worldpay.

```python
def get_attachments(self,
                   case_number,
                   attachment_id,
                   v_correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `case_number` | `str` | Template, Required | Case Number associated with the attachment<br>**Constraints**: *Maximum Length*: `12` |
| `attachment_id` | `str` | Template, Required | Attachment identifier for the file<br>**Constraints**: *Maximum Length*: `255` |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |

## Response Type

[`GetAttachmentResponse`](../../doc/models/get-attachment-response.md)

## Example Usage

```python
case_number = '14837'

attachment_id = 'A1JXVGTYUIO'

v_correlation_id = '24578e35-9bd2-238f-b4c2-0bc9ad9aed2b'

result = case_controller.get_attachments(
    case_number,
    attachment_id,
    v_correlation_id=v_correlation_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorException`](../../doc/models/error-exception.md) |

