male("Prince Phillip").
male("Prince Charles").
male("Captain Mark Phillips").
male("Timothy Laurence").
male("Prince Andrew").
male("Prince Edward").
male("Prince William").
male("Prince Harry").
male("Peter Phillips").
male("Mike Tindall").
male("Prince George").
male("James, Viscount Severn").


female("Queen Elizabeth II").
female("Princess Diana").
female("Camilla Parker Bowles").
female("Princess Anne").
female("Sarah Ferguson").
female("SophieRhys-jones").
female("Kate Middletion").
female("Autumn Kelly").
female("Zara Phillips").
female("Princess Beatrice").
female("Princess Eugenie").
female("Princess Charlotte").
female("Savannah Phillips").
female("Isla Phillips").
female("Lady Louise Mountbatten Windsor").
female("Mia Grace Tindall").


married("Prince Phillip", "Queen Elizabeth II").
married("Prince Charles", "Camilla Parker Bowles").
married("Princess Anne", "Timothy Laurence").
married("Prince Edward", "SophieRhys-jones").
married("Prince William", "Kate Middletion").
married("Autumn Kelly", "Peter Phillips").
married("Zara Phillips", "Mike Tindall").


parent("Queen Elizabeth II", "Prince Charles").
parent("Queen Elizabeth II", "Princess Anne").
parent("Queen Elizabeth II", "Prince Andrew").
parent("Queen Elizabeth II", "Prince Edward").
parent("Prince Phillip", "Prince Charles").
parent("Prince Phillip", "Princess Anne").
parent("Prince Phillip", "Prince Andrew").
parent("Prince Phillip", "Prince Edward").
parent("Prince Charles", "Prince William").
parent("Prince Charles", "Prince Harry").
parent("Princess Diana", "Prince William").
parent("Princess Diana", "Prince Harry").
parent("Captain Mark Phillips", "Peter Phillips").
parent("Captain Mark Phillips", "Zara Phillips").
parent("Princess Anne", "Peter Phillips").
parent("Princess Anne", "Zara Phillips").
parent("Prince Andrew", "Princess Beatrice").
parent("Prince Andrew", "Princess Eugenie").
parent("Sarah Ferguson", "Princess Beatrice").
parent("Sarah Ferguson", "Princess Eugenie").
parent("Prince Edward", "Lady Louise Mountbatten Windsor").
parent("Prince Edward", "James, Viscount Severn").
parent("SophieRhys-jones", "Lady Louise Mountbatten Windsor").
parent("SophieRhys-jones", "James, Viscount Severn").
parent("Prince William", "Prince George").
parent("Prince William", "Princess Charlotte").
parent("Kate Middletion", "Prince George").
parent("Kate Middletion", "Princess Charlotte").
parent("Autumn Kelly", "Savannah Phillips").
parent("Autumn Kelly", "Isla Phillips").
parent("Peter Phillips", "Savannah Phillips").
parent("Peter Phillips", "Isla Phillips").
parent("Zara Phillips", "Mia Grace Tindall").
parent("Mike Tindall", "Mia Grace Tindall").

disvorced("Princess Diana", "Prince Charles").
disvorced("Captain Mark Phillips", "Princess Anne").
disvorced("Sarah Ferguson", "Prince Andrew").

husband(Person, Wife) :-
    male(Person),
    female(Wife),
    married(Person, Wife); married(Wife, Person).

wife(Person, Husband) :-
    husband(Husband, Person).

father(Parent, Child) :-
    parent(Parent, Child),
    male(Parent).

mother(Parent, Child) :-
    parent(Parent, Child),
    female(Parent).

child(Child, Parent) :-
    parent(Parent, Child).

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

grandchild(GC, GP) :-
    grandparent(GP, GC).

grandson(GS, GP) :-
    grandchild(GS, GP),
    male(GS).

granddaughter(GD, GP) :-
    grandchild(GD, GP),
    female(GD).