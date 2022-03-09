import seaborn as sns
import matplotlib.pyplot as plt

class cn_matrix:
    def show(self,data):
        ax = sns.heatmap(data, annot=True, cmap='Blues')
        ax.set_title('Seaborn Confusion Matrix with labels\n\n')
        ax.set_xlabel('\nPredicted Values')
        ax.set_ylabel('Actual Values ')
        ax.xaxis.set_ticklabels(['False','True'])
        ax.yaxis.set_ticklabels(['False','True'])
        plt.show()