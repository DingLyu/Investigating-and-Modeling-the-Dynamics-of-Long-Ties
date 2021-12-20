# python3
# -*- coding: utf-8 -*-
"""
@author: ding lyu
@email: dylan_lyu@sjtu.edu.cn
"""

# For data preprocessing
from utils import *

def DataCollection(flag):
    # ID, call number, message number, duration, source, target
    year = ['2015', '2016']
    month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    file = 'Data/CODED-' + year[int(flag/12)] + month[int(flag%12)] + '-AndorraTelecom-CDR.csv.gz.csv'
    print(file)
    Data = []
    with open(file) as f:
        for line in csv.reader(f):
            Data.append(line)
    del Data[0]
    return Data

# phase: month, season, halfyear
def Graph(phase):
    count = 0
    if phase == 'month':
        filename_F = 'G_Frequency_Month_'
        filename_D = 'G_Duration_Month_'
        interval = 1
    if phase == 'season':
        filename_F = 'G_Frequency_Season_'
        filename_D = 'G_Duration_Season_'
        interval = 3
    if phase == 'halfyear':
        filename_F = 'G_Frequency_Halfyear_'
        filename_D = 'G_Duration_Halfyear_'
        interval = 6
    for flag in range(24):
        if interval == 1:
            Data = DataCollection
            construction = True
        else:
            if flag % interval == 0:
                count += 1
                construction = False
                Data = DataCollection(flag)
            else:
                Data += DataCollection(flag)
                if flag % interval == interval-1:
                    construction = True
        if construction:
            G_F = nx.Graph()
            G_D = nx.Graph()
            for data in Data:
                if int(data[1]) != 0 and int(float(data[3])) != 0:
                    if G_F.has_edge(data[4], data[5]):
                        G_F.get_edge_data(data[4], data[5])['weight'] += int(data[1])
                    else:
                        G_F.add_edge(data[4], data[5], weight=int(data[1]))
                    if G_D.has_edge(data[4], data[5]):
                        G_D.get_edge_data(data[4], data[5])['weight'] += int(float(data[3]))
                    else:
                        G_D.add_edge(data[4], data[5], weight=int(float(data[3])))
            nx.write_gexf(G_F, filename_F + str(count) + '.gexf')
            nx.write_gexf(G_D, filename_D + str(count) + '.gexf')


months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
days = ['31', '28', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31']

def G_Weeks():
    initial_day = 105
    week_file = {}
    today = initial_day
    for week in range(50):
        week_file[week] = []
        for day in range(7):
            if today > 1000:
                week_file[week].append('days/2015.' + str(today)[:2] + '.' + str(today)[2:])
            else:
                week_file[week].append('days/2015.0'+str(today)[0]+'.'+str(today)[1:])
            today += 1
            if today % 100 > int(days[today//100-1]):
                today = (today//100+1)*100 +1

    G_F = [nx.Graph() for i in range(50)]
    G_D = [nx.Graph() for i in range(50)]
    for week in range(50):
        Data = []
        for day in range(7):
            try:
                Data += read(week_file[week][day])
                print(week_file[week][day])
            except:
                continue
        for data in Data:
            if int(float(data[3])) != 0 and int(data[2]) != 0:
                if G_F[week].has_edge(data[0], data[1]):
                    G_F[week].get_edge_data(data[0], data[1])['weight'] += int(data[2])
                else:
                    G_F[week].add_edge(data[0], data[1], weight = int(data[2]))
                if G_D[week].has_edge(data[0], data[1]):
                    G_D[week].get_edge_data(data[0], data[1])['weight'] += int(float(data[3]))
                else:
                    G_D[week].add_edge(data[0], data[1], weight = int(float(data[3])))
        nx.write_gexf(G_F[week], 'G_Frequency_Week_{}.gexf'.format(week))
        nx.write_gexf(G_D[week], 'G_Duration_Week_{}.gexf'.format(week))

def G_Days():
    initial_day = 102
    day_file = {}
    today = initial_day
    for day in range(361):
        if today == 201 or today == 301 or today == 401:
            today += 1
        if today > 1000:
            day_file[day] = 'days/2015.' + str(today)[:2] + '.' + str(today)[2:]
        else:
            day_file[day] = 'days/2015.0' + str(today)[0] + '.' + str(today)[1:]
        today += 1
        if today % 100 > int(days[today // 100 - 1]):
            today = (today // 100 + 1) * 100 + 1

    G_F = [nx.Graph() for i in range(361)]
    G_D = [nx.Graph() for i in range(361)]
    for day in range(361):
        try:
            Data = read(day_file[day])
            for data in Data:
                if int(float(data[3])) != 0 and int(data[2]) != 0:
                    if G_F[day].has_edge(data[0], data[1]):
                        G_F[day].get_edge_data(data[0], data[1])['weight'] += int(data[2])
                    else:
                        G_F[day].add_edge(data[0], data[1], weight=int(data[2]))
                    if G_D[day].has_edge(data[0], data[1]):
                        G_D[day].get_edge_data(data[0], data[1])['weight'] += int(float(data[3]))
                    else:
                        G_D[day].add_edge(data[0], data[1], weight=int(float(data[3])))
            nx.write_gexf(G_F[day], 'G_Frequency_Day_{}.gexf'.format(day))
            nx.write_gexf(G_D[day], 'G_Duration_Day_{}.gexf'.format(day))
        except:
            print(day_file[day])

def Sliding_Days(interactions):
    G_day = [nx.read_gexf('G_{}_Day_{}.gexf'.format(interactions, i)) for i in range(361)]
    for i in range(355):
        for j in [1,2,3,4,5,6]:
            for edge in G_day[i+j].edges():
                if G_day[i].has_edge(edge[0], edge[1]):
                    G_day[i].get_edge_data(edge[0], edge[1])['weight'] += G_day[i+j].get_edge_data(edge[0], edge[1])['weight']
                else:
                    G_day[i].add_edge(edge[0], edge[1], weight=G_day[i+j].get_edge_data(edge[0], edge[1])['weight'])
        nx.write_gexf(G_day[i], 'G_{}_SlidingDay_{}.gexf'.format(interactions, i))


# drop 5% of all edges in each seasonal snapshots
def DronaEdges(interactions):
    G = [nx.read_gexf('Graph/Season/{}/G_{}_Season_{}.gexf'.format(interactions, interactions, i+1)) for i in range(8)]
    g = [nx.Graph() for i in range(8)]
    for i in range(8):
        loss = int(0.95 * nx.number_of_edges(G[i]))
        E = [t for t in range(nx.number_of_edges(G[i]))]
        keep = sorted(np.random.choice(E, loss, replace=False))
        Edgelist = list(G[i].edges())
        for j in keep:
            g[i].add_edge(Edgelist[j][0], Edgelist[j][1],weight=G[i].get_edge_data(Edgelist[j][0], Edgelist[j][1])['weight'])
        nx.write_gexf(g[i],'drona/{}_drop{}_{}.gexf'.format(interactions,'edge',i+1))

# drop 5% of all nodes in each seasonal snapshots
def DronaNodes(interactions):
    G = [nx.read_gexf('Graph/Season/{}/G_{}_Season_{}.gexf'.format(interactions, interactions, i+1)) for i in range(8)]
    for i in range(8):
        loss = int(0.05 * nx.number_of_nodes(G[i]))
        E = [t for t in range(nx.number_of_nodes(G[i]))]
        keep = sorted(np.random.choice(E, loss, replace=False))
        Nodes = []
        Nodelist = list(G[i].nodes())
        for j in keep:
            Nodes.append(Nodelist[j])
        G[i].remove_nodes_from(Nodes)
        nx.write_gexf(G[i],'drona/{}_drop{}_{}.gexf'.format(interactions,'node',i+1))