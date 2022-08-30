import pytholog as pl

class Interrogation:
          def interrogation(cls):

                    kb = pl.KnowledgeBase("book")
                    kb.from_file("myKb.pl")

                    choice = -1

                    while (choice != '5'):

                              print("|----------------------------------------------------------|")
                              print("|----- 1) Trova la durata dell'audiolibro                  |")
                              print("|----- 2) Trova la categoria dell'audiolibro               |")
                              print("|----- 3) Trova audiolibro di una durata specifica         |")
                              print("|----- 4) Trova audiolibro di una categoria specifica      |")
                              print("|----- 5) Ritorna al menu' principale                      |")
                              print("|----------------------------------------------------------|")

                              choice = input("Indica l'operazione da effettuare --> ")

                              if(choice == '1'):
                                        audiobookname = str(input("Indica il nome dell' audiolibro --> ")).lower()
                                        print(kb.query(pl.Expr("audioruntime("+audiobookname+",D"))[0])
                              
                              if(choice == '2'):
                                        audiobookname = str(input("Indica il nome dell'audiolibro --> ")).lower()
                                        print(kb.query(pl.Expr("book("+audiobookname+",T)"))[0])
                             


                              if(choice == '3'):
                                        audioruntime = str(input("Indica durata dell'audiolibro -->")).lower()
                                        booklist = list(kb.query(pl.Expr("audioruntime(F,"+audioruntime+")")))
                                        for book in booklist:
                                                  print(book)

                              if(choice == '4'):
                                        category = str(input("Indica il genere dell'audiolibro --> ")).lower()
                                        booklist = list(kb.query(pl.Expr("book(F,"+category+")")))
                                        for book in booklist:
                                                  print(book)
                              