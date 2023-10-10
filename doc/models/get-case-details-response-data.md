
# Get Case Details Response Data

## Structure

`GetCaseDetailsResponseData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `hierarchy` | [`Hierarchy`](../../doc/models/hierarchy.md) | Optional | Hierarchy details |
| `caller_info` | [`CallerInfo`](../../doc/models/caller-info.md) | Optional | Caller information |
| `case_info` | [`AdditionalCaseDetails`](../../doc/models/additional-case-details.md) | Optional | Case information |
| `attachments` | [`List[AttachmentIdentifiers]`](../../doc/models/attachment-identifiers.md) | Optional | Attachments details |

## Example (as JSON)

```json
{
  "hierarchy": {
    "salesOrganizationCode": "salesOrganizationCode2",
    "salesOrganizationName": "salesOrganizationName0",
    "salesChannelCode": "salesChannelCode4",
    "salesChannelName": "salesChannelName2",
    "partnerId": "partnerId2"
  },
  "callerInfo": {
    "requestor": "requestor6",
    "email": "email4",
    "phoneNumber": "phoneNumber8"
  },
  "caseInfo": {
    "caseNumber": "caseNumber0",
    "category": "category2",
    "caseType": "caseType0",
    "priority": "Overnight",
    "status": "New"
  },
  "attachments": [
    {
      "fileName": "fileName4",
      "id": "id0"
    },
    {
      "fileName": "fileName4",
      "id": "id0"
    },
    {
      "fileName": "fileName4",
      "id": "id0"
    }
  ]
}
```

