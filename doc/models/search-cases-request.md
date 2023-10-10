
# Search Cases Request

Request for Case Search .

## Structure

`SearchCasesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `entity_info` | [`EntityInfo`](../../doc/models/entity-info.md) | Optional | Pass entityInfo related to region/national/division/superChain/store/chain or merchant for which this search will happen. Pass entityType and entityValue, it should map to a single entity only. |
| `date_type` | [`DateTypeEnum`](../../doc/models/date-type-enum.md) | Required | Type of date<br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `10` |
| `date_range` | [`DateRangeSearch`](../../doc/models/date-range-search.md) | Required | Date range, can be between 1 and 60 days. |
| `case_info` | [`SearchCaseInfoRequest`](../../doc/models/search-case-info-request.md) | Optional | Case information. |
| `pagination_request` | [`PaginationType`](../../doc/models/pagination-type.md) | Optional | Pagination requested details |
| `sort_results_by` | [`List[SortResultsBy]`](../../doc/models/sort-results-by.md) | Optional | Select up to four fields for sorting the search results. Fields that can be selected are entityValue, caseNumber, category, caseType, origin, status and priority. |

## Example (as JSON)

```json
{
  "dateType": "openDate",
  "dateRange": {
    "fromDate": "2021-10-27",
    "toDate": "2021-12-27"
  },
  "entityInfo": {
    "entityValue": "entityValue4",
    "entityType": "PARTNER"
  },
  "caseInfo": {
    "caseNumber": "caseNumber0",
    "category": "category2",
    "caseType": "caseType0",
    "status": "New",
    "priority": "Overnight"
  },
  "paginationRequest": {
    "limit": "limit6",
    "offset": "offset2"
  },
  "sortResultsBy": [
    {
      "fieldName": "fieldName6",
      "orderBy": "ASC"
    },
    {
      "fieldName": "fieldName6",
      "orderBy": "ASC"
    },
    {
      "fieldName": "fieldName6",
      "orderBy": "ASC"
    }
  ]
}
```

