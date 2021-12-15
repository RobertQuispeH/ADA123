from recorrido import *

def Floyd_Warshall(graph,path):
    n = len(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if not(graph[i][j] == min(graph[i][j], graph[i][k] + graph[k][j])):
                    graph[i][j] = graph[i][k] + graph[k][j]
                    path[i][j] = k+1

graph = [[0   ,2631,2845,1406,INF ,INF ,INF ,INF ,1257,INF ,INF ,280 ,INF ], 
         [2631,0   ,2973,2555,INF ,INF ,INF ,INF ,1966,1518,INF ,INF ,INF ],
         [2845,2973,0   ,INF ,6794,INF ,4815,5393,1824,4444,5259,2907,5650],
         [1406,2555,INF ,0   ,INF ,INF ,INF ,INF ,INF ,3288,INF ,INF ,INF ],
         [INF ,INF ,6794,INF ,0   ,1103,INF ,INF ,INF ,2882,INF ,INF ,1401],
         [INF ,INF ,INF ,INF ,1103,0   ,INF ,INF ,INF ,1816,INF ,INF ,INF ],
         [INF ,INF ,4815,INF ,INF ,INF ,0   ,INF ,INF ,INF ,444 ,INF ,2164],
         [INF ,INF ,5393,INF ,INF ,INF ,INF ,0   ,INF ,INF ,393 ,INF ,INF ],
         [1257,1966,1824,INF ,INF ,INF ,INF ,INF ,0   ,INF ,INF ,INF ,INF ],
         [INF ,1518,4444,3288,2882,1816,INF ,INF ,INF ,0   ,INF ,INF ,INF ],
         [INF ,INF ,5259,INF ,INF ,INF ,444 ,393 ,INF ,INF ,0   ,INF ,INF ],
         [280 ,INF ,2907,INF ,INF ,INF ,INF ,INF ,INF ,INF ,INF ,0   ,INF ], 
         [INF ,INF ,5650,INF ,1401,INF ,2164,INF ,INF ,INF ,INF ,INF ,0   ]]

a = rec(13)
Floyd_Warshall(graph,a)
printdis(graph)
printdf(a)


                    