def explore((sx,sy),(tx,ty)):
    marked=[[0 for i in range(n)] for j in range(m)]
    marked[sx][sy]=1
    queue1 = [(sx,sy)]
    while queue != []:
        (ax,ay) = queue.pop()
        for (nx,ny) in #neighbours((ax,ay)):
            if !marked[nx][ny]:
                marked[nx][ny] = 1
                queue.insert(0,(nx,ny))
    return (marked[tx][ty])
