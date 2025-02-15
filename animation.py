FPS = 60
def lerp(a, b, t):
    rect = (a[0],[1])
    list_pos = []
    for i in range(int(FPS*t)+1):
        rectx = a[0] + (b[0] - a[0]) * i/(FPS*t)
        recty = a[1] + (b[1] - a[1]) * i/(FPS*t)
        list_pos.append((rectx, recty))
    return list_pos
