from typing import List


def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    if image[sr][sc] == color:
        return image

    flood(image, sr, sc, image[sr][sc], color)

    return image


def flood(image: List[List[int]], sr: int, sc: int, color: int, new_color: int):
    if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[sr]) or image[sr][sc] != color:
        return

    image[sr][sc] = new_color

    flood(image, sr + 1, sc, color, new_color)
    flood(image, sr - 1, sc, color, new_color)
    flood(image, sr, sc + 1, color, new_color)
    flood(image, sr, sc - 1, color, new_color)

    return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2

print(floodFill(image, sr, sc, color))
