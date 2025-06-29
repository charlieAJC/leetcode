class Solution(object):
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # 紀錄每個球的顏色
        ball_info = {}
        # 統計每種顏色的出現次數
        showed_color = {}
        # 保存結果
        res = []

        for query in queries:
            # 解構查詢參數
            ball_id, color = query

            # 若該球之前有顏色，移除其對應顏色的統計
            if ball_id in ball_info:
                prev_color = ball_info[ball_id]
                showed_color[prev_color] -= 1
                if showed_color[prev_color] == 0:
                    del showed_color[prev_color]

            # 更新該球的新顏色的統計
            if color in showed_color:
                showed_color[color] += 1
            else:
                showed_color[color] = 1

            # 更新球的顏色
            ball_info[ball_id] = color
            # 記錄當前顏色種類數
            res.append(len(showed_color))
        return res


# limit = 4
# queries = [[1, 4], [2, 5], [1, 3], [3, 4]]

limit = 4
queries = [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]

print(Solution().queryResults(limit, queries))
