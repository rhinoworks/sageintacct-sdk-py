"""
Sage Intacct AP Payments
"""
from typing import Dict

from .api_base import ApiBase


class APBillItem(ApiBase):
    """Class for AP Payments APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='APBILLITEM')

    def get_all(self):
        """Get all AP Bill Detail items from Sage Intacct

        Returns:
            List of Dict in AP Bill Detail schema.
        """
        data = {
            'readByQuery': {
                'object': 'APBILLITEM',
                'fields': '*',
                'query': None,
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']['apbillitem']
