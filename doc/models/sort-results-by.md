
# Sort Results By

Use for filtering search results.

## Structure

`SortResultsBy`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field_name` | `str` | Optional | Field name to be used for sorting purposes.<br>**Constraints**: *Maximum Length*: `15` |
| `order_by` | [`OrderByEnum`](../../doc/models/order-by-enum.md) | Optional | Order search results in ascnding or descending order.<br>**Default**: `'ASC'`<br>**Constraints**: *Maximum Length*: `4` |

## Example (as JSON)

```json
{
  "fieldName": "caseNumber",
  "orderBy": "DESC"
}
```

