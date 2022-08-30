import pandas as pd
#from sklearn.neighbors._classification import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
import scikitplot as sklpt





class PricePrevision:

          accuracy = 0
          precision = 0
          recall = 0

          MaeTest = 0
          MaeTrain = 0



          #model = KNeighborsClassifier()

          model = DecisionTreeClassifier() #migliore

          
          book = pd.read_csv("dataset.csv", delimiter=";")
          

          def __init__(self):

                    var1 = self.book[["audioRuntime_converted", "average_rating_converted","ratings_count_converted"]]
                    var2 = self.book.price

                    var1 = var1.astype('int')
                    var2 = var2.astype('int')

                    var1Train, var1Test, var2Train, var2Test  = train_test_split(var1, var2, test_size=0.2, random_state=1)

                    self.model.fit(var1Train, var2Train)


                    #K fold cross validation

                    k = 100
                    kFold = KFold(n_splits = k, random_state = None) 
                    crossValidationResult = cross_val_score(self.model, var1, var2, cv=kFold, n_jobs=-1)
                    
                    self.accuracy = crossValidationResult


                    # precision recall

                    precisionTest = self.model.predict(var1Test)
                    precisionTrain = self.model.predict(var1Train)

                    self.calc_precision_recall(var2Test, precisionTest)
                    
                    # mae

                    mae_train = mean_absolute_error(var2Train,precisionTrain)
                    mae_test = mean_absolute_error(var2Test,precisionTest)

                    self.testMae = mae_test
                    self.trainMae = mae_train

          @classmethod
          def PricePrevision(cls, book):         # previsione del prezzo del libro. Inserisco all'interno di un dataframe (tabella bidimensionale i valori convertiti precedentemente per poi fare la previsione del prezzo)
                    dataframe = pd.DataFrame(data={"audioRuntime_converted":[book.audioRuntime_converted], 
                                                   "average_rating_converted":[book.average_rating_converted],
                                                   "ratings_count_converted":[book.ratings_count_converted]})


                    prevision_var2 = cls.model.predict(dataframe)

                    print("Il prezzo previsto per l'audiolibro e' pari a --> ", int(prevision_var2), "euro")


          @classmethod
          def calc_precision_recall(cls, y_true, y_pred):

                    y_pred = pd.Series(y_pred, index=y_true.index)

                    truePositive = 0
                    falsePositive = 0
                    falseNegative = 0

                    for i in y_true.index:
                              if y_true[i] == y_pred[i]:    #verifico se predizione andata bene
                                        truePositive += 1
                              if y_true[i] != y_pred[i]:
                                        falsePositive += 1  #verifico se predizione andata male
                              if y_pred[i] == "" and y_true[i] != y_pred[i]:
                                        falseNegative += 1  #verifico se predizione andata male

                    try:
                              precision = truePositive / (truePositive + falsePositive)
                    except:
                              precision = 1

                    try:
                              recall = truePositive / (truePositive + falseNegative)
                    except:
                              recall = 1

                    sklpt.metrics.plot_confusion_matrix(y_true, y_pred)
                    plt.show()
                    cls.precision = precision
                    cls.recall = recall


          @classmethod
          def StatsPredictions(cls, precision, recall, MaeTest, MaeTrain, accuracy):
                    
                    print("----| STATISTICHE PREVISIONI |-----")
                    print("----> Precision : ",precision)
                    print("----> Recall : ", recall)
                    print(f"----> Accuratezza : {format(accuracy.mean())}")
                    print('----> MAE - train set :', MaeTest)
                    print('----> MAE - test set :', MaeTrain)

