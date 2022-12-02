"""
Sage Intacct AR Payments
"""
from typing import Dict

from .api_base import ApiBase


class ARPaymentItem(ApiBase):
    """Class for AR Payments APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='ARPAYMENTITEM')
