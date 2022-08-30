from sklearn.neighbors._classification import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

class SuggestAudiobook:
    
    accuracy = 0
    precision = 0
    recall = 0

    MaeTest = 0
    MaeTrain = 0


    def __init__(self, insertedbook):
                
        #model = DecisionTreeClassifier()

        model = KNeighborsClassifier()

        book = pd.read_csv("dataset.csv", delimiter = ";")

        var2 = book.Title

        var1 = book[["audioRuntime_converted", "category_converted"]]

        var2 = var2.astype('string')
        var1 = var1.astype('int')

        model.fit(var1, var2)

        dataframe = pd.DataFrame(data = {"audioRuntime_converted": [insertedbook.audioRuntime_converted], 
                                         "category_converted": [insertedbook.category_converted]})

        predictionDataframe = model.predict(dataframe)

        print("L'audiobook consigliato per te e' --> ", predictionDataframe)


            