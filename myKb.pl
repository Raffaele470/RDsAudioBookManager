:- discontiguous(i_book/3).

%-----------------------------------------------------------------------------
%Regole Book

%Mostra durata libro in base a titolo
audioruntime(Book,AudioRuntime) :- i_book(Book,_,AudioRuntime).

%Mostra nome categoria in base a titolo 
book(Title, I_book1) :- i_book(Title,I_book1,_).


%-----------------------------------------------------------------------------

%DATI

%Immissione book

i_book(travels_with_charley_in_search_of_america,travel_and_tourism,07.58).
i_book(the_100,teen,07.17).
i_book(anarchy,romance,09.58).
i_book(profound_good,religion_and_spirituality,04.25).
i_book(evicted,politics_and_social_sciences,11.03).
i_book(100_baggers,money_and_finance,06.19).
i_book(brushfire,literature_and_fiction,19.18).
i_book(alone,lgbtq+,09.52).
i_book(meth_head_syndrome,home_and_garden,0.01).
i_book(heroes,history,15.01).
i_book(beyond_order,health_and_wellness,13.11).
i_book(self_discipline,education_and_learning,0.16).
i_book(the_hobbit,childrens_audiobooks,11.05).
i_book(winning,business_and_careers,06.44).
i_book(becoming,biographies_and_memoirs,19.03).
i_book(broken_horses,arts_and_entertainment,10.03).
i_book(igen,computers_and_technology,09.52).
i_book(cosmic_journey,science_and_engineering,0.10).
i_book(bloodline,science_fiction_and_fantasy,11.12).


%-----------------------------------------------------------------------------