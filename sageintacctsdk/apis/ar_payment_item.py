"""
Sage Intacct AR Payments
"""
from typing import Dict

from .api_base import ApiBase


class ARPaymentItem(ApiBase):
    """Class for AR Payments APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='ARPAYMENTITEM')

    def get_all(self):
        """Get all AP Payments from Sage Intacct

        Returns:
            List of Dict in AP Payments schema.
        """
        data = {
            'readByQuery': {
                'object': 'ARPAYMENTITEM',
                'fields': '*',
                'query': None,
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']['arpaymentitem']