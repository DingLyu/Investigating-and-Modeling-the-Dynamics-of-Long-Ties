# /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ding lyu
@email: dylan_lyu@sjtu.edu.cn
"""
from utils import *


# Fig.~2
def DynamicTrend(interactions):
    Data = read('Results/Graph_Season_TR_{}.txt'.format(interactions))
    avg2, avg3, avg4, avg5, avg6 = [], [], [], [], []
    GH = nx.read_gexf('Graph/Season/Frequency/G_frequency_season_1.gexf')
    Large = max(nx.connected_components(GH), key=len)
    for data in Data:
        if data.count('-1') == 0:
            if data[0] in Large and data[1] in Large:
                if data[2] == '2':
                    avg2.append(list(map(int, map(float, data[10:]))))
                if data[2] == '3':
                    avg3.append(list(map(int, map(float, data[10:]))))
                if data[2] == '4':
                    avg4.append(list(map(int, map(float, data[10:]))))
                if data[2] == '5':
                    avg5.append(list(map(int, map(float, data[10:]))))
                if int(data[2]) >= 6 and int(data[2]) < 100:
                    avg6.append(list(map(int, map(float, data[10:]))))
    fig = plt.figure(figsize=(7, 7))
    ax = plt.axes()
    X = [1, 2, 3, 4, 5, 6, 7, 8]
    H = [[] for i in range(8)]
    Y = []
    Err = []
    for i in range(8):
        for j in range(len(avg2)):
            H[i].append(mt.log(avg2[j][i]+1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o",color="#34495e", ls='-', label='$=2$',
                 ecolor='#34495e',marker='^', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = [1, 2, 3, 4, 5, 6, 7, 8]
    H = [[] for i in range(8)]
    Y = []
    Err = []
    for i in range(8):
        for j in range(len(avg3)):
            H[i].append(mt.log(avg3[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#2980b9", ls='-', label='$=3$',
                 ecolor='#2980b9', marker='s', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = [1, 2, 3, 4, 5, 6, 7, 8]
    H = [[] for i in range(8)]
    Y = []
    Err = []
    for i in range(8):
        for j in range(len(avg4)):
            H[i].append(mt.log(avg4[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#7f8c8d", ls='-', label='$=4$',
                 ecolor='#7f8c8d', marker='p', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = [1, 2, 3, 4, 5, 6, 7, 8]
    H = [[] for i in range(8)]
    Y = []
    Err = []
    for i in range(8):
        for j in range(len(avg5)):
            H[i].append(mt.log(avg5[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#c0392b", ls='-', label='$=5$',
                 ecolor='#c0392b', marker='H', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = [1, 2, 3, 4, 5, 6, 7, 8]
    H = [[] for i in range(8)]
    Y = []
    Err = []
    for i in range(8):
        for j in range(len(avg6)):
            H[i].append(mt.log(avg6[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#8e44ad", ls='-', label='$\geq6$',
                 ecolor='#8e44ad', marker='8', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8], ['1', '2', '3', '4', '5', '6', '7', '8'], fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel("Phase", fontsize=25)
    plt.ylabel("$log$(Interaction {})".format(interactions), fontsize=25)
    legend = plt.legend(frameon=False, loc='upper right', title='Tie Range in Phase 1', fontsize=20)
    legend.get_title().set_fontsize(fontsize=20)
    if interactions == 'Duration':
        plt.ylim([0,6])
        plt.subplots_adjust(left=0.11, bottom=0.11, right=0.98, top=0.97)
        # plt.savefig('Plots/Manuscript/Mainresults_Duration.pdf', format='pdf')
    if interactions == 'Frequency':
        plt.ylim([0,2.5])
        plt.subplots_adjust(left=0.145, bottom=0.11, right=0.98, top=0.97)
        # plt.savefig('Plots/Manuscript/Mainresults_Frequency.pdf', format='pdf')
    plt.show()


# Fig.~3a
def PersistentProbability():
    Data = read('Results/Graph_Season_TR_Frequency.txt')
    avg2, avg3, avg4, avg5, avg6 = [], [], [], [], []
    GH = nx.read_gexf('Graph/Season/Frequency/G_frequency_season_1.gexf')
    Large = max(nx.connected_components(GH), key=len)
    for data in Data:
        if data.count('-1') == 0:
            if data[0] in Large and data[1] in Large:
                if data[2] == '2':
                    avg2.append(list(map(int, map(float, data[10:]))))
                if data[2] == '3':
                    avg3.append(list(map(int, map(float, data[10:]))))
                if data[2] == '4':
                    avg4.append(list(map(int, map(float, data[10:]))))
                if data[2] == '5':
                    avg5.append(list(map(int, map(float, data[10:]))))
                if int(data[2]) >= 6 and int(data[2]) <= 100:
                    avg6.append(list(map(int, map(float, data[10:]))))
    H = []
    Count = [0 for _ in range(7)]
    for data in avg2:
        for _ in range(7):
            if data[_ + 1] == 0:
                Count[_] += 1
    for _ in range(7):
        H.append([1 - Count[_] / len(avg2), '$=2$', int(_ + 2)])

    Count = [0 for _ in range(7)]
    for data in avg3:
        for _ in range(7):
            if data[_ + 1] == 0:
                Count[_] += 1
    for _ in range(7):
        H.append([1 - Count[_] / len(avg3), '$=3$', int(_ + 2)])

    Count = [0 for _ in range(7)]
    for data in avg4:
        for _ in range(7):
            if data[_ + 1] == 0:
                Count[_] += 1
    for _ in range(7):
        H.append([1 - Count[_] / len(avg4), '$=4$', int(_ + 2)])

    Count = [0 for _ in range(7)]
    for data in avg5:
        for _ in range(7):
            if data[_ + 1] == 0:
                Count[_] += 1
    for _ in range(7):
        H.append([1 - Count[_] / len(avg5), '$=5$', int(_ + 2)])

    Count = [0 for _ in range(7)]
    for data in avg6:
        for _ in range(7):
            if data[_ + 1] == 0:
                Count[_] += 1
    for _ in range(7):
        H.append([1 - Count[_] / len(avg6), '$\geq6$', int(_ + 2)])

    H.append([1, '$=2$', 1])
    H.append([1, '$=3$', 1])
    H.append([1, '$=4$', 1])
    H.append([1, '$=5$', 1])
    H.append([1, '$\geq6$', 1])

    fig = plt.figure(figsize=(7, 7))
    ax = plt.axes()
    X =[1,2,3,4,5,6,7,8]
    Y = [1,0.5581061427155416,0.4903426618125226,0.4811593128854058,0.42835042473760754,0.39420158284622064,0.3522280583114866,0.34217701568950765]
    plt.plot(X,Y,color='#34495e',label='$=2$',marker='^',markersize=10, linewidth=2)
    Y = [1,0.29881545026224554,0.23813227842474882,0.2341763712329985,0.1989287936705485,0.18211618810560937,0.15236909947550892,0.1509023024268824]
    plt.plot(X, Y, color='#2980b9', label='$=3$', marker='s', markersize=10, linewidth=2)
    Y = [1,0.3226499719678565,0.266305363483461,0.25456301002927806 , 0.22232604497601693, 0.20460350090325796, 0.17548121846383857, 0.17124525010901392]
    plt.plot(X, Y, color='#7f8c8d', label='$=4$', marker='p', markersize=10, linewidth=2)
    Y = [1,0.4494784876140808,0.42046936114732725, 0.39374185136897, 0.3539765319426337, 0.34680573663624514, 0.3158409387222947, 0.29269882659713164]
    plt.plot(X, Y, color='#c0392b', label='$=5$', marker='H', markersize=10, linewidth=2)
    Y = [1,0.6121212121212121,0.5454545454545454, 0.5212121212121212, 0.49696969696969695, 0.49696969696969695, 0.48484848484848486,0.4666666666666667]
    plt.plot(X, Y, color='#8e44ad', label='$\geq6$', marker='8', markersize=10, linewidth=2)
    plt.xlabel('Phase', fontsize=25)
    plt.ylabel('Persistence Probability', fontsize=25)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.ylim([0, 1.05])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    legend = plt.legend(frameon=False, loc='upper right', title='Tie Range in Phase 1', fontsize=20)
    legend.get_title().set_fontsize(fontsize=20)
    plt.subplots_adjust(left=0.145, bottom=0.11, right=0.98, top=0.97)
    plt.savefig('Plots/Manuscript/PersistentProbability.pdf', format='pdf')
    plt.show()


# Fig.~3b&c
def IncrementInteraction(interactions):
    Data = read('Results/Graph_Season_TR_{}.txt'.format(interactions))
    avg2, avg3, avg4, avg5, avg6 = [], [], [], [], []
    GH = nx.read_gexf('Graph/Season/Frequency/G_frequency_season_1.gexf')
    Large = max(nx.connected_components(GH),key=len)
    for data in Data:
        if data.count('-1') == 0:
            if data[0] in Large and data[1] in Large:
                if data[2] == '2':
                    avg2.append(list(map(int, map(float, data[10:]))))
                if data[2] == '3':
                    avg3.append(list(map(int, map(float, data[10:]))))
                if data[2] == '4':
                    avg4.append(list(map(int, map(float, data[10:]))))
                if data[2] == '5':
                    avg5.append(list(map(int, map(float, data[10:]))))
                if int(data[2]) >= 6 and int(data[2]) <= 100:
                    avg6.append(list(map(int, map(float, data[10:]))))
    plt.figure(figsize=(7, 7))
    ax = plt.axes()
    X = [1, 2, 3, 4, 5, 6, 7, 8]
    H = [[] for i in range(8)]
    Y = []
    Err = []
    for i in range(8):
        for j in range(len(avg2)):
            if avg2[j][i] != 0:
                H[i].append(mt.log(avg2[j][i] + 1)-mt.log(avg2[j][0]+1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#34495e", ls='-', label='$=2$',
                 ecolor='#34495e', marker='^', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = [1, 2, 3, 4, 5, 6, 7, 8]
    H = [[] for i in range(8)]
    Y = []
    Err = []
    for i in range(8):
        for j in range(len(avg3)):
            if avg3[j][i] != 0:
                H[i].append(mt.log(avg3[j][i] + 1)-mt.log(avg3[j][0] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#2980b9", ls='-', label='$=3$',
                 ecolor='#2980b9', marker='s', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = [1, 2, 3, 4, 5, 6, 7, 8]
    H = [[] for i in range(8)]
    Y = []
    Err = []
    for i in range(8):
        for j in range(len(avg4)):
            if avg4[j][i] != 0:
                H[i].append(mt.log(avg4[j][i] + 1)-mt.log(avg4[j][0] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#7f8c8d", ls='-', label='$=4$',
                 ecolor='#7f8c8d', marker='p', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = [1, 2, 3, 4, 5, 6, 7, 8]
    H = [[] for i in range(8)]
    Y = []
    Err = []
    for i in range(8):
        for j in range(len(avg5)):
            if avg5[j][i] != 0:
                H[i].append(mt.log(avg5[j][i] + 1)-mt.log(avg5[j][0] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#c0392b", ls='-', label='$=5$',
                 ecolor='#c0392b', marker='H', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = [1, 2, 3, 4, 5, 6, 7, 8]
    H = [[] for i in range(8)]
    Y = []
    Err = []
    for i in range(8):
        for j in range(len(avg6)):
            if avg6[j][i] != 0:
                H[i].append(mt.log(avg6[j][i] + 1)-mt.log(avg6[j][0] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#8e44ad", ls='-', label='$\geq6$',
                 ecolor='#8e44ad', marker='8', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.xlabel('Phase', fontsize=25)
    plt.ylabel('$\Delta log$(Interaction {})'.format(interactions), fontsize=25)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.ylim([-0.4, 0.8])
    legend = plt.legend(frameon=False, loc='upper right', title='Tie Range in Phase 1', fontsize=20)
    legend.get_title().set_fontsize(fontsize=20)
    if interactions == 'Duration':
        plt.ylim([-0.5, 1.5])
        plt.subplots_adjust(left=0.205, bottom=0.11, right=0.98, top=0.97)
        plt.savefig('Plots/Manuscript/IncrementDuration.pdf', format='pdf')
    if interactions == 'Frequency':
        plt.ylim([-0.5, 1.5])
        plt.subplots_adjust(left=0.205, bottom=0.11, right=0.98, top=0.97)
        plt.savefig('Plots/Manuscript/IncrementFrequency.pdf', format='pdf')
    plt.show()


# Fig.~4
def TransitionTR(a, b):
    Data = np.load('Results/trevolution/Frequency_Season_{}_{}.npy'.format(a, b))
    plt.figure(figsize=(7,7))
    DS = []
    for data in Data:
        if -1 in data or 101 in data[:2] or 100 in data[:2]:
            continue
        else:
            x = list(map(int,map(float, data[:4])))
            if x[0] > 6:
                x[0] = 6
            if x[1] > 6:
                x[1] = 6
            DS.append(x)
    A = [[0 for j in range(6)] for i in range(5)]
    B = [[0 for j in range(5)] for i in range(5)]
    for data in DS:
        if data[2] > 0:
            if data[3] == 0:
                A[int(data[0])-2][5] += 1
            else:
                if int(data[1]) >= 6:
                    A[int(data[0])-2][4] +=1
                else:
                    A[int(data[0])-2][int(data[1])-2] += 1
    for data in DS:
        B[int(data[1])-2][int(data[0])-2] += 1

    EA = [sum(A[i][:5]) for i in range(5)]
    NormA = [[0 for j in range(5)] for i in range(5)]
    for i in range(5):
        for j in range(5):
            NormA[i][j] = A[i][j]/EA[i]
    NormA = np.array(NormA)
    h = sns.heatmap(data=NormA, cmap='YlOrBr', annot=True, annot_kws={'size':15}, cbar=False)
    cb = h.figure.colorbar(h.collections[0])
    cb.ax.tick_params(labelsize=20)
    plt.xticks([0.5,1.5,2.5,3.5,4.5],['$2$', '$3$', '$4$', '$5$', '$\geq6$'], fontsize=20)
    plt.yticks([0.5,1.5,2.5,3.5,4.5],['$2$', '$3$', '$4$', '$5$', '$\geq6$'], fontsize=20)
    plt.xlabel('Tie Range in Phase %d'%b, fontsize=25)
    plt.ylabel('Tie Range in Phase %d'%a, fontsize=25)
    plt.subplots_adjust(left=0.12, bottom=0.11, right=1, top=0.98)
    plt.savefig('Plots/Manuscript/Transition_P{}_P{}.pdf'.format(a,b), format='pdf')
    # plt.show()


# Fig.~5,S8,
def InteractionTR(interactions, a, b):
    Data = np.load('Results/trevolution/{}_Season_{}_{}.npy'.format(interactions, a, b))
    plt.figure(figsize=(7, 7))
    DS = []
    for data in Data:
        if -1 in data or 101 in data[:2] or 100 in data[:2]:
            continue
        else:
            x = list(map(int, map(float, data)))
            if x[0] > 6:
                x[0] = 6
            if x[1] > 6:
                x[1] = 6
            DS.append(x)
    All = []
    for i in range(5):
        for j in range(5):
            H = []
            for data in DS:
                if data[2] != 0:
                    if data[0] == i + 2 and data[1] == j + 2:
                        H.append(mt.log(data[3] + 1))
                        All.append([i + 2, j + 2, mt.log(data[3] + 1)])
    df = pd.DataFrame(All, columns=['Tie Range in Phase a', 'Tie Range in Phase b', '$Ln({})$ in Phase b'.format(interactions)])
    A = df.groupby(['Tie Range in Phase a', 'Tie Range in Phase b'])['$Ln({})$ in Phase b'.format(interactions)].mean()
    NormA = np.array(list(A)).reshape(5,5)
    h = sns.heatmap(data=NormA, cmap='YlOrBr', annot=True, annot_kws={'size': 15}, cbar=False)
    cb = h.figure.colorbar(h.collections[0])
    cb.ax.tick_params(labelsize=20)
    plt.xticks([0.5, 1.5, 2.5, 3.5, 4.5], ['$2$', '$3$', '$4$', '$5$', '$\geq6$'], fontsize=20)
    plt.yticks([0.5, 1.5, 2.5, 3.5, 4.5], ['$2$', '$3$', '$4$', '$5$', '$\geq6$'], fontsize=20)
    plt.xlabel('Tie Range in Phase {}'.format(b), fontsize=25)
    plt.ylabel('Tie Range in Phase {}'.format(a), fontsize=25)
    plt.title('$log$({}) in Phase {}'.format(interactions, b), fontsize=30)
    plt.subplots_adjust(left=0.12, bottom=0.11, right=1, top=0.93)
    if b <= 2:
        plt.savefig('Plots/Manuscript/Evolution_P{}_P{}_{}.pdf'.format(a, b, interactions), format='pdf')
    if b > 2:
        plt.savefig('Plots/SI/Evolution_P{}_P{}_{}.pdf'.format(a, b, interactions), format='pdf')
    # plt.show()


# Fig.~5,S8,
def PPTR(a, b):
    Data = np.load('Results/trevolution/Frequency_Season_%d_%d.npy'%(a, b))
    plt.figure(figsize=(7,7))
    DS = []
    for data in Data:
        if -1 in data or 101 in data[:2] or 100 in data[:2]:
            continue
        else:
            x = list(map(int,map(float, data[:4])))
            if x[0] > 6:
                x[0] = 6
            if x[1] > 6:
                x[1] = 6
            DS.append(x)
    A = [[0 for j in range(5)] for i in range(5)]
    B = [[0 for j in range(5)] for i in range(5)]
    for data in DS:
        if data[2] > 0:
            if data[3] != 0:
                A[int(data[0])-2][int(data[1])-2] += 1
            B[int(data[0]) - 2][int(data[1]) - 2] += 1

    NormA = [[0 for j in range(5)] for i in range(5)]
    for i in range(5):
        for j in range(5):
            NormA[i][j] = A[i][j]/B[i][j]
    NormA = np.array(NormA)
    h = sns.heatmap(data=NormA, cmap='YlOrBr', annot=True, annot_kws={'size':15}, cbar=False)
    cb = h.figure.colorbar(h.collections[0])
    cb.ax.tick_params(labelsize=20)
    plt.xticks([0.5,1.5,2.5,3.5,4.5],['$2$', '$3$', '$4$', '$5$', '$\geq6$'], fontsize=20)
    plt.yticks([0.5,1.5,2.5,3.5,4.5],['$2$', '$3$', '$4$', '$5$', '$\geq6$'], fontsize=20)
    plt.xlabel('Tie Range in Phase %d'%b, fontsize=25)
    plt.ylabel('Tie Range in Phase %d'%a, fontsize=25)
    plt.title('Persistence Probability', fontsize=30)
    plt.subplots_adjust(left=0.12, bottom=0.11, right=1, top=0.93)
    if b <= 2:
        plt.savefig('Plots/Manuscript/PersistenceProbability_P{}_P{}.pdf'.format(a, b), format='pdf')
    else:
        plt.savefig('Plots/SI/PersistenceProbability_P{}_P{}.pdf'.format(a, b), format='pdf')
    # plt.show()

# Fig.~6
def old_new(interactions):
    fig = plt.figure(figsize=(7.2,7.2))
    ax = plt.axes()
    Data = read('Results/{}_season_1_2.txt'.format(interactions))
    DS = []
    for data in Data:
        if '-1' in data or '101' in data[:2] or '100' in data[:2]:
            continue
        else:
            x = list(map(int,map(float, data)))
            if x[0] > 6:
                x[0] = 6
            if x[1] > 6:
                x[1] = 6
            DS.append(x)

    X = [2,3,4,5,6]
    H = [[] for i in range(5)]
    Y = []
    Err = []
    for i in range(5):
        for j in range(len(DS)):
            if DS[j][2] == 0:
                H[DS[j][1]-2].append(mt.log(DS[j][3] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#34495e", ls='--', label='New in Phase 2',
                 ecolor='#34495e', marker='d', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = [2,3,4,5,6]
    H = [[] for i in range(5)]
    Y = []
    Err = []
    for i in range(5):
        for j in range(len(DS)):
            if DS[j][3] != 0:
                H[DS[j][1] - 2].append(mt.log(DS[j][3] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#2980b9", ls='-', label='Existing in Phase 1',
                 ecolor='#2980b9', marker='o', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    plt.xlabel('Tie Range in Phase 2', fontsize=25)
    plt.ylabel('$log$(Interaction {}) in Phase 2'.format(interactions), fontsize=25)
    plt.xticks([2,3,4,5,6], ['2', '3', '4', '5','$\geq6$'],fontsize=20)
    plt.yticks(fontsize=20)
    if interactions == 'Frequency':
        plt.ylim([0.8, 2])
    if interactions == 'Duration':
        plt.ylim([3, 6])
    legend = plt.legend(frameon=False, loc='upper right', title='Tie Status', fontsize=20)
    legend.get_title().set_fontsize(fontsize=20)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.subplots_adjust(left=0.145, bottom=0.11, right=0.98, top=0.97)
    plt.savefig('Plots/Manuscript/ExistingvsNew_{}.pdf'.format(interactions), format='pdf')
    # plt.show()
