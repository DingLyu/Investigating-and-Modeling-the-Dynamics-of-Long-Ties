from utils import *

def generate_path():
    G1 = nx.read_gexf('G_Duration_Season_1.gexf')
    def findPaths(G,u,n):
        if n == 0:
            return [[u]]
        paths = [[u]+path for neighbor in G.neighbors(u) for path in findPaths(G,neighbor,n-1) if u not in path]
        return paths
    Path = []
    count = 0
    for node in G1.nodes():
        count += 1
        Path += findPaths(G1, node, 3)
        print(count, node)
    Pathdict = {}
    for p in Path:
        if (p[0], p[-1]) in Pathdict:
            Pathdict[(p[0], p[-1])] += 1
        else:
            Pathdict[(p[0], p[-1])] = 1
    Results = {}
    for edge in G1.edges():
        a = 1
        b = len(list(nx.common_neighbors(G1, edge[0], edge[1])))
        if (edge[0], edge[1]) in Pathdict:
            c = Pathdict[(edge[0], edge[1])]
        else:
            c = 0
        Results[(edge[0], edge[1])] = [a, b, c]
        Results[(edge[1], edge[0])] = [a, b, c]
    np.save('Path.npy', Results)

def Processing():
    G = nx.read_gexf('Graph/Season/Duration/G_Duration_Season_1.gexf')
    G2 = nx.read_gexf('Graph/Season/Duration/G_Duration_Season_2.gexf')

    Lookup = dict()
    count = 0
    for node in G.nodes():
        Lookup[node] = count
        count += 1
    A_adj = np.zeros(shape=(nx.number_of_nodes(G), nx.number_of_nodes(G)))
    for edge in G.edges():
        if G2.has_node(edge[0]) and G2.has_node(edge[1]):
            if G2.has_edge(edge[0], edge[1]):
                A_adj[Lookup[edge[0]]][Lookup[edge[1]]] = G2.get_edge_data(edge[0], edge[1])['weight']
                A_adj[Lookup[edge[1]]][Lookup[edge[0]]] = G2.get_edge_data(edge[0], edge[1])['weight']
    for i in range(len(A_adj)):
        A_adj[i] = np.squeeze(np.log(A_adj[i] + 1))
        if np.sum(A_adj[i]) > 0:
            A_adj[i] = A_adj[i] / np.sum(A_adj[i])
    A_adj = torch.tensor(A_adj, dtype=torch.float32)
    Path = np.load('Path.npy', allow_pickle=True).item()
    A = []
    I = [1 for i in range(nx.number_of_edges(G))]
    B = []
    C = []
    for edge in G.edges():
        a,b,c = Path[edge]
        A.append(b)
        B.append(c)
        C.append(A_adj[Lookup[edge[0]]][Lookup[edge[1]]])

    ALL = np.array([I,A,B,C])
    np.save('baseline1.npy', ALL)

class Benefit2(nn.Module):
    def __init__(self):
        super(Benefit2, self).__init__()
        self.delta = torch.nn.Parameter(torch.FloatTensor([0.03]), requires_grad=True)

    def forward(self, I, A, B):
        self.Y = I * self.delta +A * (self.delta ** 2)
        return self.Y

class Benefit3(nn.Module):
    def __init__(self):
        super(Benefit3, self).__init__()
        self.delta = torch.nn.Parameter(torch.FloatTensor([0.03]), requires_grad=True)

    def forward(self, I, A, B):
        self.Y = I * self.delta +A * (self.delta ** 2) + B * (self.delta ** 3)
        return self.Y

def model_run():
    X = np.load('baseline1.npy')
    I = torch.tensor(X[0])
    A = torch.tensor(X[1])
    B = torch.tensor(X[2])
    C = torch.tensor(X[3])
    model = Benefit2()
    epochs = 2000
    lr = 0.001
    optimizer = torch.optim.Adam(model.parameters(), lr, weight_decay=0.001)
    loss_fn = torch.nn.MSELoss(reduction='mean')
    t0 = time.time()
    for epoch in range(epochs):
        C_hat = model(I, A, B)

        loss = loss_fn(C_hat, C)
        print(epoch, time.time() - t0, loss)
        for parameters in model.parameters():
            print(parameters)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

def Evaluation():
    G = nx.read_gexf('Graph/Season/Duration/G_Duration_Season_1.gexf')
    Edges = list(G.edges()).copy()
    Pathnsv = np.load('Path.npy', allow_pickle=True)
    Path = Pathnsv.item()
    def Cij():
        C = {}
        delta = 0.034 # 2 dimension: 0.034,  3 dimension: 0.0313
        for node in G.nodes():
            C[node] = {}
            for y in nx.neighbors(G, node):
                a, b, c = Path[(node, y)]
                u = a * delta + b * (delta ** 2) # + c * (delta ** 3)
                C[node][y] = u
        return C
    C = Cij()
    X = [2, 3, 4, 5, 6]
    H = [[] for i in range(5)]
    Y = []
    Err = []
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
            if tr >= 6:
                H[4].append(C[edge[0]][edge[1]])
                H[4].append(C[edge[1]][edge[0]])
            else:
                H[tr - 2].append(C[edge[0]][edge[1]])
                H[tr - 2].append(C[edge[1]][edge[0]])
    for i in range(5):
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    fig = plt.figure(figsize=(7, 7))
    ax = plt.axes()
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#34495e", ls='-', label='Model',
                 ecolor='#34495e', marker='8', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.xticks([2, 3, 4, 5, 6], ['2', '3', '4', '5', '$\geq6$'], fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel("Tie Range", fontsize=25)
    plt.ylabel("Average Benefits", fontsize=25)
    plt.subplots_adjust(left=0.215, bottom=0.11, right=0.98, top=0.97)
    plt.savefig('secondorder_baseline1.pdf',format='pdf')
    plt.show()

