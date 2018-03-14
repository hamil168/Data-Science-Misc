"""

helper_fxns.py

by Benjamin Hamilton

------------------------------------------

A few helper functions that were aggregated from activities I found myself repeating.

Included are 

- graphing feature importance (created for CatBoost but should work
	with relevant sklearn models

- mass scoring that generates a number of categorical scores, as well as
	confusion matrices (it needs a loss. Perhaps add one later)
	for CV and Holdout data

"""


# Import the usual suspects
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Scorers of various sorts
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, classification_report
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import make_scorer


def feature_imp(model,X,text=True,head=10,graph=True,title='Feature Importance',fgsz=(12,12)):
    """ Generate a graph with feature importances, given a fit model 'model', for a dataset X

    model: a model that has been fit that has a feature_importances_ method
    X: a dataset, typically as a dataframe
    text  = True: prints out the feature importances
    head = 10: the number of lines of feature importances to print out
    graph = True: print graph
    title = 'Feature Importance': title of the graph
    fgsz = (12,12): size of the graph. 12,12 is great for examining but 6,6 may be better if you have 
    many models in a single notebook.
    """
    # Feature Importances 
    A = pd.DataFrame(model.feature_importances_)
    
    # Feature Names
    Xc = pd.DataFrame(X.columns)

	# Create a data set Mat that has all the feature importance values 
	# concatenated to each respective feature name
    Mat = pd.concat([Xc,A],axis=1)

	#Rename columns
    Mat.columns=['features','importance']
    if text == True:
        print(Mat.sort_values('importance',ascending=False).head(head))

	# Seaborn Barplot graph
    if graph==True:
        sns.set_style('darkgrid')
        plt.figure(figsize=fgsz)

        ax = sns.barplot(x='features',y='importance',data=Mat)
        ax.set_xticklabels(ax.get_xticklabels(),rotation = 90)
        plt.title(title)
        plt.show()


# Mass Scoring Function
def mass_scoring(y,y_pred,title='Train'):
    """
    Input classification truth and predictions (not probabilities)
    Returns a list with precision, recall, f1, and support for both micro and weighted averages

    Prints f1/acc, f1(wt), and confusion matrix
    title='Train': Title of the data, such as 'CV', 'Holdout'

    The precision,recall,fscore,support are all delivered returned list X_scores
    To extract measures that use micro average:
    X_scores[0] is precision, X_scores[1] is recall, X_scores[2] is f1, X_scores[3] is support\

    Tp extract measures that use weighted average:
    X_scores[4] is precision, X_scores[5] is recall, X_scores[6] is f1, X_scores[7] is support
    """



	# precision, recall, f1 and support function from sklearn
    prfs_mic = precision_recall_fscore_support(y,y_pred,average='micro')
    prfs_wt = precision_recall_fscore_support(y,y_pred,average='weighted')
    
	# Individual components of each
    f1mic = prfs_mic[2]
    f1wt = prfs_wt[2]
    rmic = prfs_mic[1]
    rwt = prfs_wt[1]
    pmic = prfs_mic[0]
    pwt = prfs_wt[0]
    smic = prfs_mic[3]
    swt = prfs_wt[3]
    
    conf_mat = confusion_matrix(y,y_pred)
    
	# Print the f1/acc, f1(wt) and confusion matrix
    print('\n'+title+' Data: ')
    print('f1(micro)/acc: '+str(f1mic)+', f1(wt): '+str(f1wt))    
    print('Confusion Matrix (' + title +'):')
    print(pd.DataFrame(conf_mat))
      
	# create a list of all scores and return them
    X_scores = [prfs_mic,prfs_wt]
    
    return X_scores