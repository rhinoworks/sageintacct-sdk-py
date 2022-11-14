"""
Sage Intacct AR Payments
"""
from typing import Dict

from .api_base import ApiBase


class ARPaymentItems(ApiBase):
    """Class for AR Payments APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='ARPAYMENTITEM')

    def get_all(self, pagesize=1000, offset=0):
        """Get all AR Payments from Sage Intacct

        Returns:
            List of Dict in AR Payments schema.
        """
        data = {
            'readByQuery': {
                'object': 'ARPAYMENTITEM',
                'fields': '*',
                'query': None,
                'pagesize': str(pagesize),
                'offset': str(offset)
            }
        }
        print(self.format_and_send_request(data)['data'])
        return self.format_and_send_request(data)['data']['arpaymentitem']
