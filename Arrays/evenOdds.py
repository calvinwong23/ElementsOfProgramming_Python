class Arrays(object):
    def evenOdds(self, arr):
        
        nextEven, nextOdd = 0, len(arr) -1

        while nextEven < nextOdd:
            if arr[nextEven] % 2 == 0:
                nextEven += 1
            else:
                arr[nextEven], arr[nextOdd] = arr[nextOdd], arr[nextEven]
                nextOdd -= 1

        return arr

a = Arrays()
print(a.evenOdds([2,3,5,7,11,13,17,0]))