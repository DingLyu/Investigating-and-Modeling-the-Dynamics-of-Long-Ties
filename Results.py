from utils import *

# calculation for Fig.~2,3
def Season(interactions):
    Result = []
    count = 0
    G = [nx.read_gexf('Graph/Season/{}/G_{}_Season_{}.gexf'.format(interactions, interactions, i+1)) for i in range(8)]
    Edges = list(G[0].edges()).copy()
    for edge in Edges:
        count += 1
        W = []
        TR = []

        w = G[0].get_edge_data(edge[0], edge[1])['weight']
        G[0].remove_edge(edge[0], edge[1])
        if nx.has_path(G[0], edge[0], edge[1]):
            tr = nx.shortest_path_length(G[0], edge[0], edge[1])
        elif G[0].degree(edge[0]) == 0 or G[0].degree(edge[1]) == 0:
            tr = 101  # upper bond
        else:
            tr = 100
        G[0].add_edge(edge[0], edge[1], weight=w)
        W.append(w)
        TR.append(tr)
        X = [1, 2, 3, 4, 5, 6, 7]
        for _ in X:
            if G[_].has_node(edge[0]) and G[_].has_node(edge[1]):
                if G[_].has_edge(edge[0], edge[1]):
                    w = G[_].get_edge_data(edge[0], edge[1])['weight']
                    G[_].remove_edge(edge[0], edge[1])
                    if nx.has_path(G[_], edge[0], edge[1]):
                        tr = nx.shortest_path_length(G[_], edge[0], edge[1])
                    elif G[_].degree(edge[0]) == 0 or G[_].degree(edge[1]) == 0:
                        tr = 101  # upper bond
                    else:
                        tr = 100
                    G[_].add_edge(edge[0], edge[1], weight=w)
                else:
                    w = 0
                    if nx.has_path(G[_], edge[0], edge[1]):
                        tr = nx.shortest_path_length(G[_], edge[0], edge[1])
                    elif G[_].degree(edge[0]) == 0 or G[_].degree(edge[1]) == 0:
                        tr = 101  # upper bond
                    else:
                        tr = 100
            else:
                w = 0
                tr = -1
            W.append(w)
            TR.append(tr)

        result = [edge[0], edge[1]] + TR + W
        result = list(map(str, result))
        print(count, result)
        Result.append(result)
    write('Results/Graph_Season_TR_{}.txt'.format(interactions), Result)


# calculation for Fig.~4,5,S8
def TRevolution(interactions, a, b):
    file1 = 'Graph/Season/{}/G_{}_Season_{}.gexf'.format(interactions, interactions, a)
    file2 = 'Graph/Season/{}/G_{}_Season_{}.gexf'.format(interactions, interactions, b)
    G1 = nx.read_gexf(file1)
    G2 = nx.read_gexf(file2)
    Edges1 = list(G1.edges()).copy()
    Data = []
    for edge in Edges1:
        w1 = G1.get_edge_data(edge[0], edge[1])['weight']
        G1.remove_edge(edge[0], edge[1])
        if nx.has_path(G1, edge[0], edge[1]):
            tr1 = nx.shortest_path_length(G1, edge[0], edge[1])
        elif G1.degree(edge[0]) == 0 or G1.degree(edge[1]) == 0:
            tr1 = 101
        else:
            tr1 = 100
        G1.add_edge(edge[0], edge[1], weight=w1)

        if G2.has_node(edge[0]) and G2.has_node(edge[1]):
            if G2.has_edge(edge[0], edge[1]):
                w2 = G2.get_edge_data(edge[0], edge[1])['weight']
                G2.remove_edge(edge[0], edge[1])
                if nx.has_path(G2, edge[0], edge[1]):
                    tr2 = nx.shortest_path_length(G2, edge[0], edge[1])
                elif G2.degree(edge[0]) == 0 or G2.degree(edge[1]) == 0:
                    tr2 = 101
                else:
                    tr2 = 100
                G2.add_edge(edge[0], edge[1], weight=w2)
            else:
                w2 = 0
                if nx.has_path(G2, edge[0], edge[1]):
                    tr2 = nx.shortest_path_length(G2, edge[0], edge[1])
                elif G2.degree(edge[0]) == 0 or G2.degree(edge[1]) == 0:
                    tr2 = 101  # upper bond
                else:
                    tr2 = 100
        else:
            w2 = 0
            tr2 = -1
        Data.append([tr1, tr2, w1, w2])
    Data = np.array(Data)
    np.save('Results/trevolution/{}_Season_{}_{}.npy'.format(interactions, a,b), Data)


# calculation for Fig.~6
def Evolution(interactions):
    file1 = 'Graph/Season/{}/G_{}_Season_1.gexf'.format(interactions, interactions)
    file2 = 'Graph/Season/{}/G_{}_Season_2.gexf'.format(interactions, interactions)

    G1 = nx.read_gexf(file1)
    G2 = nx.read_gexf(file2)
    Edges1 = list(G1.edges()).copy()
    Edges2 = list(G2.edges()).copy()
    Data = []
    for edge in Edges1:
        w1 = G1.get_edge_data(edge[0], edge[1])['weight']
        G1.remove_edge(edge[0], edge[1])
        if nx.has_path(G1, edge[0], edge[1]):
            tr1 = nx.shortest_path_length(G1, edge[0], edge[1])
        elif G1.degree(edge[0]) == 0 or G1.degree(edge[1]) == 0:
            tr1 = 101
        else:
            tr1 = 100
        G1.add_edge(edge[0], edge[1], weight=w1)

        if G2.has_node(edge[0]) and G2.has_node(edge[1]):
            if G2.has_edge(edge[0], edge[1]):
                w2 = G2.get_edge_data(edge[0], edge[1])['weight']
                G2.remove_edge(edge[0], edge[1])
                if nx.has_path(G2, edge[0], edge[1]):
                    tr2 = nx.shortest_path_length(G2, edge[0], edge[1])
                elif G2.degree(edge[0]) == 0 or G2.degree(edge[1]) == 0:
                    tr2 = 101
                else:
                    tr2 = 100
                G2.add_edge(edge[0], edge[1], weight=w2)
            else:
                w2 = 0
                if nx.has_path(G2, edge[0], edge[1]):
                    tr2 = nx.shortest_path_length(G2, edge[0], edge[1])
                elif G2.degree(edge[0]) == 0 or G2.degree(edge[1]) == 0:
                    tr2 = 101  # upper bond
                else:
                    tr2 = 100
        else:
            w2 = 0
            tr2 = -1
        data = [tr1, tr2, w1, w2]
        Data.append(list(map(str, data)))
    for edge in Edges2:
        if G1.has_node(edge[0]) and G1.has_node(edge[1]):
            if not G1.has_edge(edge[0], edge[1]):
                w1 = 0
                w2 = G2.get_edge_data(edge[0], edge[1])['weight']
                if nx.has_path(G1, edge[0], edge[1]):
                    tr1 = nx.shortest_path_length(G1, edge[0], edge[1])
                elif G1.degree(edge[0]) == 0 or G1.degree(edge[1]) == 0:
                    tr1 = 101
                else:
                    tr1 = 100

                G2.remove_edge(edge[0], edge[1])
                if nx.has_path(G2, edge[0], edge[1]):
                    tr2 = nx.shortest_path_length(G2, edge[0], edge[1])
                elif G2.degree(edge[0]) == 0 or G2.degree(edge[1]) == 0:
                    tr2 = 101
                else:
                    tr2 = 100
                G2.add_edge(edge[0], edge[1], weight=w2)
            else:
                continue
        else:
            tr1 = -1
            w1 = 0
            w2 = G2.get_edge_data(edge[0], edge[1])['weight']
            G2.remove_edge(edge[0], edge[1])
            if nx.has_path(G2, edge[0], edge[1]):
                tr2 = nx.shortest_path_length(G2, edge[0], edge[1])
            elif G2.degree(edge[0]) == 0 or G2.degree(edge[1]) == 0:
                tr2 = 101
            else:
                tr2 = 100
            G2.add_edge(edge[0], edge[1], weight=w2)
        data = [tr1, tr2, w1, w2]
        Data.append(list(map(str, data)))
    file = 'Results/{}_Season_1_2.txt'.format(interactions)
    write(file, Data)
    print(file)


# calculation for Fig.~S1,S2
def Halfyear(interactions):
    Result = []
    count = 0
    G = [nx.read_gexf('Graph/Halfyear/{}/G_{}_Halfyear_{}.gexf'.format(interactions, interactions, i+1)) for i in range(4)]
    Edges = list(G[0].edges()).copy()

    for edge in Edges:
        count += 1
        W = []
        TR = []

        w = G[0].get_edge_data(edge[0], edge[1])['weight']
        G[0].remove_edge(edge[0], edge[1])
        if nx.has_path(G[0], edge[0], edge[1]):
            tr = nx.shortest_path_length(G[0], edge[0], edge[1])
        elif G[0].degree(edge[0]) == 0 or G[0].degree(edge[1]) == 0:
            tr = 101  # upper bond
        else:
            tr = 100
        G[0].add_edge(edge[0], edge[1], weight=w)
        W.append(w)
        TR.append(tr)
        X = [1, 2, 3]
        for _ in X:
            if G[_].has_node(edge[0]) and G[_].has_node(edge[1]):
                if G[_].has_edge(edge[0], edge[1]):
                    w = G[_].get_edge_data(edge[0], edge[1])['weight']
                    G[_].remove_edge(edge[0], edge[1])
                    if nx.has_path(G[_], edge[0], edge[1]):
                        tr = nx.shortest_path_length(G[_], edge[0], edge[1])
                    elif G[_].degree(edge[0]) == 0 or G[_].degree(edge[1]) == 0:
                        tr = 101  # upper bond
                    else:
                        tr = 100
                    G[_].add_edge(edge[0], edge[1], weight=w)
                else:
                    w = 0
                    if nx.has_path(G[_], edge[0], edge[1]):
                        tr = nx.shortest_path_length(G[_], edge[0], edge[1])
                    elif G[_].degree(edge[0]) == 0 or G[_].degree(edge[1]) == 0:
                        tr = 101  # upper bond
                    else:
                        tr = 100
            else:
                w = 0
                tr = -1
            W.append(w)
            TR.append(tr)

        result = [edge[0], edge[1]] + TR + W
        result = list(map(str, result))
        print(count, result)
        Result.append(result)

    write('Results/Graph_Halfyear_TR_{}.txt'.format(interactions), Result)


# calculation for Fig.~S1,S2
def Month(interactions):
    Result = []
    count = 0
    G = [nx.read_gexf('Graph/Month/{}/G_{}_Month_{}.gexf'.format(interactions, interactions, i+1)) for i in range(24)]

    Edges = list(G[0].edges()).copy()

    for edge in Edges:
        count += 1
        W = []
        TR = []

        w = G[0].get_edge_data(edge[0], edge[1])['weight']
        G[0].remove_edge(edge[0], edge[1])
        if nx.has_path(G[0], edge[0], edge[1]):
            tr = nx.shortest_path_length(G[0], edge[0], edge[1])
        elif G[0].degree(edge[0]) == 0 or G[0].degree(edge[1]) == 0:
            tr = 101  # upper bond
        else:
            tr = 100
        G[0].add_edge(edge[0], edge[1], weight=w)
        W.append(w)
        TR.append(tr)
        X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        for _ in X:
            if G[_].has_node(edge[0]) and G[_].has_node(edge[1]):
                if G[_].has_edge(edge[0], edge[1]):
                    w = G[_].get_edge_data(edge[0], edge[1])['weight']
                    G[_].remove_edge(edge[0], edge[1])
                    if nx.has_path(G[_], edge[0], edge[1]):
                        tr = nx.shortest_path_length(G[_], edge[0], edge[1])
                    elif G[_].degree(edge[0]) == 0 or G[_].degree(edge[1]) == 0:
                        tr = 101  # upper bond
                    else:
                        tr = 100
                    G[_].add_edge(edge[0], edge[1], weight=w)
                else:
                    w = 0
                    if nx.has_path(G[_], edge[0], edge[1]):
                        tr = nx.shortest_path_length(G[_], edge[0], edge[1])
                    elif G[_].degree(edge[0]) == 0 or G[_].degree(edge[1]) == 0:
                        tr = 101  # upper bond
                    else:
                        tr = 100
            else:
                w = 0
                tr = -1
            W.append(w)
            TR.append(tr)

        result = [edge[0], edge[1]] + TR + W
        result = list(map(str, result))
        print(count, result)
        Result.append(result)
    write('Results/Graph_Month_TR_{}.txt'.format(interactions), Result)


# calculation for Fig.~S3
def Week(interactions):
    Result = []
    count = 0
    G = [nx.read_gexf('G_{}_Week_{}.gexf'.format(interactions, i)) for i in range(50)]

    Edges = list(G[0].edges()).copy()

    for edge in Edges:
        count += 1
        W = []
        TR = []

        w = G[0].get_edge_data(edge[0], edge[1])['weight']
        G[0].remove_edge(edge[0], edge[1])
        if nx.has_path(G[0], edge[0], edge[1]):
            tr = nx.shortest_path_length(G[0], edge[0], edge[1])
        elif G[0].degree(edge[0]) == 0 or G[0].degree(edge[1]) == 0:
            tr = 101  # upper bond
        else:
            tr = 100
        G[0].add_edge(edge[0], edge[1], weight=w)
        W.append(w)
        TR.append(tr)
        X = np.arange(1, 50)
        for _ in X:
            if G[_].has_node(edge[0]) and G[_].has_node(edge[1]):
                if G[_].has_edge(edge[0], edge[1]):
                    w = G[_].get_edge_data(edge[0], edge[1])['weight']
                    G[_].remove_edge(edge[0], edge[1])
                    if nx.has_path(G[_], edge[0], edge[1]):
                        tr = nx.shortest_path_length(G[_], edge[0], edge[1])
                    elif G[_].degree(edge[0]) == 0 or G[_].degree(edge[1]) == 0:
                        tr = 101  # upper bond
                    else:
                        tr = 100
                    G[_].add_edge(edge[0], edge[1], weight=w)
                else:
                    w = 0
                    if nx.has_path(G[_], edge[0], edge[1]):
                        tr = nx.shortest_path_length(G[_], edge[0], edge[1])
                    elif G[_].degree(edge[0]) == 0 or G[_].degree(edge[1]) == 0:
                        tr = 101  # upper bond
                    else:
                        tr = 100
            else:
                w = 0
                tr = -1
            W.append(w)
            TR.append(tr)

        result = [edge[0], edge[1]] + TR + W
        result = list(map(str, result))
        print(count, result)
        Result.append(result)
    write('results/Graph_Week_TR_{}.txt'.format(interactions), Result)


# calculation for Fig.~S5
def Sliding_Day(interactions):
    Result = []
    count = 0
    G = [nx.read_gexf('G_{}_SlidingDay_{}.gexf'.format(interactions, i)) for i in range(355)]

    Edges = list(G[0].edges()).copy()

    for edge in Edges:
        count += 1
        W = []
        TR = []

        w = G[0].get_edge_data(edge[0], edge[1])['weight']
        G[0].remove_edge(edge[0], edge[1])
        if nx.has_path(G[0], edge[0], edge[1]):
            tr = nx.shortest_path_length(G[0], edge[0], edge[1])
        elif G[0].degree(edge[0]) == 0 or G[0].degree(edge[1]) == 0:
            tr = 101  # upper bond
        else:
            tr = 100
        G[0].add_edge(edge[0], edge[1], weight=w)
        W.append(w)
        TR.append(tr)
        X = np.arange(1, 355)
        for _ in X:
            if G[_].has_node(edge[0]) and G[_].has_node(edge[1]):
                if G[_].has_edge(edge[0], edge[1]):
                    w = G[_].get_edge_data(edge[0], edge[1])['weight']
                    G[_].remove_edge(edge[0], edge[1])
                    if nx.has_path(G[_], edge[0], edge[1]):
                        tr = nx.shortest_path_length(G[_], edge[0], edge[1])
                    elif G[_].degree(edge[0]) == 0 or G[_].degree(edge[1]) == 0:
                        tr = 101  # upper bond
                    else:
                        tr = 100
                    G[_].add_edge(edge[0], edge[1], weight=w)
                else:
                    w = 0
                    if nx.has_path(G[_], edge[0], edge[1]):
                        tr = nx.shortest_path_length(G[_], edge[0], edge[1])
                    elif G[_].degree(edge[0]) == 0 or G[_].degree(edge[1]) == 0:
                        tr = 101  # upper bond
                    else:
                        tr = 100
            else:
                w = 0
                tr = -1
            W.append(w)
            TR.append(tr)

        result = [edge[0], edge[1]] + TR + W
        result = list(map(str, result))
        print(count, result)
        Result.append(result)
    write('results/Graph_SlidingDay_TR_{}.txt'.format(interactions), Result)


# calculation for Fig.~S6
def SeasonwithDrona(interactions, choice):
    Result = []
    count = 0
    if choice == 1:
        G = [nx.read_gexf('drona/{}_drop{}_{}.gexf'.format(interactions, 'node', i+1)) for i in range(8)]
    if choice == 2:
        G = [nx.read_gexf('drona/{}_drop{}_{}.gexf'.format(interactions, 'edge', i+1)) for i in range(8)]
    Edges = list(G[0].edges()).copy()
    for edge in Edges:
        count += 1
        W = []
        TR = []

        w = G[0].get_edge_data(edge[0], edge[1])['weight']
        G[0].remove_edge(edge[0], edge[1])
        if nx.has_path(G[0], edge[0], edge[1]):
            tr = nx.shortest_path_length(G[0], edge[0], edge[1])
        elif G[0].degree(edge[0]) == 0 or G[0].degree(edge[1]) == 0:
            tr = 101  # upper bond
        else:
            tr = 100
        G[0].add_edge(edge[0], edge[1], weight=w)
        W.append(w)
        TR.append(tr)
        X = [1, 2, 3, 4, 5, 6, 7]
        for _ in X:
            if G[_].has_node(edge[0]) and G[_].has_node(edge[1]):
                if G[_].has_edge(edge[0], edge[1]):
                    w = G[_].get_edge_data(edge[0], edge[1])['weight']
                    G[_].remove_edge(edge[0], edge[1])
                    if nx.has_path(G[_], edge[0], edge[1]):
                        tr = nx.shortest_path_length(G[_], edge[0], edge[1])
                    elif G[_].degree(edge[0]) == 0 or G[_].degree(edge[1]) == 0:
                        tr = 101  # upper bond
                    else:
                        tr = 100
                    G[_].add_edge(edge[0], edge[1], weight=w)
                else:
                    w = 0
                    if nx.has_path(G[_], edge[0], edge[1]):
                        tr = nx.shortest_path_length(G[_], edge[0], edge[1])
                    elif G[_].degree(edge[0]) == 0 or G[_].degree(edge[1]) == 0:
                        tr = 101  # upper bond
                    else:
                        tr = 100
            else:
                w = 0
                tr = -1
            W.append(w)
            TR.append(tr)
        result = [edge[0], edge[1]] + TR + W
        result = list(map(str, result))
        print(count, result)
        Result.append(result)
    if choice == 1:
        write('Results/drona/Graph_Season_TR_{}_{}.txt'.format(interactions, 'Node'), Result)
    if choice == 2:
        write('Results/drona/Graph_Season_TR_{}_{}.txt'.format(interactions, 'Edge'), Result)

# calculation for Fig.~S7
def Trend_Month(interactions):
    Result = []
    count = 0
    G = [nx.read_gexf('Graph/Month/G_{}_Month_{}.gexf'.format(interactions, i+1)) for i in range(24)]

    Edges = list(G[0].edges()).copy()

    for edge in Edges:
        count += 1
        W = []
        TR = []

        w = G[0].get_edge_data(edge[0], edge[1])['weight']
        G[0].remove_edge(edge[0], edge[1])
        if nx.has_path(G[0], edge[0], edge[1]):
            tr = nx.shortest_path_length(G[0], edge[0], edge[1])
        elif G[0].degree(edge[0]) == 0 or G[0].degree(edge[1]) == 0:
            tr = 101  # upper bond
        else:
            tr = 100
        G[0].add_edge(edge[0], edge[1], weight=w)
        W.append(w)
        TR.append(tr)
        X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        for _ in X:
            if G[_].has_node(edge[0]) and G[_].has_node(edge[1]):
                if G[_].has_edge(edge[0], edge[1]):
                    w = G[_].get_edge_data(edge[0], edge[1])['weight']
                    G[_].remove_edge(edge[0], edge[1])
                    if nx.has_path(G[_], edge[0], edge[1]):
                        tr = nx.shortest_path_length(G[_], edge[0], edge[1])
                    elif G[_].degree(edge[0]) == 0 or G[_].degree(edge[1]) == 0:
                        tr = 101  # upper bond
                    else:
                        tr = 100
                    G[_].add_edge(edge[0], edge[1], weight=w)
                else:
                    w = 0
                    if nx.has_path(G[_], edge[0], edge[1]):
                        tr = nx.shortest_path_length(G[_], edge[0], edge[1])
                    elif G[_].degree(edge[0]) == 0 or G[_].degree(edge[1]) == 0:
                        tr = 101  # upper bond
                    else:
                        tr = 100
            else:
                w = 0
                tr = -1
            W.append(w)
            TR.append(tr)

        result = [edge[0], edge[1]] + TR + W
        result = list(map(str, result))
        print(count, result)
        Result.append(result)
    write('Results/descendingorder/Graph_Month_TR_{}.txt'.format(interactions), Result)

# calculation for Fig.~S12
def Existing_Newlyformed_data(interactions):
    Result = []
    count = 0
    G = [nx.read_gexf('Graph/Season/{}/G_{}_Season_{}.gexf'.format(interactions, interactions, i+1) for i in range(8))]
    Edges = list(G[1].edges()).copy()

    for edge in Edges:
        W = []
        TR = []
        if (G[0].has_node(edge[0])) and (G[0].has_node(edge[1])) and (G[0].has_edge(edge[0], edge[1])): # Existing
        # if not ((G[0].has_node(edge[0])) and (G[0].has_node(edge[1])) and (G[0].has_edge(edge[0], edge[1]))): # Newly formed
            count += 1
            X = [1, 2, 3, 4, 5, 6, 7]
            for _ in X:
                if G[_].has_node(edge[0]) and G[_].has_node(edge[1]):
                    if G[_].has_edge(edge[0], edge[1]):
                        w = G[_].get_edge_data(edge[0], edge[1])['weight']
                        G[_].remove_edge(edge[0], edge[1])
                        if nx.has_path(G[_], edge[0], edge[1]):
                            tr = nx.shortest_path_length(G[_], edge[0], edge[1])
                        elif G[_].degree(edge[0]) == 0 or G[_].degree(edge[1]) == 0:
                            tr = 101  # upper bond
                        else:
                            tr = 100
                        G[_].add_edge(edge[0], edge[1], weight=w)
                    else:
                        w = 0
                        if nx.has_path(G[_], edge[0], edge[1]):
                            tr = nx.shortest_path_length(G[_], edge[0], edge[1])
                        elif G[_].degree(edge[0]) == 0 or G[_].degree(edge[1]) == 0:
                            tr = 101  # upper bond
                        else:
                            tr = 100
                else:
                    w = 0
                    tr = -1
                W.append(w)
                TR.append(tr)

            result = [edge[0], edge[1]] + TR + W
            result = list(map(str, result))
            print(count, result)
            Result.append(result)
    write('Results/oldedge/Graph_Season_TR_{}.txt'.format(interactions), Result)
    # write('Results/newedge/Graph_Season_TR_{}.txt'.format(interactions), Result)

