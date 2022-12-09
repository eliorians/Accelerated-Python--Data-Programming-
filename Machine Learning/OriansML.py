
#Classifications
#https://cprosenjit.medium.com/10-classification-methods-from-scikit-learn-we-should-know-40c03ab8b077

#Implement Pipeline & GridSearchCV
#https://scikit-learn.org/stable/tutorial/statistical_inference/putting_together.html

import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

from sklearn.decomposition import PCA #reduces the mean, use for strongly correlated data to get rid of outliers
from sklearn.preprocessing import StandardScaler #reduces to between 0-1, useful for negative values

#classifiers
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.neural_network import MLPClassifier 


def main(): 

    #? TODO use one or more Pipelines and GridSearchCV to select hyperparameters.
    #TODO write notes in .txt

    loader(1)
    loader(2)
    loader(3) 
    loader(4)
    loader(5)
    loader(6)
    loader(7)
    loader(8)
    loader(9)
    loader(10)
    loader(11)
    loader(12)

def loader(problem):
    problem_name = f'challenge_{problem:02d}' 

    #load and show training data
    train_file = f'{problem_name}.npz'
    data = np.load(train_file)
    x_train = data['x_train']
    y_train = data['y_train']
    x_test = data['x_test']

    plt.clf()
    plt.scatter(x_train[y_train==0, 0], x_train[y_train==0, 1], label=r'$y=0$', color='blue', marker='*')
    plt.scatter(x_train[y_train==1, 0], x_train[y_train==1, 1], label=r'$y=1$', color='red', marker='+')

    plt.xlabel(r'$x_1$')
    plt.ylabel(r'$x_2$')
    plt.title(f'Data set {problem} train')
    plt.legend()
    plt.axis('equal')
    plt.show()

    #choose model based on problem

    if problem == 1:
        #model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .91
        #model= LogisticRegression(random_state=0)      #accuracy = .86
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .92
        model= GaussianNB()                             #accuracy = .94
        #model= DecisionTreeClassifier()                #accuracy = .80
        #model= RandomForestClassifier()                #accuracy = .89
        #model= AdaBoostClassifier()                    #accuracy = .89
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .94
        #model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .93

    elif problem == 2:
        model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .90 w 5, 3 =.88 6=.88
        #model= LogisticRegression(random_state=0)       #accuracy = .86
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .85
        #model= GaussianNB()                            #accuracy = .88
        #model= DecisionTreeClassifier()                #accuracy = .85
        #model= RandomForestClassifier()                #accuracy = .87
        #model= AdaBoostClassifier()                    #accuracy = .82
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .90
        #model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .88

    elif problem == 3:
        #model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .88
        #model= LogisticRegression(random_state=0)      #accuracy = .88
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .83
        #model= GaussianNB()                            #accuracy = .76
        #model= DecisionTreeClassifier()                 #accuracy = .83
        #model= RandomForestClassifier()                #accuracy = .84
        #model= AdaBoostClassifier()                    #accuracy = .84
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .86
        #model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .89

        pipe= Pipeline(steps= [("pca", PCA()), ("classifier", LogisticRegression(random_state=0))])
        model= GridSearchCV(pipe, param_grid={})    #accuracy = .88

    elif problem == 4:
        #model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .82
        model= LogisticRegression(random_state=0)      #accuracy = .84
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .83
        #model= GaussianNB()                            #accuracy = .83
        #model= DecisionTreeClassifier()                #accuracy = .77
        #model= RandomForestClassifier()                #accuracy = .82
        #model= AdaBoostClassifier()                    #accuracy = .78
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .83
        #model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .83

        # pipe= Pipeline(steps= [("ss", StandardScaler()), ("classifier", SVC(random_state=0, kernel='rbf'))])
        # model= GridSearchCV(pipe, param_grid={}) accuracy= .84

    elif problem == 5:
        model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .89
        #model= LogisticRegression(random_state=0)      #accuracy = .86
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .85
        #model= GaussianNB()                            #accuracy = .82
        #model= DecisionTreeClassifier()                #accuracy = .84
        #model= RandomForestClassifier()                #accuracy = .84
        #model= AdaBoostClassifier()                    #accuracy = .85
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .86
        #model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .85

        #pipe= Pipeline(steps= [("pca", PCA()), ("classifier", SVC(random_state=0, kernel='rbf'))])
        #model= GridSearchCV(pipe, param_grid={}) #.85

    elif problem == 6:
        #model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .99
        #model= LogisticRegression(random_state=0)      #accuracy = .60
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .77
        #model= GaussianNB()                            #accuracy = .59
        model= DecisionTreeClassifier()                #accuracy = 1.0
        #model= RandomForestClassifier()                #accuracy = 1.0
        #model= AdaBoostClassifier()                    #accuracy = .99
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .63
        #model= MLPClassifier(alpha=1, max_iter=2000)   #accuracy = .97

    elif problem == 7:
        model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .68, pca=.68, ss= .68, both= .68
        #model= LogisticRegression(random_state=0)      #accuracy = .40, .4, .4
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .52, .52, .54
        #model= GaussianNB()                            #accuracy = .5, .43
        #model= DecisionTreeClassifier()                #accuracy = .65, .56
        #model= RandomForestClassifier()                #accuracy = .67, .55
        #model= AdaBoostClassifier()                    #accuracy = .61, .5
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .48, .48
        #model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .50, .6, .5

        # pipe= Pipeline(steps= [("scaler", StandardScaler()), ("pca", PCA()), 
        #     ("classifier", KNeighborsClassifier(n_neighbors=5))])
        # model= GridSearchCV(pipe, param_grid={})

    elif problem == 8:
        #model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .94
        #model= LogisticRegression(random_state=0)      #accuracy = .89
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .95
        #model= GaussianNB()                            #accuracy = .87
        model= DecisionTreeClassifier()                #accuracy = 1.0
        #model= RandomForestClassifier()                #accuracy = .99
        #model= AdaBoostClassifier()                    #accuracy = 1.0
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .89
        #model= MLPClassifier(alpha=1, max_iter=2000)   #accuracy = .96

    elif problem == 9:
        model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .99
        #model= LogisticRegression(random_state=0)      #accuracy = .90
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .97
        #model= GaussianNB()                            #accuracy = .93
        #model= DecisionTreeClassifier()                #accuracy = .95
        #model= RandomForestClassifier()                #accuracy = .96
        #model= AdaBoostClassifier()                    #accuracy = .95
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .92
        #model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .97

    elif problem == 10:
        #model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .90
        model= LogisticRegression(random_state=0)      #accuracy = .90
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .83
        #model= GaussianNB()                            #accuracy = .76
        #model= DecisionTreeClassifier()                #accuracy = .85
        #model= RandomForestClassifier()                #accuracy = .88
        #model= AdaBoostClassifier()                    #accuracy = .87
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .90
        #model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .90

    elif problem == 11:
        #model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .90
        #model= LogisticRegression(random_state=0)      #accuracy = .91
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .87
        #model= GaussianNB()                            #accuracy = .68
        #model= DecisionTreeClassifier()                #accuracy = .87
        #model= RandomForestClassifier()                #accuracy = .90
        #model= AdaBoostClassifier()                    #accuracy = .89
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .88
        model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .92

    elif problem == 12:
        model= KNeighborsClassifier(n_neighbors=3)     #accuracy = .90 at 3, .89 at 2 and .87 at 4
        #model= LogisticRegression(random_state=0)      #accuracy = .44
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .87
        #model= GaussianNB()                            #accuracy = .49
        #model= DecisionTreeClassifier()                #accuracy = .88
        #model= RandomForestClassifier()                #accuracy = .9
        #model= AdaBoostClassifier()                    #accuracy = .80
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .47
        #model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .47

    else:
        print("Failed to find problem " + problem)
        quit()



    #split data (ONLY USED FOR TESTING ACCURACY)
    #x_train, x_valid, y_train, y_valid = train_test_split(x_train, y_train, random_state=1)

    #fit & predict the data
    model.fit(x_train, y_train)

    #y_hat = model.predict(x_valid) #for testing accuracy
    y_hat = model.predict(x_test)   #for submission files

    #plot new data 
    # plt.clf()
    # plt.scatter(x_valid[y_hat==0, 0], x_valid[y_hat==0, 1], label=r'$y=0$', color='blue', marker='*')
    # plt.scatter(x_valid[y_hat==1, 0], x_valid[y_hat==1, 1], label=r'$y=1$', color='red', marker='+')
    # plt.legend()
    # plt.show()

    #save submission
    submission_file = f'{problem_name}_submission.npz'
    np.savez(submission_file, y_test=y_hat)
    
    #output accuracy score (ONLY USED FOR TESTING ACCURACY)
    #print("Problem " + str(problem))
    #print(model)
    #print(model.score(x_valid, y_valid))
    #print("\n")
    

if __name__ == '__main__':
    main()