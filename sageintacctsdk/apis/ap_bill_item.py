"""
Sage Intacct AP Payments
"""
from typing import Dict

from .api_base import ApiBase


class APBillItem(ApiBase):
    """Class for AP Payments APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='APBILLITEM')