class Solution:
    def insertInterval(self, intervals, newinterval):
        r_i = -1
        for i in range(len(intervals)):
            if intervals[i][1] >= newinterval[0]:
                r_i = i
                break
        if r_i == -1:
            r_i = len(intervals)-1
        intervals.insert(r_i+1, newinterval)
        a = []
        intervals.sort()
        for i in range(len(intervals)):
            if not a:
                a.append(intervals[i])
            elif a[-1][1] >= intervals[i][0]:
                a[-1][1] = max(a[-1][1], intervals[i][1])
            else:
                a.append(intervals[i])
        return a

# 
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        intervals = [list(map(int, input().split())) for i in range(N)]
        newEvent = list(map(int, input().split()))
        ob = Solution()
        res = ob.insertInterval(intervals, newEvent)
        print('[', end='')
        for i in range(len(res)):
            print('[', end='')
            print(str(res[i][0])+','+str(res[i][1]), end='')
            print(']', end='')
            if i < len(res)-1:
                print(',', end='')
        print(']')
        print("~")
