
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

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
        #model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .505
        #model= LogisticRegression(random_state=0)      #accuracy = .49
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .5
        model= GaussianNB()                             #accuracy = .52
        #model= DecisionTreeClassifier()                #accuracy = .52
        #model= RandomForestClassifier()                #accuracy = .52
        #model= AdaBoostClassifier()                    #accuracy = .52
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .52
        #model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .515

    elif problem == 2:
        #model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .505
        model= LogisticRegression(random_state=0)       #accuracy = .52
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .5025
        #model= GaussianNB()                            #accuracy = .4925
        #model= DecisionTreeClassifier()                #accuracy = .5
        #model= RandomForestClassifier()                #accuracy = .505
        #model= AdaBoostClassifier()                    #accuracy = .5025
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .505
        #model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .505

    elif problem == 3:
        #model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .525
        #model= LogisticRegression(random_state=0)      #accuracy = .4925
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .4975 rbf / .49 linear
        #model= GaussianNB()                            #accuracy = .505 visual split
        model= DecisionTreeClassifier()                 #accuracy = .51
        #model= RandomForestClassifier()                #accuracy = .5
        #model= AdaBoostClassifier()                    #accuracy = .5025
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .4925
        #model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .4925

    elif problem == 4:
        #model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .4825
        #model= LogisticRegression(random_state=0)      #accuracy = .4975
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .5025
        #model= GaussianNB()                            #accuracy = .505
        #model= DecisionTreeClassifier()                #accuracy = .5
        #model= RandomForestClassifier()                #accuracy = .495
        model= AdaBoostClassifier()                     #accuracy = .51
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .5
        #model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .505

    elif problem == 5:
        #model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .5225
        #model= LogisticRegression(random_state=0)      #accuracy = .5125
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .5225
        #model= GaussianNB()                            #accuracy = .52
        #model= DecisionTreeClassifier()                #accuracy = .5
        #model= RandomForestClassifier()                #accuracy = .515
        model= AdaBoostClassifier()                    #accuracy = .5375
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .5125
        #model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .515


    elif problem == 6:
        #model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .515
        #model= LogisticRegression(random_state=0)      #accuracy = .485
        model= SVC(random_state=0, kernel='rbf')       #accuracy = .5325
        #model= GaussianNB()                            #accuracy = .4875
        #model= DecisionTreeClassifier()                #accuracy = .5125
        #model= RandomForestClassifier()                #accuracy = .5125
        #model= AdaBoostClassifier()                    #accuracy = .52
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .4875
        #model= MLPClassifier(alpha=1, max_iter=2000)   #accuracy = .52

    elif problem == 7:
        #model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .525
        #model= LogisticRegression(random_state=0)      #accuracy = .4625
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .4875
        #model= GaussianNB()                            #accuracy = .4925
        model= DecisionTreeClassifier()                #accuracy = .5275
        #model= RandomForestClassifier()                #accuracy = .525
        #model= AdaBoostClassifier()                    #accuracy = .525
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .465
        #model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .515

    elif problem == 8:
        #model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .4925
        model= LogisticRegression(random_state=0)      #accuracy = .505
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .48
        #model= GaussianNB()                            #accuracy = .5025
        #model= DecisionTreeClassifier()                #accuracy = .49
        #model= RandomForestClassifier()                #accuracy = .4875
        #model= AdaBoostClassifier()                    #accuracy = .49
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .495
        #model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .4975

    elif problem == 9:
        #model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .515
        model= LogisticRegression(random_state=0)      #accuracy = .5575
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .5175
        #model= GaussianNB()                            #accuracy = .53
        #model= DecisionTreeClassifier()                #accuracy = .5125
        #model= RandomForestClassifier()                #accuracy = .5125
        #model= AdaBoostClassifier()                    #accuracy = .52
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .545
        #model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .525

    elif problem == 10:
        #model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .5075
        #model= LogisticRegression(random_state=0)      #accuracy = .5025
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .5075
        #model= GaussianNB()                            #accuracy = .495
        #model= DecisionTreeClassifier()                #accuracy = .51
        #model= RandomForestClassifier()                #accuracy = .5125
        model= AdaBoostClassifier()                    #accuracy = .5125
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .5075
        #model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .5025

    elif problem == 11:
        #model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .51
        #model= LogisticRegression(random_state=0)      #accuracy = .5125
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .4875
        model= GaussianNB()                            #accuracy = .5225
        #model= DecisionTreeClassifier()                #accuracy = .5225
        #model= RandomForestClassifier()                #accuracy = .5125
        #model= AdaBoostClassifier()                    #accuracy = .5075
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .5025
        #model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .51

    elif problem == 12:
        #model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .51
        #model= LogisticRegression(random_state=0)      #accuracy = .515
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .52
        #model= GaussianNB()                            #accuracy = .4875
        #model= DecisionTreeClassifier()                #accuracy = .5125
        model= RandomForestClassifier()                #accuracy = .5375
        #model= AdaBoostClassifier()                    #accuracy = .5275
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .47
        #model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .4725

    else:
        print("Error: Select Problem 1-12")
        quit()
        
    #save submission
    model.fit(x_train, y_train)
    y_hat = model.predict(x_test)
    submission_file = f'{problem_name}_submission.npz'
    np.savez(submission_file, y_test=y_hat)

    #testing
    plt.clf()
    plt.scatter(x_test[y_hat==0, 0], x_train[y_hat==0, 1], label=r'$y=0$', color='blue', marker='*')
    plt.scatter(x_test[y_hat==1, 0], x_train[y_hat==1, 1], label=r'$y=1$', color='red', marker='+')
    plt.legend()
    plt.show()

    print("Problem " + str(problem))
    print(model)
    print(accuracy_score(y_train, y_hat)) #https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html
    print("\n")

if __name__ == '__main__':
    main()