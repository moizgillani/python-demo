
# Pagination Response

## Structure

`PaginationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination` | [`PaginationType`](../../doc/models/pagination-type.md) | Optional | Pagination type details |
| `more_data_available` | `str` | Optional | Indicates if more data is available for the search criteria<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `3000` |
| `total_row_count` | `int` | Optional | Total number of rows available for the search results<br>**Constraints**: `<= 10000` |
| `total_returned_count` | `int` | Optional | Number of rows returned |

## Example (as JSON)

```json
{
  "moreDataAvailable": "false",
  "totalRowCount": 3000,
  "totalReturnedCount": 1,
  "pagination": {
    "limit": "limit2",
    "offset": "offset6"
  }
}
```

