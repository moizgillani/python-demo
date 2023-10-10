
# Case List

List of cases associated with salesOrganization/salesChannel/partner/region/national/division/superChain/store/chain or merchant.

## Structure

`CaseList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `case_hierarchy` | [`Hierarchy`](../../doc/models/hierarchy.md) | Optional | Case hierarchy details. |
| `case_info` | [`SearchCaseInfoResponse`](../../doc/models/search-case-info-response.md) | Optional | Case information details. |

## Example (as JSON)

```json
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
```

