
# Get Case Category Types Response

List of case types for a specific case category from WolrdPay will be returned in the response

## Structure

`GetCaseCategoryTypesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `category` | `str` | Optional | Case Category. High level grouping of case types.<br>**Constraints**: *Maximum Length*: `70` |
| `case_types` | `List[str]` | Optional | List of applicable case types for case category. |

## Example (as JSON)

```json
{
  "category": "Account Management",
  "caseTypes": [
    "caseTypes7"
  ]
}
```

