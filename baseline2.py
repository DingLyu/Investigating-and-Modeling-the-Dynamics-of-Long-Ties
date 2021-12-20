from utils import *

class C(nn.Module):
    def __init__(self, G, k):
        super(C, self).__init__()
        self.G = G #
        self.N = nx.number_of_nodes(G)
        self.lookup = {}  # reindex nodes

        count = 0
        for node in self.G.nodes():
            self.lookup[node] = torch.LongTensor([count])
            count += 1
        self.endowments = nn.Embedding(self.N, k, max_norm=1.0).requires_grad_(True) #using nn.Embedding
        self.c = {}

    def forward(self, x): # input a node of the Graph
        self.c[x] = torch.zeros(self.N) # generate a tensor with N dimension
        for j in self.G.neighbors(x): # find utility for all neighbors of this node
            u = torch.sum(torch.relu((self.endowments(self.lookup[j])-self.endowments(self.lookup[x])).squeeze()))
            self.c[x][self.lookup[j][0]] = u # insert the utility
        self.c[x] = torch.softmax(self.c[x], 0) # softmax
        return self.c[x]

def learning_endowments(dimension=4):
    n_sample = 1000
    G = nx.read_gexf('Graph/Season/Duration/G_Duration_Season_1.gexf')
    G2 = nx.read_gexf('Graph/Season/Duration/G_Duration_Season_2.gexf')
    Lookup = dict()
    count = 0
    for node in G.nodes():
        Lookup[node] = count
        count += 1
    A = np.zeros(shape=(nx.number_of_nodes(G), nx.number_of_nodes(G)))
    for edge in G.edges():
        if G2.has_node(edge[0]) and G2.has_node(edge[1]):
            if G2.has_edge(edge[0], edge[1]):
                A[Lookup[edge[0]]][Lookup[edge[1]]] = G2.get_edge_data(edge[0], edge[1])['weight']
                A[Lookup[edge[1]]][Lookup[edge[0]]] = G2.get_edge_data(edge[0], edge[1])['weight']
    for i in range(len(A)):
        A[i] = np.squeeze(np.log(A[i] + 1))
        if np.sum(A[i]) > 0:
            A[i] = A[i] / np.sum(A[i])
    A = torch.tensor(A, dtype=torch.float32)

    Nodes = []
    p = []
    for node in G.nodes():
        Nodes.append(node)
        p.append(G.degree(node) ** (3 / 4))
    sum_p = sum(p)
    p = np.array(p) / sum_p

    epochs = 400
    lr = 0.001
    model = C(G=G, k=dimension)   # dimension of endowment vectors default 4
    optimizer = torch.optim.Adam(model.parameters(), lr, weight_decay=0.001)
    loss_fn = torch.nn.MSELoss(reduction='mean')
    t0 = time.time()
    for epoch in range(epochs):
        random_node = np.random.choice(Nodes, n_sample, p=p.ravel())
        indices = torch.tensor([Lookup[node] for node in random_node])
        ADJ = torch.index_select(A, 0, indices)

        ADJ_hat = []
        for node in random_node:
            ADJ_hat.append(model(node).unsqueeze(0))
        ADJ_hat = torch.cat(ADJ_hat)

        loss = loss_fn(ADJ_hat, ADJ)
        print(epoch, time.time() - t0, loss)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if epoch % 100 == 99:
            H = []
            for node in G.nodes():
                H.append([int(node)] + model.endowments(model.lookup[node]).detach().numpy().tolist()[0])
            df = pd.DataFrame(H)
            df.to_csv('endowments_baseline2.csv', index=False, header=False)

def evaluation():
    G = nx.read_gexf('Graph/Season/Duration/G_Duration_Season_1.gexf')
    Edges = list(G.edges()).copy()
    endowments = read_endowments('endowments_baseline2.csv')

    def Cij():
        C = {}
        for node in G.nodes():
            C[node] = {}
            for y in nx.neighbors(G, node):
                u = np.sum(np.maximum(np.array(endowments[y] - np.array((endowments[node]))), 0))
                C[node][y] = u
            C[node]['all'] = np.sum(np.exp(np.array(list(C[node].values()))))
            for y in C[node]:
                if y != 'all':
                    C[node][y] = np.exp(C[node][y]) / C[node]['all']
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
    plt.subplots_adjust(left=0.17, bottom=0.11, right=0.98, top=0.97)
    plt.savefig('baseline2.pdf', format='pdf')
    plt.show()