class Solution(object):

    # @param nestedList a list, each element in the list
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    @staticmethod
    def flatten(nestedList):
        # Write your code here
        result = []
        if isinstance(nestedList,int):
            return [nestedList]
        while nestedList:
            if isinstance(nestedList[0], int):

                result.append(nestedList.pop(0))
            elif isinstance(nestedList[0], list):
                temp = nestedList.pop(0)
                nestedList = temp + nestedList
        return result
        pass


if __name__ == '__main__':
    test_array = [4, [3, [2, [1]]]]
    print(Solution.flatten(test_array))
