from typing import *

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        #[1, 0, 0, 0, 1, 0, 1]

        for i in range(len(flowerbed)):

            if n == 0:
                return True

            if i == 0 and flowerbed[i] == 0 and len(flowerbed) != 1 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
            elif i == len(flowerbed)-1 and flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
            else:
                if i != 0 and i != len(flowerbed)-1 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    n -= 1
                
        return True if n == 0 else False
    
print(Solution().canPlaceFlowers([1,0,0,0,1], 2))