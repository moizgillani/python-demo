
# Get Attachment Response

Retrive attachment files on a case. All attachments (file names with attachment ids) can be retrieved on a case by looking up the case details.

## Structure

`GetAttachmentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `attachment_id` | `str` | Optional | Attachment identifier for the file.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255` |
| `file_name` | `str` | Required | This element contains file name of attachment.<br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `255` |
| `file_content` | `str` | Required | File content in the form of base64 or multipart file.<br>**Constraints**: *Maximum Length*: `1000` |

## Example (as JSON)

```json
{
  "attachmentId": "0099UI6732",
  "fileName": "testFile.xml",
  "fileContent": "V2ViIC0gZVdQRA=="
}
```

