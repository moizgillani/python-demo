
# Additional Case Details

## Structure

`AdditionalCaseDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `case_number` | `str` | Optional | Unique number assigned to the case (Auto generated once case is created)<br>**Constraints**: *Maximum Length*: `12` |
| `category` | `str` | Optional | Case category. High level grouping of case types.<br>**Constraints**: *Maximum Length*: `70` |
| `case_type` | `str` | Optional | Case type for selected category for the case<br>**Constraints**: *Maximum Length*: `70` |
| `priority` | [`Priority1Enum`](../../doc/models/priority-1-enum.md) | Optional | Defines time limit for case resolution<br>**Constraints**: *Maximum Length*: `50` |
| `status` | [`Status2Enum`](../../doc/models/status-2-enum.md) | Optional | Status of a case<br>**Constraints**: *Maximum Length*: `35` |
| `sub_status` | [`SubStatusEnum`](../../doc/models/sub-status-enum.md) | Optional | Only applicable when status is Pending |
| `reason` | `str` | Optional | The reason a case was created<br>**Constraints**: *Maximum Length*: `70` |
| `subject` | `str` | Optional | Brief description of the customer’s question or feedback.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `255` |
| `description` | `str` | Optional | User defined field.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `32000` |

## Example (as JSON)

```json
{
  "caseNumber": "0123213213",
  "category": "Account Management",
  "caseType": "Authorized User Maintenance",
  "priority": "Urgent",
  "status": "Pending",
  "reason": "Status Update",
  "subject": "KB-SUB-827",
  "description": "This is the test description"
}
```

