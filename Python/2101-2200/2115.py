from collections import defaultdict


class Solution:
    def findAllRecipes(
        self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]
    ) -> list[str]:
        g = defaultdict(list)
        indeg = defaultdict(int)
        for a, b in zip(recipes, ingredients):
            for v in b:
                g[v].append(a)
            indeg[a] += len(b)
        print(dict(g))
        print(dict(indeg))

        q = supplies
        ans = []
        for i in q:
            for j in g[i]:
                indeg[j] -= 1
                if indeg[j] == 0:
                    ans.append(j)
                    q.append(j)
        return ans


recipes = ["bread", "sandwich", "burger"]
ingredients = [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]]
supplies = ["yeast", "flour", "meat"]
print(Solution().findAllRecipes(recipes, ingredients, supplies))
