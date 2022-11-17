"""
Sage Intacct AP Payments
"""
from typing import Dict

from .api_base import ApiBase


class APBillDetail(ApiBase):
    """Class for AP Payments APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='APBILLDETAIL')

    def get_all(self):
        """Get all AP Bill Detail items from Sage Intacct

        Returns:
            List of Dict in AP Bill Detail schema.
        """
        data = {
            'readByQuery': {
                'object': 'APBILLDETAIL',
                'fields': '*',
                'query': None,
                'pagesize': '1000'
            }
        }

        return self.format_and_send_request(data)['data']['apbilldetail']
