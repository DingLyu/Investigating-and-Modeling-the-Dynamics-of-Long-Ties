from utils import *

# calculation for Tab.~S1
def G_TR():
    All  = []
    for _ in range(8):
        G = nx.read_gexf('Graph/Season/Frequency/G_frequency_season_%d.gexf'%(_+1))
        Edges = list(G.edges()).copy()
        TR = [0 for i in range(10)]
        for edge in Edges:
            w = G.get_edge_data(edge[0], edge[1])['weight']
            G.remove_edge(edge[0], edge[1])
            if nx.has_path(G, edge[0], edge[1]):
                tr = nx.shortest_path_length(G, edge[0], edge[1])
            elif G.degree(edge[0]) == 0 or G.degree(edge[1]) == 0:
                tr = 101  # upper bond
            else:
                tr = 100
            G.add_edge(edge[0], edge[1], weight=w)
            if tr < 100:
                TR[tr] += 1
        All.append(TR)
    All = np.array(All)
    np.save('Results/statistics_tr.npy', All)


# Tab.~S1
def StatisticsTR():
    Data = np.load('Results/statistics_tr.npy')
    S = [sum(Data[i]) for i in range(8)]
    A = [[0 for j in range(5)] for i in range(8)]
    B = [[0 for j in range(5)] for i in range(8)]
    for i in range(8):
        for j in range(2, 10):
            if j >= 6:
                A[i][4] += Data[i][j]
            else:
                A[i][j - 2] = Data[i][j]
    for i in range(8):
        for j in range(5):
            B[i][j] = A[i][j]/S[i]
    A = np.array(A).T
    B = np.array(B).T
    print(A)
    print(B)


# calculation for Tab.~S2
def Statistics():
    GD = [nx.read_gexf('Graph/Month/Duration/G_Duration_Month_{}.gexf'.format(i+1)) for i in range(24)]
    GF = [nx.read_gexf('Graph/Month/Frequency/G_Frequency_Month_{}.gexf'.format(i + 1)) for i in range(24)]
    duration = [[] for i in range(24)]
    frequency = [[] for j in range(24)]
    Deg = [[] for i in range(24)]
    TR = [[] for i in range(24)]
    for i in range(24):
        for edge in GD[i].edges():
            duration[i].append(np.log(GD[i].get_edge_data(edge[0], edge[1])['weight']+1))
        for edge in GF[i].edges():
            frequency[i].append(np.log(GF[i].get_edge_data(edge[0], edge[1])['weight']+1))
        for node in GF[i].nodes():
            Deg[i].append(GF[i].degree(node))
        Edges = list(GF[i].edges()).copy()
        for edge in Edges:
            w = GF[i].get_edge_data(edge[0], edge[1])['weight']
            frequency[i].append(np.log(GF[i].get_edge_data(edge[0], edge[1])['weight'] + 1))
            GF[i].remove_edge(edge[0], edge[1])
            if nx.has_path(GF[i], edge[0], edge[1]):
                tr = nx.shortest_path_length(GF[i], edge[0], edge[1])
            elif GF[i].degree(edge[0]) == 0 or GF[i].degree(edge[1]) == 0:
                tr = 101  # upper bond
            else:
                tr = 100
            GF[i].add_edge(edge[0], edge[1], weight=w)
            if tr < 100:
                TR[i].append(tr)
    np.save('Results/duration.npy', duration)
    np.save('Results/frequency.npy', frequency)
    np.save('Results/Deg.npy', Deg)
    np.save('Results/TR.npy', TR)

# Tab.~S2
def table_show():
    duration = np.load('Results/duration.npy')
    frequency = np.load('Results/frequency.npy')
    Deg = np.load('Results/Deg.npy')
    TR = np.load('Results/TR.npy')

    A = [[] for i in range(24)]
    for i in range(24):
        l = len(duration[i])
        x = sorted(duration[i])
        A[i] += [x[0], x[int(0.25 * l)], sum(x) / l, x[int(0.25 * l)], x[int(0.75 * l)], x[-1]]
        l = len(frequency[i])
        x = sorted(frequency[i])
        A[i] += [x[0], x[int(0.25 * l)], sum(x) / l, x[int(0.25 * l)], x[int(0.75 * l)], x[-1]]
        l = len(Deg[i])
        x = sorted(Deg[i])
        A[i] += [x[0], x[int(0.25 * l)], sum(x) / l, x[int(0.25 * l)], x[int(0.75 * l)], x[-1]]
        l = len(TR[i])
        x = sorted(TR[i])
        A[i] += [x[0], x[int(0.25*l)], sum(x)/l, x[int(0.25 * l)], x[int(0.75*l)], x[-1]]
    A = np.around(np.array(A).transpose(), decimals=2)

    for i in range(24):
        x = map(str, A[i])
        print("&".join(x))