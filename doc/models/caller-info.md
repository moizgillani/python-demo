
# Caller Info

## Structure

`CallerInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `requestor` | `str` | Required | Name of the requestor<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `50` |
| `email` | `str` | Required | Requestor's email address<br>**Constraints**: *Maximum Length*: `100` |
| `phone_number` | `str` | Optional | Requestor's phone number<br>**Constraints**: *Maximum Length*: `10` |

## Example (as JSON)

```json
{
  "requestor": "RequestorName",
  "email": "Requestors@email.com",
  "phoneNumber": "6789923328"
}
```

