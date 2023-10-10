
# Date Range Search

Specify the date range for search. Consumer can lookup for 60 days data at a time. If you want more data divide your search into multiple windows.

## Structure

`DateRangeSearch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `from_date` | `str` | Required | specify start date for range.<br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-9]{2}-[0-9]{2}` |
| `to_date` | `str` | Required | specify end date for range.<br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `[0-9]{4}-[0-9]{2}-[0-9]{2}` |

## Example (as JSON)

```json
{
  "fromDate": "2021-10-27",
  "toDate": "2021-12-27"
}
```

