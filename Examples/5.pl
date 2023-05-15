male("Jay").
male("Manny").
male("Phil").
male("Luke").
male("Mitchell").
male("Cameron").

female("Gloria").
female("Claire").
female("Haley").
female("Alex").
female("Lily").

married("Jay", "Gloria").
married("Gloria", "Jay").
married("Phil", "Claire").
married("Claire", "Phil").
married("Mitchell", "Cameron").
married("Cameron", "Mitchell").

parent("Jay", "Claire").
parent("Jay", "Mitchell").
parent("Jay", "Manny").
parent("Gloria", "Claire").
parent("Gloria", "Mitchell").
parent("Gloria", "Manny").
parent("Phil", "Haley").
parent("Phil", "Alex").
parent("Phil", "Luke").
parent("Claire", "Haley").
parent("Claire", "Alex").
parent("Claire", "Luke").
parent("Mitchell", "Lily").
parent("Cameron", "Lily").


husband(Person, Wife) :- 
    male(Person),
    female(Wife),
    married(Person, Wife).

wife(Person, Husband) :- husband(Husband, Person).

gay(Person1, Person2) :-
    male(Person1),
    male(Person2),
    married(Person1, Person2).

father(Parent, Child) :- 
    parent(Parent, Child),
    male(Parent).

mother(Parent, Child) :-
    parent(Parent, Child),
    female(Parent).

child(Child, Parent) :- parent(Parent, Child).

son(Child, Parent) :- 
    child(Child, Parent), 
    male(Child).

daughter(Child, Parent) :- 
    child(Child, Parent), 
    female(Child).

grandparent(GP, GC) :- 
    parent(GP, Parent), 
    parent(Parent, GC).

grandmother(GM, GC) :- 
    grandparent(GM, GC), 
    female(GM).

grandfather(GF, GC) :- 
    grandparent(GF, GC), 
    male(GF).

grandchild(GC, GP) :- grandparent(GP, GC).

grandson(GS, GP) :- 
    grandchild(GS, GP),
    male(GS).

granddaughter(GD, GP) :- 
    grandchild(GD, GP), 
    female(GD).

sibling(Person1, Person2) :- 
    parent(Parent, Person1), 
    parent(Parent, Person2), 
    Person1 \= Person2.

brother(Person, Sibling) :- 
    sibling(Person, Sibling), 
    male(Person).

sister(Person, Sibling) :- 
    sibling(Person, Sibling), 
    female(Person).

aunt(Person, NieceNephew) :- 
    sister(Person, Parent), 
    parent(Parent, NieceNephew).

uncle(Person, NieceNephew) :- 
    brother(Person, Parent), 
    parent(Parent, NieceNephew).

niece(Person, AuntUncle) :- 
    female(Person), 
    parent(Parent, Person), 
    sibling(Parent, AuntUncle).

nephew(Person, AuntUncle) :- 
    male(Person), 
    parent(Parent, Person), 
    sibling(Parent, AuntUncle).