import glob, os
from itertools import product
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings(action="ignore")
import numpy as np
RobustRandomCutForest = 0
Robust_covariance = 1
One_Class_SVM = 3
Isolation_Forest = 4

y_test = 1
Y_pred  = [RobustRandomCutForest,
           Robust_covariance,
           One_Class_SVM,
           Isolation_Forest]
axeis =[]
plot_nums = 1
for name in Y_pred:
    TP =(name == 1) & (y_test == 1)
    TN = (name == -1) & (y_test == -1)
    FP = (name == 1) & (y_test == -1)
    FN = (name == -1) & (y_test == 1)
    # TP = sum(TP)
    # TN = sum(TN)
    # FP = sum(FP)
    # FN = sum(FN)
    #
    # con = ([[TP / (TP + FP), FP / (TP + FP)],
    #         [FN / (TN + FN), TN / (TN + FN)]])
    #
    # ACC = (TP + TN) / (TP + TN + FP + FN)
    # SCE = TN / (TN + FP)
    # PRE = TP / (TP + FP)
    # F1 = 2 * TP / (2 * TP + FP + FN)
    #
    # accuracy = np.trace(con) / np.sum(con)
    # misclass = 1 - accuracy
    #
    # #   plt.title(name)
    # ax = fig.add_subplot(1, len(Y_pred), plot_nums)
    # plt.subplots_adjust(left=0.0, bottom=0.0, right=2.8, top=0.9, wspace=0.5, hspace=0.5)
    # plt.ylabel('True label')
    # sns.heatmap(con, annot=True, cmap='Blues', linewidths=0.2)
    # ax.set_xlabel(name)
    plot_nums += 1
    # print(ACC,
    #       SCE,
    #       PRE)
plt.show()