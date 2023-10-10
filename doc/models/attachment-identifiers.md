
# Attachment Identifiers

## Structure

`AttachmentIdentifiers`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `file_name` | `str` | Required | This element contains file name of attched file<br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `255` |
| `id` | `str` | Required | Attachment file identifier.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255` |

## Example (as JSON)

```json
{
  "fileName": "testFile.xml",
  "id": "XCG1234"
}
```

