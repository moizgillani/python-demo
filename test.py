from servicingmerchantcasemanagementapi.exceptions.error_exception import ErrorException
from servicingmerchantcasemanagementapi.exceptions.api_exception import APIException
from servicingmerchantcasemanagementapi.servicingmerchantcasemanagementapi_client import ServicingmerchantcasemanagementapiClient
from servicingmerchantcasemanagementapi.configuration import Environment

client = ServicingmerchantcasemanagementapiClient(
    authorization='Authorization',
    environment=Environment.PRODUCTION
)

case_controller = client.case
case_number = '11111234'

v_correlation_id = '24578e35-9bd2-238f-b4c2-0bc9ad9aed2b'

try:
    result = case_controller.get_case_details(
        case_number,
        v_correlation_id=v_correlation_id
    )
    print(result)
except ErrorException as e: 
    print(e)
except APIException as e: 
    print(e)

