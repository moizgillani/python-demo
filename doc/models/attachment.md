
# Attachment

## Structure

`Attachment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `file_name` | `str` | Required | Name of the file with extension<br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `255` |
| `file_content` | `binary` | Required | Content of the file. Accepts upto 4 MB |

## Example (as JSON)

```json
{
  "fileName": "testFile.txt",
  "fileContent": "fileContent6"
}
```

