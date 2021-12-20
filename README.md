# codes and data for "Investigating and Modeling the Dynamics of Long Ties"

Preprint: https://arxiv.org/abs/2109.10523

Contact: Yuan Yuan, Purdue University, yuanyuan@purdue.edu


## Overview

The replication codes and data are provided, including analysis, plot, and modeling.
We store all figures in the main text and SI in the Plots folder.

For all necessary data for the emprical analysis, we store them in the Results folder.


## Dependencies and programming language

Python 3 (including packages: csv, time, math, numpy, scipy, pandas, networkx, torch)

## Code

Graph.py is based on NetworkX for network construction. 
We generate snapshots at the interval of a semi-year, a season, a month, a week, and a day, respectively.
Each snapshot is a weighted network aggregated from all phone calls in a fixed time window.
The weight of edges is denoted by the sum of interaction duration (call volumes in seconds) or frequency.

Statistics.py is the file for statistics on some analytic indices (weight, degree) and tie range in each snapshot.

Results.py presents all empirical analyses in our work, which calculate the intermediate results based on snapshots.

Manuscript_plots.py is the file for the figures in the main text.
SI_plots.py is the file for the figures in SI.

Model.py is the implementation of our proposed model based on PyTorch. 

You can run the code in the following way:

        model_run(delta, dimension)

* delta: the hyper-parameter to balance the direct effect and the indirect effect

* dimension: the dimension of endowment vectors

We also compare our model and two baselines: baseline1.py is a classic connections model [1]; baseline2.py is the simplified version of our model by removing the indirect effect.

[1]Jackson, M. O., & Wolinsky, A. (1996). A strategic model of social and economic networks. Journal of economic theory, 71(1), 44-74.https://www.sciencedirect.com/science/article/abs/pii/S0022053196901088

## Data

We employ a nationwide phone call dataset from Jan. 2015 to Dec. 2016.
The *log* interaction duration and *log* interaction frequency in each phase (intermediate results) are both provided. Currently we upload the Results folder to Google Drive.
(https://drive.google.com/drive/folders/1h4rHZvzzQO7niYMelbzToJZernOij1dv?usp=sharing)

Please download the files from the google drive for replication purposes.

In each file, we list tie ranges and interactions in all phases. 
For example, in "Results/Graph_season_TR_Duration.txt", the former eight columns are tie range and the latter eight columns are *log* interaction duration.
Tie range is calculated by the length of the second shortest path of two nodes. 
'-1' means that one node of this connection have no interaction with others in this phase.
'100' means that there is no second path between two nodes, indicating that the tie range is infinite.
'101' means that the degree of one node is 1, indicating that the tie range is infinite.  

Differential privacy is applied to protect the privacy of users. 
Concretely, we add a Gaussian noise with &mu;=0, &sigma;=5 to *log* interactions.
When reproducing the results, please remove all *numpy.log* in the codes, and minus a &sigma; for the calculation of error bars.

## Citation

You are welcome to reuse our code or data, but please cite us:

    @article{lyu2021investigating,
      title={Investigating and Modeling the Dynamics of Long Ties},
      author={Lyu, Ding and Yuan, Yuan and Wang, Lin and Wang, Xiaofan and Pentland, Alex},
      journal={arXiv preprint arXiv:2109.10523},
      year={2021}
    }