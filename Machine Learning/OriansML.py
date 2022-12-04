
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
    #loader(1)
    #loader(2)
    loader(3)


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
        print(problem)
        #model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .505
        #model= LogisticRegression(random_state=0)      #accuracy = .49
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .5
        model= GaussianNB()                            #accuracy = .52
        #model= DecisionTreeClassifier(criterion= 'entropy', random_state=0) #accuracy = .52
        #model= RandomForestClassifier()                #accuracy = .52
        #model= AdaBoostClassifier()                    #accuracy = .52
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .52
        #model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .515

    if problem == 2:
        print(problem)
        #model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .505
        model= LogisticRegression(random_state=0)      #accuracy = .52
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .5025
        #model= GaussianNB()                            #accuracy = .4925
        #model= DecisionTreeClassifier(criterion= 'entropy', random_state=0) #accuracy = .5
        #model= RandomForestClassifier()                #accuracy = .505
        #model= AdaBoostClassifier()                    #accuracy = .5025
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .505
        #model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .505

    if problem == 3:
        print(problem)
        #model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .
        #model= LogisticRegression(random_state=0)      #accuracy = .
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .
        #model= GaussianNB()                            #accuracy = .
        #model= DecisionTreeClassifier(criterion= 'entropy', random_state=0) #accuracy = .
        #model= RandomForestClassifier()                #accuracy = .
        #model= AdaBoostClassifier()                    #accuracy = .
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .
        #model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .

    if problem == 4:
        print(problem)
        #model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .
        #model= LogisticRegression(random_state=0)      #accuracy = .
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .
        #model= GaussianNB()                            #accuracy = .
        #model= DecisionTreeClassifier(criterion= 'entropy', random_state=0) #accuracy = .
        #model= RandomForestClassifier()                #accuracy = .
        #model= AdaBoostClassifier()                    #accuracy = .
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .
        #model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .

    if problem == 5:
        print(problem)
        #model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .
        #model= LogisticRegression(random_state=0)      #accuracy = .
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .
        #model= GaussianNB()                            #accuracy = .
        #model= DecisionTreeClassifier(criterion= 'entropy', random_state=0) #accuracy = .
        #model= RandomForestClassifier()                #accuracy = .
        #model= AdaBoostClassifier()                    #accuracy = .
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .
        #model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .
        
    if problem == 6:
        print(problem)
        #model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .
        #model= LogisticRegression(random_state=0)      #accuracy = .
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .
        #model= GaussianNB()                            #accuracy = .
        #model= DecisionTreeClassifier(criterion= 'entropy', random_state=0) #accuracy = .
        #model= RandomForestClassifier()                #accuracy = .
        #model= AdaBoostClassifier()                    #accuracy = .
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .
        #model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .

    if problem == 7:
        print(problem)
        #model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .
        #model= LogisticRegression(random_state=0)      #accuracy = .
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .
        #model= GaussianNB()                            #accuracy = .
        #model= DecisionTreeClassifier(criterion= 'entropy', random_state=0) #accuracy = .
        #model= RandomForestClassifier()                #accuracy = .
        #model= AdaBoostClassifier()                    #accuracy = .
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .
        #model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .

    if problem == 8:
        print(problem)
        #model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .
        #model= LogisticRegression(random_state=0)      #accuracy = .
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .
        #model= GaussianNB()                            #accuracy = .
        #model= DecisionTreeClassifier(criterion= 'entropy', random_state=0) #accuracy = .
        #model= RandomForestClassifier()                #accuracy = .
        #model= AdaBoostClassifier()                    #accuracy = .
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .
        #model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .

    if problem == 9:
        print(problem)
        #model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .
        #model= LogisticRegression(random_state=0)      #accuracy = .
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .
        #model= GaussianNB()                            #accuracy = .
        #model= DecisionTreeClassifier(criterion= 'entropy', random_state=0) #accuracy = .
        #model= RandomForestClassifier()                #accuracy = .
        #model= AdaBoostClassifier()                    #accuracy = .
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .
        #model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .

    if problem == 10:
        print(problem)
        #model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .
        #model= LogisticRegression(random_state=0)      #accuracy = .
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .
        #model= GaussianNB()                            #accuracy = .
        #model= DecisionTreeClassifier(criterion= 'entropy', random_state=0) #accuracy = .
        #model= RandomForestClassifier()                #accuracy = .
        #model= AdaBoostClassifier()                    #accuracy = .
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .
        #model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .

    if problem == 11:
        print(problem)
        #model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .
        #model= LogisticRegression(random_state=0)      #accuracy = .
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .
        #model= GaussianNB()                            #accuracy = .
        #model= DecisionTreeClassifier(criterion= 'entropy', random_state=0) #accuracy = .
        #model= RandomForestClassifier()                #accuracy = .
        #model= AdaBoostClassifier()                    #accuracy = .
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .
        #model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .

    if problem == 12:
        print(problem)
        #model= KNeighborsClassifier(n_neighbors=5)     #accuracy = .
        #model= LogisticRegression(random_state=0)      #accuracy = .
        #model= SVC(random_state=0, kernel='rbf')       #accuracy = .
        #model= GaussianNB()                            #accuracy = .
        #model= DecisionTreeClassifier(criterion= 'entropy', random_state=0) #accuracy = .
        #model= RandomForestClassifier()                #accuracy = .
        #model= AdaBoostClassifier()                    #accuracy = .
        #model= QuadraticDiscriminantAnalysis()         #accuracy = .
        #model= MLPClassifier(alpha=1, max_iter=1000)   #accuracy = .

    else:
        print("Error: Select Problem 1-12")
        quit()
        
    #save model
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
    print(accuracy_score(y_train, y_hat))

main()