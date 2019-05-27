ss = '200 0 200 10 200 50 200 30 200 25'


def find_min(s):
    xy = s.split()
    xy = list(map(int, xy))
    x, y = [0], [0]
    for i in range(5):
        x.append(xy[i * 2])
        y.append(xy[i * 2 + 1])

    dis = [[0 for _ in range(6)] for _ in range(6)]
    for i in range(6):
        for j in range(6):
            dis[i][j] = (abs(x[i] - x[j]) ** 2 + abs(y[i] - y[j]) ** 2) ** 0.5

    min_dis = float('inf')


    for i in range(6):
        print(dis[i])
    pass

def find_path(j):
    path_vertexs.append(j)
    row=c[j]
    copy_row=[value for value in row]
    walked_vertex=[]
    for i in path_vertexs:
        walked_vertex.append(copy_row[i])
    for vertex in walked_vertex:
        copy_row.remove(vertex)
    if len(path_vertexs)<5:
        min_e=min(copy_row)
        j=row.index(min_e)
        path_length.append(min_e)
        find_path(j)
    else:
        min_e=c[j][0]
        path_length.append(min_e)
        path_vertexs.append(0)
    return path_vertexs,path_length

if __name__ == "__main__":
    c=[[0,3,1,5,8],
    [3,0,6,7,9],
    [1,6,0,4,2],
    [5,7,4,0,3],
    [8,9,2,3,0]]
    path_length=[]
    path_vertexs=[]
    path_vertexs,path_length=find_path(0)
    print(path_length)

print(find_min(ss))
