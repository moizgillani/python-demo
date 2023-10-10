
# Error Response

## Structure

`ErrorResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | Worldpay generated Correlation Id<br>**Constraints**: *Maximum Length*: `36`, *Pattern*: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]-[0-9a-fA-F]{12}` |
| `error_code` | `str` | Optional | Error code<br>**Constraints**: *Maximum Length*: `20` |
| `error_message` | `str` | Required | Error message<br>**Constraints**: *Maximum Length*: `255` |

## Example (as JSON)

```json
{
  "errorCode": "400 Bad Request",
  "errorMessage": "Missing NotificationId in the request.",
  "correlationId": "correlationId2"
}
```

