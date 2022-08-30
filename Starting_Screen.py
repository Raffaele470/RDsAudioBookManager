#Schermata iniziale  che mi permetterà di visualizzare un menu' in cui avro' la possibilita' di selezionare le varie opzioni.

import sys
from Book import Book
from PricePrevision import PricePrevision
from SuggestAudiobook import SuggestAudiobook
from prolog import Interrogation

if __name__ == '__main__':

          book = Book()         
          choice = 0          

          price = PricePrevision()     
          interrogation = Interrogation()

          while choice != 4:

                    print("|----------------------------------------------------------|")
                    print("|                      RD-AudibleManager                   |")
                    print("|----------------------------------------------------------|")
                    print("| Digita il numero corrispondente per effettuare la scelta |")
                    print("|                                                          |")
                    print("| ----- 1) Previsione prezzo                               |") 
                    print("| ----- 2) Suggerisci Audiolibro                           |")
                    print("| ----- 3) Accuratezza                                     |")
                    print("| ----- 4) Interrogazioni sugli Audiolibri                 |")
                    print("| ----- 5) Exit                                            |")
                    print("|                                                          |")
                    print("|----------------------------------------------------------|")

                    while choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5':
                              choice = input("Inserisci un'operazione valida --> ")

                    if choice == '1':
                              book.InsertInformationBook()
                              price.PricePrevision(book)

                    if choice == '2':
                              book.audiobookAcquisitionToRecommend()
                              ReccomendedAudiobook = SuggestAudiobook(book)

                    if choice == '3':
                              price.StatsPredictions(price.precision, price.recall, price.MaeTest, price.MaeTrain,price.accuracy)  
                    
                    if choice == '4':
                              interrogation.interrogation()

                    if choice == '5':
                              print("Chiusura in corso...")
                              sys.exit()
                    choice = 0
                    book.resetValue() #resetto i valori 
pass