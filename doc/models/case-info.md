
# Case Info

Information needed to create a case. If the Entity Type is MERCHANT or CHAIN, case type is required

## Structure

`CaseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subject` | `str` | Required | Brief description of the requstor’s issue<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255` |
| `category` | `str` | Required | Case category. High level grouping of case types<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `70` |
| `case_type` | `str` | Optional | Case type for selected category for the case<br>**Constraints**: *Maximum Length*: `70` |
| `reason` | `str` | Required | Reason for creating the case<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `70` |
| `description` | `str` | Required | Description of a case<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `32000` |
| `origin` | `str` | Required | Indicates the source of the case.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `70` |
| `priority` | [`PriorityEnum`](../../doc/models/priority-enum.md) | Optional | Defines time limit for case resolution<br>**Constraints**: *Maximum Length*: `70` |

## Example (as JSON)

```json
{
  "subject": "Update Primary Contact",
  "category": "Account Management",
  "caseType": "Authorized User Maintenance",
  "reason": "Service Activity",
  "description": "Detailed discription",
  "origin": "Web-eWPD",
  "priority": "Urgent"
}
```

