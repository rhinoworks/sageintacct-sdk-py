"""
Sage Intacct AR Payments
"""
from typing import Dict

from .api_base import ApiBase


class ARPaymentDetail(ApiBase):
    """Class for AR Payments APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='ARPYMTDETAIL')
