
# Create Case Request

## Structure

`CreateCaseRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `entity_info` | [`EntityInfo`](../../doc/models/entity-info.md) | Required | Entity information details |
| `caller_info` | [`CallerInfo`](../../doc/models/caller-info.md) | Required | Caller information details |
| `case_info` | [`CaseInfo`](../../doc/models/case-info.md) | Required | Case information details |
| `attachments` | [`List[Attachment]`](../../doc/models/attachment.md) | Optional | Attachment file names |

## Example (as JSON)

```json
{
  "entityInfo": {
    "entityValue": "0H9124",
    "entityType": "CHAIN"
  },
  "callerInfo": {
    "requestor": "RequestorName",
    "email": "Requestors@email.com",
    "phoneNumber": "6789923328"
  },
  "caseInfo": {
    "subject": "Update Primary Contact",
    "category": "Account Management",
    "caseType": "Authorized User Maintenance",
    "reason": "Service Activity",
    "description": "Detailed discription",
    "origin": "Web-eWPD",
    "priority": "Urgent"
  },
  "attachments": [
    {
      "fileName": "fileName4",
      "fileContent": "fileContent6"
    },
    {
      "fileName": "fileName4",
      "fileContent": "fileContent6"
    },
    {
      "fileName": "fileName4",
      "fileContent": "fileContent6"
    }
  ]
}
```

