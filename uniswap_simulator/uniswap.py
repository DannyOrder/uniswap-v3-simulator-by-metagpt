## uniswap.py
from uniswap import Uniswap
from typing import Dict

class UniswapV3:
    def __init__(self, address: str, private_key: str):
        self.uniswap = Uniswap(address, private_key, version=3)

    def get_pool_data(self, pool_id: str) -> Dict:
        """
        Get pool data from Uniswap V3
        """
        try:
            pool_data = self.uniswap.get_pool(pool_id)
            return pool_data
        except Exception as e:
            print(f"An error occurred while getting pool data: {str(e)}")
            return {}
