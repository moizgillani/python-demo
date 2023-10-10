
# Create Attachment Request

## Structure

`CreateAttachmentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `attachments` | [`List[Attachment]`](../../doc/models/attachment.md) | Required | Attachment file names |

## Example (as JSON)

```json
{
  "attachments": [
    {
      "fileName": "testFile.txt",
      "fileContent": "fileContent6"
    }
  ]
}
```

