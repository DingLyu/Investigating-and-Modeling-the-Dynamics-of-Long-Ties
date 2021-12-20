# /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ding lyu
@email: dylan_lyu@sjtu.edu.cn
"""
from utils import *

# Fig.~S1a&c
def Analysis_halfyear(interactions):
    Data = read('Results/Graph_Halfyear_TR_{}.txt'.format(interactions))
    avg2, avg3, avg4, avg5, avg6 = [], [], [], [], []
    for data in Data:
        if data.count('-1') == 0:
            if data[2] == '2':
                avg2.append(list(map(int, map(float, data[6:]))))
            if data[2] == '3':
                avg3.append(list(map(int, map(float, data[6:]))))
            if data[2] == '4':
                avg4.append(list(map(int, map(float, data[6:]))))
            if data[2] == '5':
                avg5.append(list(map(int, map(float, data[6:]))))
            if int(data[2]) >= 6 and int(data[2]) < 100:
                avg6.append(list(map(int, map(float, data[6:]))))

    fig = plt.figure(figsize=(7, 7))
    ax = plt.axes()
    X = [1, 2, 3, 4]
    H = [[] for i in range(4)]
    Y = []
    Err = []
    for i in range(4):
        for j in range(len(avg2)):
            H[i].append(mt.log(avg2[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#34495e", ls='-', label='$=2$',
                 ecolor='#34495e', marker='^', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = [1, 2, 3, 4]
    H = [[] for i in range(4)]
    Y = []
    Err = []
    for i in range(4):
        for j in range(len(avg3)):
            H[i].append(mt.log(avg3[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#2980b9", ls='-', label='$=3$',
                 ecolor='#2980b9', marker='s', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = [1, 2, 3, 4]
    H = [[] for i in range(4)]
    Y = []
    Err = []
    for i in range(4):
        for j in range(len(avg4)):
            H[i].append(mt.log(avg4[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#7f8c8d", ls='-', label='$=4$',
                 ecolor='#7f8c8d', marker='p', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = [1, 2, 3, 4]
    H = [[] for i in range(4)]
    Y = []
    Err = []
    for i in range(4):
        for j in range(len(avg5)):
            H[i].append(mt.log(avg5[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#c0392b", ls='-', label='$=5$',
                 ecolor='#c0392b', marker='H', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = [1, 2, 3, 4]
    H = [[] for i in range(4)]
    Y = []
    Err = []
    for i in range(4):
        for j in range(len(avg6)):
            H[i].append(mt.log(avg6[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#8e44ad", ls='-', label='$\geq6$',
                 ecolor='#8e44ad', marker='8', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.xticks([1, 2, 3, 4], ['1', '2', '3', '4'], fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel("Phase", fontsize=25)
    plt.ylabel("$log$(Interaction {})".format(interactions), fontsize=25)

    legend = plt.legend(frameon=False, loc='upper right', title='Tie Range in Phase 1', fontsize=20)
    legend.get_title().set_fontsize(fontsize=20)
    if interactions == 'Frequency':
        plt.ylim([0, 2.5])
        plt.subplots_adjust(left=0.145, bottom=0.11, right=0.98, top=0.97)
        # plt.savefig('Plots/SI/RobustnessCheck_HY_F.pdf', format='pdf')
    if interactions == 'Duration':
        plt.ylim([0, 7])
        plt.subplots_adjust(left=0.11, bottom=0.11, right=0.98, top=0.97)
        # plt.savefig('Plots/SI/RobustnessCheck_HY_D.pdf', format='pdf')
    plt.show()


# Fig.~S1b&d
def Analysis_month(interactions):
    Data = read('opendata/Results/Graph_Month_TR_{}.txt'.format(interactions))
    avg2, avg3, avg4, avg5, avg6 = [], [], [], [], []
    for data in Data:
        if data.count('-1') == 0:
            if data[2] == '2':
                avg2.append(list(map(int, map(float, data[26:]))))
            if data[2] == '3':
                avg3.append(list(map(int, map(float, data[26:]))))
            if data[2] == '4':
                avg4.append(list(map(int, map(float, data[26:]))))
            if data[2] == '5':
                avg5.append(list(map(int, map(float, data[26:]))))
            if int(data[2]) >= 6 and int(data[2]) < 100:
                avg6.append(list(map(int, map(float, data[26:]))))

    fig = plt.figure(figsize=(14, 7))
    ax = plt.axes()
    X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    H = [[] for i in range(24)]
    Y = []
    Err = []
    for i in range(24):
        for j in range(len(avg2)):
            H[i].append(mt.log(avg2[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#34495e", ls='-', label='$=2$',
                 ecolor='#34495e', marker='^', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    H = [[] for i in range(24)]
    Y = []
    Err = []
    for i in range(24):
        for j in range(len(avg3)):
            H[i].append(mt.log(avg3[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#2980b9", ls='-', label='$=3$',
                 ecolor='#2980b9', marker='s', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    H = [[] for i in range(24)]
    Y = []
    Err = []
    for i in range(24):
        for j in range(len(avg4)):
            H[i].append(mt.log(avg4[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#7f8c8d", ls='-', label='$=4$',
                 ecolor='#7f8c8d', marker='p', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    H = [[] for i in range(24)]
    Y = []
    Err = []
    for i in range(24):
        for j in range(len(avg5)):
            H[i].append(mt.log(avg5[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#c0392b", ls='-', label='$=5$',
                 ecolor='#c0392b', marker='H', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    H = [[] for i in range(24)]
    Y = []
    Err = []
    for i in range(24):
        for j in range(len(avg6)):
            H[i].append(mt.log(avg6[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#8e44ad", ls='-', label='$\geq6$',
                 ecolor='#8e44ad', marker='8', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
               ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                '20', '21', '22', '23', '24'], fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel("Phase", fontsize=25)
    plt.ylabel("$log$(Interaction {})".format(interactions), fontsize=25)

    legend = plt.legend(frameon=False, loc='upper right', title='Tie Range in Phase 1', fontsize=20)
    legend.get_title().set_fontsize(fontsize=20)
    if interactions == 'Frequency':
        plt.ylim([0, 2])
        plt.subplots_adjust(left=0.09, bottom=0.11, right=0.98, top=0.97)
        # plt.savefig('Plots/SI/RobustnessCheck_M_F.pdf', format='pdf')
    if interactions == 'Duration':
        plt.ylim([0, 6])
        plt.subplots_adjust(left=0.06, bottom=0.11, right=0.98, top=0.97)
        # plt.savefig('Plots/SI/RobustnessCheck_M_D.pdf', format='pdf')
    plt.show()


# Fig.~S2(a)
def Persistent_ProbabilityHY():
    fig = plt.figure(figsize=(7, 7))
    ax = plt.axes()
    Data = read('Results/Graph_Halfyear_TR_Frequency.txt')
    avg2, avg3, avg4, avg5, avg6 = [], [], [], [], []
    GH = nx.read_gexf('Graph/Halfyear/Frequency/G_Frequency_Halfyear_1.gexf')
    Large = max(nx.connected_components(GH), key=len)
    for data in Data:
        if data.count('-1') == 0:
            if data[0] in Large and data[1] in Large:
                if data[2] == '2':
                    avg2.append(list(map(int, map(float, data[6:]))))
                if data[2] == '3':
                    avg3.append(list(map(int, map(float, data[6:]))))
                if data[2] == '4':
                    avg4.append(list(map(int, map(float, data[6:]))))
                if data[2] == '5':
                    avg5.append(list(map(int, map(float, data[6:]))))
                if int(data[2]) >= 6 and int(data[2]) <= 100:
                    avg6.append(list(map(int, map(float, data[6:]))))
    H = []
    Count = [0 for _ in range(3)]
    for data in avg2:
        for _ in range(3):
            if data[_ + 1] == 0:
                Count[_] += 1
    for _ in range(3):
        H.append([1 - Count[_] / len(avg2), '$=2$', int(_ + 2)])

    Count = [0 for _ in range(3)]
    for data in avg3:
        for _ in range(3):
            if data[_ + 1] == 0:
                Count[_] += 1
    for _ in range(3):
        H.append([1 - Count[_] / len(avg3), '$=3$', int(_ + 2)])

    Count = [0 for _ in range(3)]
    for data in avg4:
        for _ in range(3):
            if data[_ + 1] == 0:
                Count[_] += 1
    for _ in range(3):
        H.append([1 - Count[_] / len(avg4), '$=4$', int(_ + 2)])

    Count = [0 for _ in range(3)]
    for data in avg5:
        for _ in range(3):
            if data[_ + 1] == 0:
                Count[_] += 1
    for _ in range(3):
        H.append([1 - Count[_] / len(avg5), '$=5$', int(_ + 2)])

    Count = [0 for _ in range(3)]
    for data in avg6:
        for _ in range(3):
            if data[_ + 1] == 0:
                Count[_] += 1
    for _ in range(3):
        H.append([1 - Count[_] / len(avg6), '$\geq6$', int(_ + 2)])

    H.append([1, '$=2$', 1])
    H.append([1, '$=3$', 1])
    H.append([1, '$=4$', 1])
    H.append([1, '$=5$', 1])
    H.append([1, '$\geq6$', 1])
    TR = ['$=2$', '$=3$', '$=4$', '$=5$', '$\geq6$']
    result = [0 for _ in range(4)]
    for tr in TR:
        for h in H:
            if h[1] == tr:
                result[h[2] - 1] = h[0]
        print(tr, result)

    X = [1, 2, 3, 4]
    Y = [1, 0.5198435241847288, 0.42654463428219314, 0.3555069087329271]
    plt.plot(X, Y, color='#34495e', label='$=2$', marker='^', markersize=10, linewidth=2)
    Y = [1, 0.24877016233119698, 0.1885505247553232, 0.14666597830175454]
    plt.plot(X, Y, color='#2980b9', label='$=3$', marker='s', markersize=10, linewidth=2)
    Y = [1, 0.28445115376320895, 0.2249730429156782, 0.18266120336424407]
    plt.plot(X, Y, color='#7f8c8d', label='$=4$', marker='p', markersize=10, linewidth=2)
    Y = [1, 0.46226415094339623, 0.4231805929919138, 0.39622641509433965]
    plt.plot(X, Y, color='#c0392b', label='$=5$', marker='H', markersize=10, linewidth=2)
    Y = [1, 0.5, 0.5333333333333333, 0.3666666666666667]
    plt.plot(X, Y, color='#8e44ad', label='$\geq6$', marker='8', markersize=10, linewidth=2)
    plt.xlabel('Phase', fontsize=25)
    plt.ylabel('Persistence Probability', fontsize=25)
    plt.xticks([1, 2, 3, 4], ['1', '2', '3', '4'], fontsize=20)
    plt.yticks(fontsize=20)
    plt.ylim([0,1.05])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    legend = plt.legend(frameon=False, loc='upper right', title='Tie Range in Phase 1', fontsize=20)
    legend.get_title().set_fontsize(fontsize=20)
    plt.subplots_adjust(left=0.145, bottom=0.11, right=0.98, top=0.97)
    plt.savefig('Plots/SI/PersistenceProability_HY.pdf', format='pdf')
    # plt.show()

# Fig.~S2(b)
def Persistent_ProbabilityM():
    fig = plt.figure(figsize=(14, 7))
    ax = plt.axes()
    Data = read('Results/Graph_Month_TR_Frequency.txt')
    avg2, avg3, avg4, avg5, avg6 = [], [], [], [], []
    GH = nx.read_gexf('Graph/Month/Frequency/G_Frequency_Month_1.gexf')
    Large = max(nx.connected_components(GH), key=len)
    for data in Data:
        if data.count('-1') == 0:
            if data[0] in Large and data[1] in Large:
                if data[2] == '2':
                    avg2.append(list(map(int, map(float, data[26:]))))
                if data[2] == '3':
                    avg3.append(list(map(int, map(float, data[26:]))))
                if data[2] == '4':
                    avg4.append(list(map(int, map(float, data[26:]))))
                if data[2] == '5':
                    avg5.append(list(map(int, map(float, data[26:]))))
                if int(data[2]) >= 6 and int(data[2]) <= 100:
                    avg6.append(list(map(int, map(float, data[26:]))))
    H = []
    Count = [0 for _ in range(23)]
    for data in avg2:
        for _ in range(23):
            if data[_ + 1] == 0:
                Count[_] += 1
    for _ in range(23):
        H.append([1 - Count[_] / len(avg2), '$=2$', int(_ + 2)])

    Count = [0 for _ in range(23)]
    for data in avg3:
        for _ in range(23):
            if data[_ + 1] == 0:
                Count[_] += 1
    for _ in range(23):
        H.append([1 - Count[_] / len(avg3), '$=3$', int(_ + 2)])

    Count = [0 for _ in range(23)]
    for data in avg4:
        for _ in range(23):
            if data[_ + 1] == 0:
                Count[_] += 1
    for _ in range(23):
        H.append([1 - Count[_] / len(avg4), '$=4$', int(_ + 2)])

    Count = [0 for _ in range(23)]
    for data in avg5:
        for _ in range(23):
            if data[_ + 1] == 0:
                Count[_] += 1
    for _ in range(23):
        H.append([1 - Count[_] / len(avg5), '$=5$', int(_ + 2)])

    Count = [0 for _ in range(23)]
    for data in avg6:
        for _ in range(23):
            if data[_ + 1] == 0:
                Count[_] += 1
    for _ in range(23):
        H.append([1 - Count[_] / len(avg6), '$\geq6$', int(_ + 2)])

    H.append([1, '$=2$', 1])
    H.append([1, '$=3$', 1])
    H.append([1, '$=4$', 1])
    H.append([1, '$=5$', 1])
    H.append([1, '$\geq6$', 1])
    TR = ['$=2$', '$=3$', '$=4$', '$=5$', '$\geq6$']
    result = [0 for _ in range(24)]
    for tr in TR:
        for h in H:
            if h[1] == tr:
                result[h[2] - 1] = h[0]
        print(tr, result)
    X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    Y = [1, 0.6061740692648393, 0.5890802042014265, 0.5341165798039809, 0.5202689482203525, 0.5301944182571728,
         0.5062345470392572, 0.4311175936960814, 0.4795620697628915, 0.4826304274355645, 0.47064159803625105,
         0.4807093687187606, 0.4454277023781995, 0.42871627030007653, 0.42141446841815045, 0.41126665362244086,
         0.39762357921699065, 0.401038794713531, 0.380049449474377, 0.33741261850975646, 0.3652412885323467,
         0.3648143865952792, 0.34965047403902594, 0.36287554029776414]
    plt.plot(X, Y, color='#34495e', label='$=2$', marker='^', markersize=10, linewidth=2)
    Y = [1, 0.3798954096455549, 0.35470656595002903, 0.30177222545031956, 0.28634514816966883, 0.2986345148169669,
         0.27611853573503775, 0.21577571179546773, 0.255520046484602, 0.2624927367809413, 0.2563044741429401,
         0.2607205113306217, 0.23678094131319005, 0.22295177222545037, 0.21751888436955258, 0.2133643230679837,
         0.20615920976176638, 0.20456130156885532, 0.18829169087739683, 0.15424171993027314, 0.18224869262056942,
         0.18326554328878564, 0.17210923881464268, 0.17771644392794883]
    plt.plot(X, Y, color='#2980b9', label='$=3$', marker='s', markersize=10, linewidth=2)
    Y = [1, 0.3520072021933952, 0.3310144453083439, 0.2915660678479355, 0.2776118181446168, 0.28661455988869333,
         0.2633301960142407, 0.212014568073004, 0.24593853582682002, 0.24659328068093467, 0.23562630437451404,
         0.2475344764087245, 0.223554446126775, 0.21160535253918233, 0.20473053157097842, 0.2035028849695134,
         0.195277652739698, 0.19560502516675538, 0.17878626672668496, 0.15488807955149975, 0.17514424847567212,
         0.17293448459303518, 0.16073986168514953, 0.16876048614805417]
    plt.plot(X, Y, color='#7f8c8d', label='$=4$', marker='p', markersize=10, linewidth=2)
    Y = [1, 0.43298040099121426, 0.4210407749493129, 0.38691146654651953, 0.3821806713223699, 0.38161748141473306,
         0.3625816625366074, 0.31223248479387244, 0.3487271908087407, 0.34771344897499434, 0.3242847488173012,
         0.34185627393557105, 0.3232710069835548, 0.29916647893669746, 0.2930840279342194, 0.2995043928812796,
         0.28531200720883076, 0.29342194187880155, 0.272020725388601, 0.24769092137868887, 0.2699932417211084,
         0.2605316512728092, 0.2496057670646542, 0.26300968686641135]
    plt.plot(X, Y, color='#c0392b', label='$=5$', marker='H', markersize=10, linewidth=2)
    Y = [1, 0.5426874536005939, 0.5567928730512249, 0.5248700816629548, 0.5374907201187824, 0.5397178916109874,
         0.5382331106161842, 0.4803266518188567, 0.5048255382331106, 0.51818856718634, 0.4721603563474388,
         0.526354862657758, 0.465478841870824, 0.4506310319227914, 0.4528582034149963, 0.45805493689680776,
         0.4491462509279881, 0.44988864142538976, 0.44840386043058644, 0.4053452115812918, 0.4276169265033407,
         0.42835931700074237, 0.4046028210838901, 0.41870824053452116]
    plt.plot(X, Y, color='#8e44ad', label='$\geq6$', marker='8', markersize=10, linewidth=2)

    plt.xlabel('Phase', fontsize=25)
    plt.ylabel('Persistence Probability', fontsize=25)
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
               ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                '20', '21', '22', '23', '24'], fontsize=20)
    plt.yticks(fontsize=20)
    plt.ylim([0,1.05])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    legend = plt.legend(frameon=False, loc='upper right', title='Tie Range in Phase 1', fontsize=20)
    legend.get_title().set_fontsize(fontsize=20)
    plt.subplots_adjust(left=0.075, bottom=0.11, right=0.98, top=0.97)
    plt.savefig('Plots/SI/PersistencePropbability_M.pdf', format='pdf')
    # plt.show()


# Fig.~S2(c&e)
def IncrementationHY(interactions):
    Data = read('Results/Graph_Halfyear_TR_{}.txt'.format(interactions))
    avg2, avg3, avg4, avg5, avg6 = [], [], [], [], []
    GH = nx.read_gexf('Graph/Halfyear/Frequency/G_Frequency_Halfyear_1.gexf')
    Large = max(nx.connected_components(GH), key=len)
    for data in Data:
        if data.count('-1') == 0:
            if data[0] in Large and data[1] in Large:
                if data[2] == '2':
                    avg2.append(list(map(int, map(float, data[6:]))))
                if data[2] == '3':
                    avg3.append(list(map(int, map(float, data[6:]))))
                if data[2] == '4':
                    avg4.append(list(map(int, map(float, data[6:]))))
                if data[2] == '5':
                    avg5.append(list(map(int, map(float, data[6:]))))
                if int(data[2]) >= 6 and int(data[2]) <= 100:
                    avg6.append(list(map(int, map(float, data[6:]))))
    plt.figure(figsize=(7, 7))
    ax = plt.axes()
    X = [1, 2, 3, 4]
    H = [[] for i in range(4)]
    Y = []
    Err = []
    for i in range(4):
        for j in range(len(avg2)):
            if avg2[j][i] != 0:
                H[i].append(mt.log(avg2[j][i] + 1) - mt.log(avg2[j][0] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#34495e", ls='-', label='$=2$',
                 ecolor='#34495e', marker='^', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)
    X = [1, 2, 3, 4]
    H = [[] for i in range(4)]
    Y = []
    Err = []
    for i in range(4):
        for j in range(len(avg3)):
            if avg3[j][i] != 0:
                H[i].append(mt.log(avg3[j][i] + 1) - mt.log(avg3[j][0] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#2980b9", ls='-', label='$=3$',
                 ecolor='#2980b9', marker='s', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = [1, 2, 3, 4]
    H = [[] for i in range(4)]
    Y = []
    Err = []
    for i in range(4):
        for j in range(len(avg4)):
            if avg4[j][i] != 0:
                H[i].append(mt.log(avg4[j][i] + 1) - mt.log(avg4[j][0] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#7f8c8d", ls='-', label='$=4$',
                 ecolor='#7f8c8d', marker='p', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = [1, 2, 3, 4]
    H = [[] for i in range(4)]
    Y = []
    Err = []
    for i in range(4):
        for j in range(len(avg5)):
            if avg5[j][i] != 0:
                H[i].append(mt.log(avg5[j][i] + 1) - mt.log(avg5[j][0] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#c0392b", ls='-', label='$=5$',
                 ecolor='#c0392b', marker='H', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = [1, 2, 3, 4]
    H = [[] for i in range(4)]
    Y = []
    Err = []
    for i in range(4):
        for j in range(len(avg6)):
            if avg6[j][i] != 0:
                H[i].append(mt.log(avg6[j][i] + 1) - mt.log(avg6[j][0] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#8e44ad", ls='-', label='$\geq6$',
                 ecolor='#8e44ad', marker='8', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.xlabel('Phase', fontsize=25)
    plt.ylabel('$\Delta log$(Interaction {})'.format(interactions), fontsize=25)
    plt.xticks([1,2,3,4],['1','2','3','4'],fontsize=20)
    plt.yticks(fontsize=20)
    plt.ylim([-2, 2])
    legend = plt.legend(frameon=False, loc='upper right', title='Tie Range in Phase 1', fontsize=20)
    legend.get_title().set_fontsize(fontsize=20)
    plt.subplots_adjust(left=0.18, bottom=0.11, right=0.98, top=0.97)
    if interactions == 'Frequency':
        plt.savefig('Plots/SI/IncrementFrequency_HY.pdf', format='pdf')
    if interactions == 'Duration':
        plt.savefig('Plots/SI/IncrementDuration_HY.pdf', format='pdf')
    plt.show()

# Fig.~S2(d&f)
def IncrementationM(interactions):
    Data = read('Results/Graph_Month_TR_{}.txt'.format(interactions))
    avg2, avg3, avg4, avg5, avg6 = [], [], [], [], []
    GH = nx.read_gexf('Graph/Month/Frequency/G_Frequency_Month_1.gexf')
    Large = max(nx.connected_components(GH), key=len)
    for data in Data:
        if data.count('-1') == 0:
            if data[0] in Large and data[1] in Large:
                if data[2] == '2':
                    avg2.append(list(map(int, map(float, data[26:]))))
                if data[2] == '3':
                    avg3.append(list(map(int, map(float, data[26:]))))
                if data[2] == '4':
                    avg4.append(list(map(int, map(float, data[26:]))))
                if data[2] == '5':
                    avg5.append(list(map(int, map(float, data[26:]))))
                if int(data[2]) >= 6 and int(data[2]) <= 100:
                    avg6.append(list(map(int, map(float, data[26:]))))
    plt.figure(figsize=(14, 7))
    ax = plt.axes()
    X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    H = [[] for i in range(24)]
    Y = []
    Err = []
    for i in range(24):
        for j in range(len(avg2)):
            if avg2[j][i] != 0:
                H[i].append(mt.log(avg2[j][i] + 1) - mt.log(avg2[j][0] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#34495e", ls='-', label='$=2$',
                 ecolor='#34495e', marker='^', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)
    X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    H = [[] for i in range(24)]
    Y = []
    Err = []
    for i in range(24):
        for j in range(len(avg3)):
            if avg3[j][i] != 0:
                H[i].append(mt.log(avg3[j][i] + 1) - mt.log(avg3[j][0] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#2980b9", ls='-', label='$=3$',
                 ecolor='#2980b9', marker='s', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    H = [[] for i in range(24)]
    Y = []
    Err = []
    for i in range(24):
        for j in range(len(avg4)):
            if avg4[j][i] != 0:
                H[i].append(mt.log(avg4[j][i] + 1) - mt.log(avg4[j][0] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#7f8c8d", ls='-', label='$=4$',
                 ecolor='#7f8c8d', marker='p', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    H = [[] for i in range(24)]
    Y = []
    Err = []
    for i in range(24):
        for j in range(len(avg5)):
            if avg5[j][i] != 0:
                H[i].append(mt.log(avg5[j][i] + 1) - mt.log(avg5[j][0] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#c0392b", ls='-', label='$=5$',
                 ecolor='#c0392b', marker='H', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    H = [[] for i in range(24)]
    Y = []
    Err = []
    for i in range(24):
        for j in range(len(avg6)):
            if avg6[j][i] != 0:
                H[i].append(mt.log(avg6[j][i] + 1) - mt.log(avg6[j][0] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#8e44ad", ls='-', label='$\geq6$',
                 ecolor='#8e44ad', marker='8', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.xlabel('Phase', fontsize=25)
    plt.ylabel('$\Delta log$(Interaction {})'.format(interactions), fontsize=25)
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
               ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                '20', '21', '22', '23', '24'], fontsize=20)
    plt.yticks(fontsize=20)
    plt.ylim([-0.5, 1.5])
    legend = plt.legend(frameon=False, loc='upper right', title='Tie Range in Phase 1', fontsize=20)
    legend.get_title().set_fontsize(fontsize=20)
    plt.subplots_adjust(left=0.105, bottom=0.11, right=0.98, top=0.97)
    if interactions == 'Frequency':
        plt.savefig('Plots/SI/IncrementFrequency_M.pdf', format='pdf')
    if interactions == 'Duration':
        plt.savefig('Plots/SI/IncrementDuration_M.pdf', format='pdf')
    # plt.show()


# Fig.~S3
def Analysis_Week(interactions):
    Data = read('Results/Graph_Week_TR_{}.txt'.format(interactions))
    avg2, avg3, avg4, avg5, avg6, avg7= [], [], [], [], [], []
    for data in Data:
        if data.count('-1') == 0:
            if data[2] == '2':
                avg2.append(list(map(int, map(float, data[52:]))))
            if data[2] == '3':
                avg3.append(list(map(int, map(float, data[52:]))))
            if data[2] == '4':
                avg4.append(list(map(int, map(float, data[52:]))))
            if data[2] == '5':
                avg5.append(list(map(int, map(float, data[52:]))))
            if data[2] == '6':
                avg6.append(list(map(int, map(float, data[52:]))))
            if int(data[2]) >= 7 and int(data[2]) < 100:
                avg7.append(list(map(int, map(float, data[52:]))))

    fig = plt.figure(figsize=(14, 7))
    ax = plt.axes()
    X = np.arange(1, 51)
    H = [[] for i in range(50)]
    Y = []
    Err = []
    for i in range(50):
        for j in range(len(avg2)):
            H[i].append(mt.log(avg2[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#34495e", ls='-', label='$=2$',
                 ecolor='#34495e', marker='^', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = np.arange(1, 51)
    H = [[] for i in range(50)]
    Y = []
    Err = []
    for i in range(50):
        for j in range(len(avg3)):
            H[i].append(mt.log(avg3[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#2980b9", ls='-', label='$=3$',
                 ecolor='#2980b9', marker='s', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = np.arange(1, 51)
    H = [[] for i in range(50)]
    Y = []
    Err = []
    for i in range(50):
        for j in range(len(avg4)):
            H[i].append(mt.log(avg4[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#7f8c8d", ls='-', label='$=4$',
                 ecolor='#7f8c8d', marker='p', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = np.arange(1, 51)
    H = [[] for i in range(50)]
    Y = []
    Err = []
    for i in range(50):
        for j in range(len(avg5)):
            H[i].append(mt.log(avg5[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#c0392b", ls='-', label='$=5$',
                 ecolor='#c0392b', marker='H', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = np.arange(1, 51)
    H = [[] for i in range(50)]
    Y = []
    Err = []
    for i in range(50):
        for j in range(len(avg6)):
            H[i].append(mt.log(avg6[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#8e44ad", ls='-', label='$=6$',
                 ecolor='#8e44ad', marker='8', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = np.arange(1, 51)
    H = [[] for i in range(50)]
    Y = []
    Err = []
    for i in range(50):
        for j in range(len(avg7)):
            H[i].append(mt.log(avg7[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="green", ls='-', label='$\geq7$',
                 ecolor='green', marker='o', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.xlabel("Phase", fontsize=25)
    plt.ylabel("$log$(Interaction {})".format(interactions), fontsize=25)

    legend = plt.legend(frameon=False, loc='upper right', title='Tie Range in Phase 1', fontsize=20)
    legend.get_title().set_fontsize(fontsize=20)
    if interactions == 'Frequency':
        plt.ylim([0, 2])
        plt.subplots_adjust(left=0.09, bottom=0.11, right=0.98, top=0.97)
        # plt.savefig('Plots/SI/weeks_{}.pdf'.format(interactions), format='pdf')
    if interactions == 'Duration':
        plt.ylim([0, 6])
        plt.subplots_adjust(left=0.06, bottom=0.11, right=0.98, top=0.97)
        # plt.savefig('Plots/SI/weeks_{}.pdf'.format(interactions), format='pdf')
    plt.show()


# Fig.~S4
def showdist():
    plt.figure(figsize=(7,7))
    Data = read('Results/trdistribution/Day_TR.txt')
    TR = []
    for data in Data:
        if int(float(data[2])) < 100:
            TR.append(int(float(data[2])))
    X = np.arange(2, 21)
    Y = []
    for i in X:
        Y.append(TR.count(i) / len(TR))
    plt.plot(X, Y, 'red', label='day')

    Data = read('Results/trdistribution/Week_TR.txt')
    TR = []
    for data in Data:
        if int(float(data[2])) < 100:
            TR.append(int(float(data[2])))
    X = np.arange(2, 21)
    Y = []
    for i in X:
        Y.append(TR.count(i) / len(TR))
    plt.plot(X, Y, 'blue', label='week')

    Data = read('Results/trdistribution/Month_TR.txt')
    TR = []
    for data in Data:
        if int(float(data[2])) < 100:
            TR.append(int(float(data[2])))
    X = np.arange(2, 21)
    Y = []
    for i in X:
        Y.append(TR.count(i) / len(TR))
    plt.plot(X, Y, 'green', label='month')

    Data = read('Results/trdistribution/Season_TR.txt')
    TR = []
    for data in Data:
        if int(float(data[2])) < 100:
            TR.append(int(float(data[2])))
    X = np.arange(2, 21)
    Y = []
    for i in X:
        Y.append(TR.count(i) / len(TR))
    plt.plot(X, Y, 'purple', label='season')

    Data = read('Results/trdistribution/Halfyear_TR.txt')
    TR = []
    for data in Data:
        if int(float(data[2])) < 100:
            TR.append(int(float(data[2])))
    X = np.arange(2, 21)
    Y = []
    for i in X:
        Y.append(TR.count(i) / len(TR))
    plt.plot(X, Y, 'black', label='halfyear')


    plt.xlabel('Tie Range', fontsize=25)
    plt.ylabel('Empirical Probability', fontsize=25)
    plt.xticks([2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 17], ['2', '3', '4', '5', '6', '7', '8', '9', '10', '12', '17'], fontsize=20)
    plt.yticks(fontsize=20)
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    legend = plt.legend(frameon=False, loc='upper right', title='Interval', fontsize=20)
    legend.get_title().set_fontsize(fontsize=20)
    plt.subplots_adjust(left=0.145, bottom=0.11, right=0.98, top=0.97)
    # plt.savefig('Plots/SI/trdistribution.pdf', format='pdf')
    plt.show()


# Fig.~S5
def Analysis_Day(interactions):
    Data = read('results/Graph_SlidingDay_TR_{}.txt'.format(interactions))
    avg2, avg3, avg4, avg5, avg6, avg7 = [], [], [], [], [], []
    for data in Data:
        if data.count('-1') == 0:
            if data[2] == '2':
                avg2.append(list(map(int, map(float, data[357:]))))
            if data[2] == '3':
                avg3.append(list(map(int, map(float, data[357:]))))
            if data[2] == '4':
                avg4.append(list(map(int, map(float, data[357:]))))
            if data[2] == '5':
                avg5.append(list(map(int, map(float, data[357:]))))
            if data[2] == '6':
                avg6.append(list(map(int, map(float, data[357:]))))
            if int(data[2]) >= 7 and int(data[2]) < 100:
                avg7.append(list(map(int, map(float, data[357:]))))

    fig = plt.figure(figsize=(14, 7))
    ax = plt.axes()
    X = np.arange(1, 356)
    H = [[] for i in range(355)]
    Y = []
    Err = []
    for i in range(355):
        for j in range(len(avg2)):
            H[i].append(mt.log(avg2[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#34495e", ls='-', label='$=2$',
                 ecolor='#34495e', marker='^', markersize=1, linewidth=2, elinewidth=0.5, capsize=4)

    X = np.arange(1, 356)
    H = [[] for i in range(355)]
    Y = []
    Err = []
    for i in range(355):
        for j in range(len(avg3)):
            H[i].append(mt.log(avg3[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#2980b9", ls='-', label='$=3$',
                 ecolor='#2980b9', marker='s', markersize=1, linewidth=2, elinewidth=0.5, capsize=4)

    X = np.arange(1, 356)
    H = [[] for i in range(355)]
    Y = []
    Err = []
    for i in range(355):
        for j in range(len(avg4)):
            H[i].append(mt.log(avg4[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#7f8c8d", ls='-', label='$=4$',
                 ecolor='#7f8c8d', marker='p', markersize=1, linewidth=2, elinewidth=0.5, capsize=4)

    X = np.arange(1, 356)
    H = [[] for i in range(355)]
    Y = []
    Err = []
    for i in range(355):
        for j in range(len(avg5)):
            H[i].append(mt.log(avg5[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#c0392b", ls='-', label='$=5$',
                 ecolor='#c0392b', marker='H', markersize=1, linewidth=2, elinewidth=0.5, capsize=4)

    X = np.arange(1, 356)
    H = [[] for i in range(355)]
    Y = []
    Err = []
    for i in range(355):
        for j in range(len(avg6)):
            H[i].append(mt.log(avg6[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#8e44ad", ls='-', label='$=6$',
                 ecolor='#8e44ad', marker='8', markersize=1, linewidth=2, elinewidth=0.5, capsize=4)

    X = np.arange(1, 356)
    H = [[] for i in range(355)]
    Y = []
    Err = []
    for i in range(355):
        for j in range(len(avg7)):
            H[i].append(mt.log(avg7[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="green", ls='-', label='$\geq7$',
                 ecolor='green', marker='o', markersize=1, linewidth=2, elinewidth=0.5, capsize=4)

    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.xlabel("Phase", fontsize=25)
    plt.ylabel("$log$(Interaction {})".format(interactions), fontsize=25)

    legend = plt.legend(frameon=False, loc='upper right', title='Tie Range in Phase 1', fontsize=20, ncol=2)
    legend.get_title().set_fontsize(fontsize=20)
    if interactions == 'Frequency':
        plt.ylim([0, 2])
        plt.subplots_adjust(left=0.09, bottom=0.11, right=0.98, top=0.97)
        # plt.savefig('Plots/SI/slidingdays_{}.pdf'.format(interactions), format='pdf')
    if interactions == 'Duration':
        plt.ylim([0, 6])
        plt.subplots_adjust(left=0.06, bottom=0.11, right=0.98, top=0.97)
        # plt.savefig('Plots/SI/slidingdays_{}.pdf'.format(interactions), format='pdf')
    plt.show()



# Fig.~S6
def drona_plot(interactions, choice):
    Data = read('Results/drona/Graph_Season_TR_{}_{}.txt'.format(interactions, choice))
    avg2, avg3, avg4, avg5, avg6 = [], [], [], [], []
    for data in Data:
        if data.count('-1') == 0:
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
        plt.ylim([0, 7])
        plt.subplots_adjust(left=0.11, bottom=0.11, right=0.98, top=0.97)
    if interactions == 'Frequency':
        plt.ylim([0,2.5])
        plt.subplots_adjust(left=0.17, bottom=0.11, right=0.98, top=0.97)
    plt.savefig('Plots/SI/drona_{}_{}.pdf'.format(choice, interactions), format='pdf')


# Fig.~S7
def Analysis_Trend_Month(interactions):
    Data = read('Results/descendingorder/Graph_Month_TR_{}.txt'.format(interactions))
    avg2 = []
    for data in Data:
        if data.count('-1') == 0:
            avg2.append(list(map(int, map(float, data[26:]))))

    fig = plt.figure(figsize=(14, 7))
    ax = plt.axes()
    X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    H = [[] for i in range(24)]
    Y = []
    Err = []
    for i in range(24):
        for j in range(len(avg2)):
            H[i].append(mt.log(avg2[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#34495e", ls='-', label='Conditional',
                 ecolor='#34495e', marker='^', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    Nodedict = {}
    Data = read('Results/descendingorder/Graph_Month_TR_{}.txt'.format(interactions))
    for data in Data:
        if data.count('-1') == 0:
            Nodedict[data[0]] = 1
            Nodedict[data[1]] = 1

    G_F = [nx.read_gexf('Graph/Month/G_{}_Month_{}.gexf'.format(interactions, i + 1)) for i in range(24)]
    weight = [[] for i in range(24)]
    for i in range(24):
        g = G_F[i]
        weight[i] = []
        for edge in g.edges():
            if edge[0] in Nodedict and edge[1] in Nodedict:
                weight[i].append(mt.log(g.get_edge_data(edge[0], edge[1])['weight'] + 1))
    Y = []
    Err = []
    for i in range(24):
        Y.append(np.mean(weight[i]))
        Err.append(mean_confidence_interval(weight[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="steelblue", ls='-', label='Unconditional',
                 ecolor='steelblue', marker='o', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
               ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                '20', '21', '22', '23', '24'], fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel("Phase", fontsize=25)
    plt.ylabel("$log$(Interaction {})".format(interactions), fontsize=25)

    legend = plt.legend(frameon=False, loc='upper right', title='Label', fontsize=20)
    legend.get_title().set_fontsize(fontsize=20)
    plt.subplots_adjust(left=0.06, bottom=0.11, right=0.98, top=0.97)
    if interactions == 'Frequency':
        plt.ylim([0, 2])
        plt.savefig('F_evolve.pdf', format='pdf')
    if interactions == 'Duration':
        plt.ylim([0, 7])
        plt.savefig('D_evolve.pdf', format='pdf')
    plt.show()


# Fig.~S8a&b
def LastingPhase(year):
    plt.figure(figsize=(7, 7))
    ax = plt.axes()
    length = 14
    Data = read('Results/Graph_Year{}_TR_Frequency.txt'.format(year))
    H = [[] for i in range(5)]
    for data in Data:
        if data.count('-1') == 0:
            if int(data[2]) < 100:
                interactions = list(map(int, map(float, data[length:])))
                if int(data[2]) >= 6:
                    tr = 6
                else:
                    tr = int(data[2])

                count = 0
                for i in range(len(interactions)):
                    if interactions[i] != 0:
                        count = i
                H[tr-2].append(count+1)
    X = [2, 3, 4, 5, 6]
    Y = []
    Err = []
    for i in range(5):
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#34495e", ls='-', label='$=2$',
                 ecolor='#34495e', marker='o', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)
    plt.xticks([2,3,4,5,6], ['2', '3' , '4', '5', '$\geq6$'], fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel('Tie Range in Phase 1', fontsize=25)
    plt.ylabel('Lifespan', fontsize=25)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.subplots_adjust(left=0.14, bottom=0.11, right=0.98, top=0.94)
    if year == 1:
        plt.title("12 Months (2015)", fontsize=25)
        plt.savefig('Plots/SI/Lifespan_2015.pdf', format='pdf')
    if year == 2:
        plt.title("12 Months (2016)", fontsize=25)
        plt.savefig('Plots/SI/Lifespan_2016.pdf', format='pdf')
    # plt.show()



# Fig.~S8c&d
def LastingPhase_Termination(year):
    plt.figure(figsize=(7, 7))
    ax = plt.axes()
    length = 14
    Data = read('Results/Graph_Year{}_TR_Frequency.txt'.format(year))
    H = [[] for i in range(5)]
    for data in Data:
        if data.count('-1') == 0:
            if int(data[2]) < 100:
                interactions = list(map(int, map(float, data[length:])))
                if int(data[2]) >= 6:
                    tr = 6
                else:
                    tr = int(data[2])
                lastingphase = -1
                flag = 1
                for i in interactions:
                    if i != 0:
                        if flag == 1:
                            lastingphase += 1
                    else:
                        flag = 0
                H[tr-2].append(lastingphase)
    X = [2, 3, 4, 5, 6]
    Y = []
    Err = []
    for i in range(5):
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#34495e", ls='-', label='$=2$',
                 ecolor='#34495e', marker='o', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)
    plt.xticks([2,3,4,5,6], ['2', '3' , '4', '5', '$\geq6$'], fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel('Tie Range in Phase 1', fontsize=25)
    plt.ylabel('Lifespan', fontsize=25)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.subplots_adjust(left=0.14, bottom=0.11, right=0.98, top=0.94)
    if year == 1:
        plt.title("12 Months (2015)", fontsize=25)
        plt.savefig('Plots/SI/Lifespan_2015_withTermination.pdf', format='pdf')
    if year == 2:
        plt.title("12 Months (2016)", fontsize=25)
        plt.savefig('Plots/SI/Lifespan_2016_withTermination.pdf', format='pdf')
    # plt.show()



# Fig.~S10
def TR_Degree():
    Data = read('Results/Graph_Season_TR_Duration.txt')
    G = nx.read_gexf('Graph/Season/Duration/G_Duration_Season_1.gexf')
    Deg = []
    for data in Data:
        if int(data[2])>=6 and int(data[2])<100:
            Deg.append(G.degree(data[0]))
            Deg.append(G.degree(data[1]))
    X = np.arange(1,30)
    Y = []
    for i in X:
        Y.append(Deg.count(i)/len(Deg))
    plt.figure(figsize=(7,7))
    ax = plt.axes()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.bar(X, Y)
    plt.xlim([0,30])
    plt.ylim([0,0.4])
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel('Degree',fontsize=25)
    plt.ylabel('$f$',fontsize=25)
    plt.subplots_adjust(left=0.18, bottom=0.11, right=0.95, top=0.97)
    plt.savefig('Plots/SI/TieRange_Degree.pdf', format='pdf')
    plt.show()

# def TR_Degree1():
#     Data = read('Results/Graph_Season_TR_Duration.txt')
#     G = nx.read_gexf('Graph/Season/Duration/G_Duration_Season_1.gexf')
#     Deg = []
#     Mass = {node:0 for node in G.nodes()}
#
#
#     for data in Data:
#         if int(data[2])>=6 and int(data[2])<100:
#             Mass[data[0]] += 1
#             Mass[data[1]] += 1
#             # Deg.append(G.degree(data[0]))
#             # Deg.append(G.degree(data[1]))
#
#     Probability = [[] for i in range(29)]
#     X = np.arange(2,31)
#     Y = []
#     Err = []
#     for node in G.nodes():
#         if G.degree(node) > 1 and G.degree(node) <= 30:
#             Probability[G.degree(node)-2].append(Mass[node]/G.degree(node)*100)
#     for i in range(29):
#         Y.append(np.mean(Probability[i]))
#         Err.append(mean_confidence_interval(Probability[i]))
#
#     plt.figure(figsize=(7,7))
#     ax = plt.axes()
#     ax.spines['top'].set_visible(False)
#     ax.spines['right'].set_visible(False)
#     plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#34495e", ls='-',
#                  ecolor='#34495e', marker='o', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)
#     plt.xlim([0,30])
#     plt.ylim([-1,5])
#     plt.xticks(fontsize=20)
#     plt.yticks(fontsize=20)
#     plt.xlabel('Degree',fontsize=25)
#     plt.ylabel('$f$(long-range ties) (%)',fontsize=25)
#     plt.subplots_adjust(left=0.13, bottom=0.11, right=0.95, top=0.97)
#     # plt.savefig('Plots/SI/TieRange_Degree.pdf', format='pdf')
#     plt.show()

# Fig.~S11
def DegreeunderControl(interactions):
    Data = read('Results/Graph_Season_TR_{}.txt'.format(interactions))
    avg2, avg3, avg4, avg5, avg6 = [], [], [], [], []
    GH = nx.read_gexf('Graph/Season/Frequency/G_Frequency_Season_1.gexf')
    Large = max(nx.connected_components(GH), key=len)
    for data in Data:
        if data.count('-1') == 0:
            if data[0] in Large and data[1] in Large:
                if GH.degree(data[0]) <= 5 or GH.degree(data[1]) <= 5:
                # if 5 < GH.degree(data[0]) <= 15 or 5 < GH.degree(data[1]) <= 15:
                # if GH.degree(data[0]) > 15 or GH.degree(data[1]) > 15:
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
    plt.ylim([0.5, 2.5])
    legend = plt.legend(frameon=False, loc='upper right', title='Tie Range in Phase 1', fontsize=20)
    legend.get_title().set_fontsize(fontsize=20)
    plt.title('$ND_{1}\leq5$', fontsize=30)
    # plt.title('$5<ND_{1}\leq15$', fontsize=30)
    # plt.title('$ND_{1}>15$', fontsize=30)
    plt.subplots_adjust(left=0.17, bottom=0.11, right=0.98, top=0.935)
    plt.savefig('Plots/SI/Mainresults_LowerDegree_{}.pdf'.format(interactions), format='pdf')
    plt.show()


# Fig.~S12(a&b)
def Analysis_Existing(interactions):
    Data = read('Results/oldedge/Graph_Season_TR_{}.txt'.format(interactions))
    avg2, avg3, avg4, avg5, avg6 = [], [], [], [], []
    GH = nx.read_gexf('Graph/Season/Frequency/G_Frequency_Season_1.gexf')
    Large = max(nx.connected_components(GH),key=len)
    for data in Data:
        if data.count('-1') == 0:
            if data[0] in Large and data[1] in Large:
                if data[2] == '2':
                    avg2.append(list(map(int, map(float, data[9:]))))
                if data[2] == '3':
                    avg3.append(list(map(int, map(float, data[9:]))))
                if data[2] == '4':
                    avg4.append(list(map(int, map(float, data[9:]))))
                if data[2] == '5':
                    avg5.append(list(map(int, map(float, data[9:]))))
                if int(data[2]) >= 6 and int(data[2]) < 100:
                    avg6.append(list(map(int, map(float, data[9:]))))
    fig = plt.figure(figsize=(7, 7))
    ax = plt.axes()
    X = [2, 3, 4, 5, 6, 7, 8]
    H = [[] for i in range(7)]
    Y = []
    Err = []
    for i in range(7):
        for j in range(len(avg2)):
            H[i].append(mt.log(avg2[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#34495e", ls='-', label='$=2$',
                 ecolor='#34495e', marker='^', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = [2, 3, 4, 5, 6, 7, 8]
    H = [[] for i in range(7)]
    Y = []
    Err = []
    for i in range(7):
        for j in range(len(avg3)):
            H[i].append(mt.log(avg3[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#2980b9", ls='-', label='$=3$',
                 ecolor='#2980b9', marker='s', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = [2, 3, 4, 5, 6, 7, 8]
    H = [[] for i in range(7)]
    Y = []
    Err = []
    for i in range(7):
        for j in range(len(avg4)):
            H[i].append(mt.log(avg4[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#7f8c8d", ls='-', label='$=4$',
                 ecolor='#7f8c8d', marker='p', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = [2, 3, 4, 5, 6, 7, 8]
    H = [[] for i in range(7)]
    Y = []
    Err = []
    for i in range(7):
        for j in range(len(avg5)):
            H[i].append(mt.log(avg5[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#c0392b", ls='-', label='$=5$',
                 ecolor='#c0392b', marker='H', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = [2, 3, 4, 5, 6, 7, 8]
    H = [[] for i in range(7)]
    Y = []
    Err = []
    for i in range(7):
        for j in range(len(avg6)):
            H[i].append(mt.log(avg6[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#8e44ad", ls='-', label='$\geq6$',
                 ecolor='#8e44ad', marker='8', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.xticks([2, 3, 4, 5, 6, 7, 8], ['2', '3', '4', '5', '6', '7', '8'], fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel("Phase", fontsize=25)
    plt.ylabel("$log$(Interaction {})".format(interactions), fontsize=25)
    legend = plt.legend(frameon=False, loc='upper right', title='Tie Range in Phase 2', fontsize=20)
    legend.get_title().set_fontsize(fontsize=20)
    plt.title('Existing Ties',fontsize=30)
    if interactions == 'Duration':
        plt.ylim([1, 8])
        plt.subplots_adjust(left=0.11, bottom=0.11, right=0.98, top=0.935)
        plt.savefig('Plots/SI/Mainresults_ExistingTies_D.pdf', format='pdf')
    if interactions == 'Frequency':
        plt.ylim([0.5, 3])
        plt.subplots_adjust(left=0.145, bottom=0.11, right=0.98, top=0.935)
        plt.savefig('Plots/SI/Mainresults_ExistingTies_F.pdf', format='pdf')
        plt.show()


# Fig.~S12(d&e)
def Analysis_Newlyformed(interactions):
    Data = read('Results/newedge/Graph_Season_TR_{}.txt'.format(interactions))
    avg2, avg3, avg4, avg5, avg6 = [], [], [], [], []
    GH = nx.read_gexf('Graph/Season/Frequency/G_Frequency_Season_1.gexf')
    Large = max(nx.connected_components(GH),key=len)
    for data in Data:
        if data.count('-1') == 0:
            if data[0] in Large and data[1] in Large:
                if data[2] == '2':
                    avg2.append(list(map(int, map(float, data[9:]))))
                if data[2] == '3':
                    avg3.append(list(map(int, map(float, data[9:]))))
                if data[2] == '4':
                    avg4.append(list(map(int, map(float, data[9:]))))
                if data[2] == '5':
                    avg5.append(list(map(int, map(float, data[9:]))))
                if int(data[2]) >= 6 and int(data[2]) < 100:
                    avg6.append(list(map(int, map(float, data[9:]))))

    fig = plt.figure(figsize=(7, 7))
    ax = plt.axes()
    X = [2, 3, 4, 5, 6, 7, 8]
    H = [[] for i in range(7)]
    Y = []
    Err = []
    for i in range(7):
        for j in range(len(avg2)):
            H[i].append(mt.log(avg2[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#34495e", ls='--', label='$=2$',
                 ecolor='#34495e', marker='^', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = [2, 3, 4, 5, 6, 7, 8]
    H = [[] for i in range(7)]
    Y = []
    Err = []
    for i in range(7):
        for j in range(len(avg3)):
            H[i].append(mt.log(avg3[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#2980b9", ls='--', label='$=3$',
                 ecolor='#2980b9', marker='s', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = [2, 3, 4, 5, 6, 7, 8]
    H = [[] for i in range(7)]
    Y = []
    Err = []
    for i in range(7):
        for j in range(len(avg4)):
            H[i].append(mt.log(avg4[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#7f8c8d", ls='--', label='$=4$',
                 ecolor='#7f8c8d', marker='p', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = [2, 3, 4, 5, 6, 7, 8]
    H = [[] for i in range(7)]
    Y = []
    Err = []
    for i in range(7):
        for j in range(len(avg5)):
            H[i].append(mt.log(avg5[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#c0392b", ls='--', label='$=5$',
                 ecolor='#c0392b', marker='H', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)

    X = [2, 3, 4, 5, 6, 7, 8]
    H = [[] for i in range(7)]
    Y = []
    Err = []
    for i in range(7):
        for j in range(len(avg6)):
            H[i].append(mt.log(avg6[j][i] + 1))
        Y.append(np.mean(H[i]))
        Err.append(mean_confidence_interval(H[i]))
    plt.errorbar(x=X, y=Y, yerr=Err, fmt="o", color="#8e44ad", ls='--', label='$\geq6$',
                 ecolor='#8e44ad', marker='8', markersize=10, linewidth=2, elinewidth=0.5, capsize=4)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.xticks([2, 3, 4, 5, 6, 7, 8], ['2', '3', '4', '5', '6', '7', '8'], fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel("Phase", fontsize=25)
    plt.ylabel("$log$(Interaction {})".format(interactions), fontsize=25)

    legend = plt.legend(frameon=False, loc='upper right', title='Tie Range in Phase 2', fontsize=20)
    legend.get_title().set_fontsize(fontsize=20)
    plt.title('Newly Formed Ties', fontsize=30)
    if interactions == 'Frequency':
        plt.ylim([0, 1.2])
        plt.subplots_adjust(left=0.145, bottom=0.11, right=0.98, top=0.935)
        plt.savefig('Plots/SI/Mainresults_NewTies_F.pdf', format='pdf')
    if interactions == 'Duration':
        plt.ylim([0, 5])
        plt.subplots_adjust(left=0.145, bottom=0.11, right=0.98, top=0.935)
        plt.savefig('Plots/SI/Mainresults_NewTies_D.pdf', format='pdf')
    # plt.show()


# Fig.~S12(c&f)
def Existing_Newlyformed_pp(choice):
    if choice == 1:
        Data = read('Results/oldedge/Graph_Season_TR_Frequency.txt')
    if choice == 2:
        Data = read('Results/newedge/Graph_Season_TR_Frequency.txt')
    avg2, avg3, avg4, avg5, avg6 = [], [], [], [], []
    GH = nx.read_gexf('Graph/Season/Frequency/G_Frequency_Season_1.gexf')
    Large = max(nx.connected_components(GH),key=len)
    for data in Data:
        if data.count('-1') == 0:
            if data[0] in Large and data[1] in Large:
                if data[2] == '2':
                    avg2.append(list(map(int, map(float, data[9:]))))
                if data[2] == '3':
                    avg3.append(list(map(int, map(float, data[9:]))))
                if data[2] == '4':
                    avg4.append(list(map(int, map(float, data[9:]))))
                if data[2] == '5':
                    avg5.append(list(map(int, map(float, data[9:]))))
                if int(data[2]) >= 6 and int(data[2]) < 100:
                    avg6.append(list(map(int, map(float, data[9:]))))
    H = []
    Count = [0 for _ in range(6)]
    for data in avg2:
        for _ in range(6):
            if data[_ + 1] == 0:
                Count[_] += 1
    for _ in range(6):
        H.append([1 - Count[_] / len(avg2), '$=2$', int(_ + 3)])

    Count = [0 for _ in range(6)]
    for data in avg3:
        for _ in range(6):
            if data[_ + 1] == 0:
                Count[_] += 1
    for _ in range(6):
        H.append([1 - Count[_] / len(avg3), '$=3$', int(_ + 3)])

    Count = [0 for _ in range(6)]
    for data in avg4:
        for _ in range(6):
            if data[_ + 1] == 0:
                Count[_] += 1
    for _ in range(6):
        H.append([1 - Count[_] / len(avg4), '$=4$', int(_ + 3)])

    Count = [0 for _ in range(6)]
    for data in avg5:
        for _ in range(6):
            if data[_ + 1] == 0:
                Count[_] += 1
    for _ in range(6):
        H.append([1 - Count[_] / len(avg5), '$=5$', int(_ + 3)])

    Count = [0 for _ in range(6)]
    for data in avg6:
        for _ in range(6):
            if data[_ + 1] == 0:
                Count[_] += 1
    for _ in range(6):
        H.append([1 - Count[_] / len(avg6), '$\geq6$', int(_ + 3)])

    H.append([1, '$=2$', 2])
    H.append([1, '$=3$', 2])
    H.append([1, '$=4$', 2])
    H.append([1, '$=5$', 2])
    H.append([1, '$\geq6$', 2])
    if choice == 1:
        fig = plt.figure(figsize=(7, 7))
        ax = plt.axes()
        X = [2, 3, 4, 5, 6, 7, 8]
        Y = [1, 0.736412550974173, 0.7031490711372904, 0.630629814227458, 0.592359537834164, 0.5328103760761214,
             0.5092659719075668]
        plt.plot(X, Y, color='#34495e', label='$=2$', marker='^', markersize=10, linewidth=2)
        Y = [1, 0.5344482512975338, 0.5021540757827606, 0.4311883035381119, 0.39811391159808673, 0.3356965975779368,
             0.3241968859187897]
        plt.plot(X, Y, color='#2980b9', label='$=3$', marker='s', markersize=10, linewidth=2)
        Y = [1, 0.5887842465753425, 0.5521404109589041, 0.48809931506849313, 0.4537671232876712, 0.39400684931506846,
             0.3813356164383561]
        plt.plot(X, Y, color='#7f8c8d', label='$=4$', marker='p', markersize=10, linewidth=2)
        Y = [1, 0.7099236641221374, 0.6863867684478371, 0.6361323155216285, 0.5909669211195929, 0.5597964376590331,
             0.5502544529262087]
        plt.plot(X, Y, color='#c0392b', label='$=5$', marker='H', markersize=10, linewidth=2)
        Y = [1, 0.7976190476190477, 0.7857142857142857, 0.7142857142857143, 0.7976190476190477, 0.7261904761904762,
             0.6547619047619048]
        plt.plot(X, Y, color='#8e44ad', label='$\geq6$', marker='8', markersize=10, linewidth=2)

        plt.xlabel('Phase', fontsize=25)
        plt.ylabel('Persistence Probability', fontsize=25)
        plt.xticks(fontsize=20)
        plt.yticks(fontsize=20)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        legend = plt.legend(frameon=False, loc='upper right', title='Tie Range in Phase 2', fontsize=20)
        legend.get_title().set_fontsize(fontsize=20)
        plt.ylim([0.3,1.3])
        plt.title('Existing Ties', fontsize=30)
        plt.subplots_adjust(left=0.145, bottom=0.11, right=0.98, top=0.935)
        plt.savefig('PersistenceProbability_ExistingTies.pdf', format='pdf')
        plt.show()
    if choice == 2:
        fig = plt.figure(figsize=(7, 7))
        ax = plt.axes()
        X =[2,3,4,5,6,7,8]
        Y = [1, 0.3032891687576915, 0.26103182086975973, 0.20548514440058174, 0.20976841566910132, 0.17565407789800058, 0.1657050616119804]
        plt.plot(X,Y,color='#34495e',label='$=2$',marker='^',markersize=10, linewidth=2, linestyle='--')
        Y = [1, 0.17113469925121372, 0.14338846375380565, 0.10812145149345842, 0.11179132724430185, 0.0883403274911545, 0.08396280753723362]
        plt.plot(X, Y, color='#2980b9', label='$=3$', marker='s', markersize=10, linewidth=2, linestyle='--')
        Y = [1, 0.1609676167478763, 0.1353111120693372, 0.10948212668707691, 0.11025828985382258, 0.08641283256435683, 0.08110905092492782]
        plt.plot(X, Y, color='#7f8c8d', label='$=4$', marker='p', markersize=10, linewidth=2, linestyle='--')
        Y = [1, 0.20102827763496145, 0.18046272493573268, 0.13521850899742927, 0.1460154241645244, 0.13573264781491, 0.12596401028277637]
        plt.plot(X, Y, color='#c0392b', label='$=5$', marker='H', markersize=10, linewidth=2, linestyle='--')
        Y = [1, 0.26415094339622647, 0.26415094339622647, 0.15094339622641506, 0.26415094339622647, 0.28301886792452835, 0.1132075471698113]
        plt.plot(X, Y, color='#8e44ad', label='$\geq6$', marker='8', markersize=10, linewidth=2, linestyle='--')

        plt.xlabel('Phase', fontsize=25)
        plt.ylabel('Persistence Probability', fontsize=25)
        plt.xticks(fontsize=20)
        plt.yticks(fontsize=20)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        legend = plt.legend(frameon=False, loc='upper right', title='Tie Range in Phase 2', fontsize=20)
        legend.get_title().set_fontsize(fontsize=20)
        plt.ylim([0, 1])
        plt.title('Newly Formed Ties', fontsize=30)
        plt.subplots_adjust(left=0.145, bottom=0.11, right=0.98, top=0.935)
        plt.savefig('Plots/SI/PersistenceProbability_NewTies.pdf', format='pdf')
        # plt.show()

