
# Search Cases Response

List of Cases will be returned in the Search Response from WolrdPay

## Structure

`SearchCasesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `case_list` | [`List[CaseList]`](../../doc/models/case-list.md) | Optional | Case list details for selected case criteria. |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Pagination response details |

## Example (as JSON)

```json
{
  "caseList": [
    {
      "caseHierarchy": {
        "salesOrganizationCode": "salesOrganizationCode4",
        "salesOrganizationName": "salesOrganizationName2",
        "salesChannelCode": "salesChannelCode6",
        "salesChannelName": "salesChannelName4",
        "partnerId": "partnerId4"
      },
      "caseInfo": {
        "caseNumber": "caseNumber0",
        "category": "category2",
        "caseType": "caseType0",
        "origin": "origin8",
        "status": "New"
      }
    },
    {
      "caseHierarchy": {
        "salesOrganizationCode": "salesOrganizationCode4",
        "salesOrganizationName": "salesOrganizationName2",
        "salesChannelCode": "salesChannelCode6",
        "salesChannelName": "salesChannelName4",
        "partnerId": "partnerId4"
      },
      "caseInfo": {
        "caseNumber": "caseNumber0",
        "category": "category2",
        "caseType": "caseType0",
        "origin": "origin8",
        "status": "New"
      }
    },
    {
      "caseHierarchy": {
        "salesOrganizationCode": "salesOrganizationCode4",
        "salesOrganizationName": "salesOrganizationName2",
        "salesChannelCode": "salesChannelCode6",
        "salesChannelName": "salesChannelName4",
        "partnerId": "partnerId4"
      },
      "caseInfo": {
        "caseNumber": "caseNumber0",
        "category": "category2",
        "caseType": "caseType0",
        "origin": "origin8",
        "status": "New"
      }
    }
  ],
  "paginationResponse": {
    "pagination": {
      "limit": "limit2",
      "offset": "offset6"
    },
    "moreDataAvailable": "moreDataAvailable6",
    "totalRowCount": 50,
    "totalReturnedCount": 200
  }
}
```

