
# Pagination Type

Use for pagination.

## Structure

`PaginationType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `str` | Optional | The maximum number of entries to return. If the value exceeds the maximum, then the maximum value will be used.<br>**Default**: `'25'`<br>**Constraints**: *Maximum Length*: `25` |
| `offset` | `str` | Optional | The offset used for page results<br>**Default**: `'1'`<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `1` |

## Example (as JSON)

```json
{
  "limit": "3",
  "offset": "1"
}
```

