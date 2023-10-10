
# Entity Info

## Structure

`EntityInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `entity_value` | `str` | Required | Unique identifier of the entity<br>**Constraints**: *Maximum Length*: `20` |
| `entity_type` | [`EntityTypeEnum`](../../doc/models/entity-type-enum.md) | Optional | Type of the entity, Required for US entities<br>**Constraints**: *Maximum Length*: `10` |

## Example (as JSON)

```json
{
  "entityValue": "0H9124",
  "entityType": "CHAIN"
}
```

