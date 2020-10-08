"""
733. Flood Fill

An image is represented by a 2-D array of integers, 
each integer representing the pixel value of the image (from 0 to 65535).
Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, 
and a pixel value newColor, "flood fill" the image.
To perform a "flood fill", consider the starting pixel, 
plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel,
plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel),
and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

>>> s = Solution()
>>> s.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)
[[2, 2, 2], [2, 2, 0], [2, 0, 1]]
"""
from collections import deque
from typing import List

class Solution:
    
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image:
            return image
        rows = len(image)
        cols = len(image[0])
        pick_color = image[sr][sc]
        if pick_color == newColor:
            return image
        
        def nextPixels(x, y):
            # print("initial", x, y)
            res = []
            for d in Solution.directions:
                _x = x + d[0]
                _y = y + d[1]
                # print("derived", _x, _y)
                if _x >= 0 and \
                    _x < rows and \
                    _y >= 0 and \
                    _y < cols and \
                    image[_x][_y] == pick_color:
                    res.append((_x, _y))
            return res
                    
        q = deque()
        q.append((sr, sc))
        while q:
            next_point = q.popleft()
            image[next_point[0]][next_point[1]] = newColor
            next_pixels = nextPixels(next_point[0], next_point[1])
            for p in next_pixels:
                q.append(p)
        return image

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)