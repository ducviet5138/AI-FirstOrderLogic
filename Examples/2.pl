# slide
parent("Tom", "John").
parent("Tom", "Fred").
male("Tom").

father(Parent, Child) :-
    parent(Parent, Child),
    male(Parent).

sibling(Person1, Person2) :-
    parent(Parent, Person1),
    parent(Parent, Person2),
    Person1 \= Person2.