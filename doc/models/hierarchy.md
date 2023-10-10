
# Hierarchy

## Structure

`Hierarchy`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sales_organization_code` | `str` | Optional | Sales Organization Code<br>**Constraints**: *Maximum Length*: `10` |
| `sales_organization_name` | `str` | Optional | Sales organization name<br>**Constraints**: *Maximum Length*: `30` |
| `sales_channel_code` | `str` | Optional | Sales channel code<br>**Constraints**: *Maximum Length*: `10` |
| `sales_channel_name` | `str` | Optional | Sales channel name<br>**Constraints**: *Maximum Length*: `30` |
| `partner_id` | `str` | Optional | The identifier associated with the partner group<br>**Constraints**: *Maximum Length*: `16` |
| `partner_name` | `str` | Optional | The name of the partner's group<br>**Constraints**: *Maximum Length*: `50` |
| `region_code` | `str` | Optional | Region Code<br>**Constraints**: *Maximum Length*: `10` |
| `region_name` | `str` | Optional | Region Name<br>**Constraints**: *Maximum Length*: `255` |
| `national_code` | `str` | Optional | National code<br>**Constraints**: *Maximum Length*: `7` |
| `national_name` | `str` | Optional | National name<br>**Constraints**: *Maximum Length*: `30` |
| `division_code` | `str` | Optional | Division Code<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `3` |
| `division_name` | `str` | Optional | The name associated with a given partner division<br>**Constraints**: *Maximum Length*: `30` |
| `super_chain_code` | `str` | Optional | Super chain code<br>**Constraints**: *Maximum Length*: `10` |
| `super_chain_name` | `str` | Optional | Super chain name<br>**Constraints**: *Maximum Length*: `30` |
| `store_number` | `str` | Optional | The identifier code of a store under a given partner chain. Can store alphanumber value when creating the store<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `9` |
| `store_name` | `str` | Optional | The name associated with a store under a given partner chain<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `40` |
| `chain_code` | `str` | Optional | The Chain Code is the level of the merchant hierarchy that groups merchant identifiers (MIDs) and any related roll-up values under a common identifier for settlement, billing and reporting. Chain Code is the primary identifier for merchants boarded in MDB (Merchant Database) system.<br>**Constraints**: *Maximum Length*: `6` |
| `chain_name` | `str` | Optional | The name associated with a given merchant under a chain-level hierarchy<br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `25` |
| `merchant_id` | `str` | Optional | The identifier code associated with a given merchant under a store-level hierarchy<br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `16` |
| `merchant_name` | `str` | Optional | The name associated with a given merchant under a store-level hierarchy<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `30` |

## Example (as JSON)

```json
{
  "salesOrganizationCode": "55",
  "salesOrganizationName": "CORE",
  "salesChannelCode": "812",
  "salesChannelName": "ABC NORTH WEST",
  "partnerId": "81",
  "partnerName": "VSoft",
  "regionCode": "MD0001",
  "regionName": "Mid West South Central",
  "nationalCode": "ABC101",
  "nationalName": "ABC Company",
  "divisionCode": "191",
  "divisionName": "DIVISION 191",
  "superChainCode": "STEST7053",
  "superChainName": "SKrog",
  "storeNumber": "000000011",
  "storeName": "ABC #037",
  "chainCode": "0T0081",
  "chainName": "ABC, Inc",
  "merchantId": "111222333444555",
  "merchantName": "ABC #037"
}
```

