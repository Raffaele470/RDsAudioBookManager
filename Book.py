class Book:
            #inizializzo i valori
          category = ""
          average_rating = -1
          audioRuntime = 0
          ratings_count = -1

          audioRuntime_converted = 0
          average_rating_converted = 0
          ratings_count_converted = 0
          category_converted = 0


          @classmethod
          def InsertInformationBook(cls):


                    while (cls.audioRuntime <= 0.01 or cls.audioRuntime >= 23.59):
                              cls.audioRuntime = float(input("Inserisci la durata in ore dell'audiolibro (per esempio: 1 equivale a 1 ora, 0.12 a 12 minuti, 0.02 a 2 minuto ) --> "))

                    while (cls.average_rating <= 1 or cls.average_rating > 5):
                              cls.average_rating = int(input("Inserisci il rating dell'audiolibro (numero da 1 a 5) --> "))

                    while (cls.ratings_count <= 1 or cls.ratings_count > 242323):
                              cls.ratings_count = int(input("Inserisci il numero di recensioni (numero da 1 a 242323)--> "))
                              
                
                    if cls.audioRuntime <= 0.30:    #30 minuti
                              cls.audioRuntime_converted = 1
                    elif cls.audioRuntime <= 4:   #4 ore 
                              cls.audioRuntime_converted = 2
                    elif cls.audioRuntime <= 15:  #15 ore
                              cls.audioRuntime_converted = 3
                    else:    #meno di 15 ore
                              cls.audioRuntime_converted = 4

                          
                    if cls.average_rating >= 5: #voto medio
                              cls.average_rating_converted  = 5
                    elif cls.average_rating >=4:
                              cls.average_rating_converted  = 4
                    elif cls.average_rating >=3:
                              cls.average_rating_converted  = 3
                    elif cls.average_rating >=2:
                              cls.average_rating_converted  = 2
                    else:    
                              cls.average_rating_converted  = 1
                    
                    
                    if (cls.ratings_count >= 20000):    #numero di voti
                              cls.ratings_count_converted = 5
                    elif cls.ratings_count > 5000:
                              cls.ratings_count_converted = 4
                    elif cls.ratings_count > 1000:
                              cls.ratings_count_converted = 3
                    elif cls.ratings_count > 100:
                              cls.ratings_count_converted = 2
                    else:
                              cls.ratings_count_converted= 1
                    

                           
          @classmethod
          def audiobookAcquisitionToRecommend(cls):    #viene richiamata per acquisire dati in input per poter consigliare un audiobook
            print("|------------------ CATEGORIA AUDIOLIBRO ------------------|")
            print("|----- 1) Arts & Entertainment                             |") 
            print("|----- 2) Biographies & Memoirs                            |")
            print("|----- 3) Business & Careers                               |")
            print("|----- 4) Children's Audiobooks                            |")
            print("|----- 5) Computers & Technology                           |")
            print("|----- 6) Education & Learning                             |")
            print("|----- 7) Erotica                                          |")
            print("|----- 8) Health & Wellness                                |")
            print("|----- 9) History                                          |")
            print("|----- 10) Home & Garden                                   |")
            print("|----- 11) LGBTQ+                                          |")
            print("|----- 12) Literature & Fiction                            |")
            print("|----- 13) Money & Finance                                 |")
            print("|----- 14) Mystery, Thriller & Suspense                    |")
            print("|----- 15) Politics & Social Sciences                      |")
            print("|----- 16) Relationships, Parenting & Personal Development |")
            print("|----- 17) Religion & Spirituality                         |")
            print("|----- 18) Romance                                         |")
            print("|----- 19) Science & Engineering                           |")
            print("|----- 20) Science Fiction & Fantasy                       |")
            print("|----- 21) Teen                                            |")
            print("|----- 22) Travel & Tourism                                |")
            print("|----------------------------------------------------------|")

            while(cls.category_converted <= 0 or cls.category_converted >= 23):
                cls.category_converted = int(input("Indica la categoria dell'audiolibro che preferisci --> "))

      
            while cls.audioRuntime_converted < 1 or cls.audioRuntime_converted > 4:
                print("----- 1) fino 30 minuti")
                print("----- 2) fino a 4 ore")
                print("----- 3) fino a 15 ore")
                print("----- 4) fino a 24 ore")
                cls.audioRuntime_converted = int(input("Indica la durata che vuoi che abbia l'audiolibro --> "))
     

          @classmethod
          def resetValue(cls):          # mi serve affinche' i valori si resettino dopo che faccio la previsione altrimenti viene restituito sempre lo stesso valore
                    cls.category = ""
                    cls.average_rating = -1
                    cls.audioRuntime = 0
                    cls.ratings_count = -1

                    cls.audioRuntime_converted = 0
                    cls.average_rating_converted = 0
                    cls.ratings_count_converted = 0
                    cls.category_converted = 0
