class Solution(object):

    @staticmethod
    def min_sub_string(source, target):
        char_set = set(list(target))
        target_count = {}
        source_count = {}
        for i in char_set:
            source_count[i] = 0
            target_count[i] = list(target).count(i)
        start = 0
        end = -1
        min_len = len(source)
        found = 0
        for i in range(len(source)):
            if source[i] in char_set:
                source_count[source[i]] += 1
                found = found + 1 if source_count[source[i]] <= target_count[source[i]] else found
            if found == len(target):
                while start < i:
                    if source[start] in char_set:
                        if source_count[source[start]] > target_count[source[start]]:
                            source_count[source[start]] -= 1
                            start += 1
                        else:
                            break
                    else:
                        start += 1
                if i - start < min_len:
                    end = i
                    min_len = i - start
                source_count[source[start]] -= 1
                found -= 1
        return source[start:end + 1] if end != -1 else ''

        # while end > 0:
        #     if source[end] not in char_set:
        #         end -= 1
        #     elif origin_count[source[end]] > target_count[source[end]]:
        #         origin_count[source[end]] -= 1
        #         end -= 1
        #     else:
        #         break
        # while start<len(source):
        #     if source[start] not in char_set:
        #         start += 1
        #     elif origin_count[source[start]] > target_count[source[start]]:
        #         origin_count[source[start]] -= 1
        #         start += 1
        #     else:
        #         break


if __name__ == '__main__':
    print(Solution.min_sub_string('absdfaabab', 'adb'))
    pass
