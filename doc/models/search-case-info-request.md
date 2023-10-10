
# Search Case Info Request

Search parameters for searching the case.

## Structure

`SearchCaseInfoRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `case_number` | `str` | Optional | Case number assigned to case<br>**Constraints**: *Maximum Length*: `12` |
| `category` | `str` | Optional | Case category. High level grouping of case types<br>**Constraints**: *Maximum Length*: `70` |
| `case_type` | `str` | Optional | Case type for selected category for the case<br>**Constraints**: *Maximum Length*: `70` |
| `status` | [`StatusEnum`](../../doc/models/status-enum.md) | Optional | Case status<br>**Constraints**: *Maximum Length*: `25` |
| `priority` | [`Priority1Enum`](../../doc/models/priority-1-enum.md) | Optional | Defines time limit for case resolution<br>**Constraints**: *Maximum Length*: `70` |

## Example (as JSON)

```json
{
  "caseNumber": "02567576",
  "category": "Account Management",
  "caseType": "Authorized User Maintenance",
  "status": "In Progress",
  "priority": "Urgent"
}
```

