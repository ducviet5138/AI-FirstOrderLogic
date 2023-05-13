male("Hagoromo").
male("Indra").
male("Asura").
male("Tajima").
male("Madara").
male("Izuna").
male("Fugaku").
male("Itachi").
male("Sasuke").
male("Minato").
male("Naruto").
male("Boruto").

female("Ozawa").
female("Outdra").
female("Bsura").
female("Tanara").
female("Mikoto").
female("Sakura").
female("Sarada").
female("Kushina").
female("Hinata").
female("Himawari").


parent("Hagoromo", "Indra").
parent("Hagoromo", "Asura").
parent("Ozawa", "Indra").
parent("Ozawa", "Asura").
parent("Indra", "Tajima").
parent("Indra", "Fugaku").
parent("Outdra", "Tajima").
parent("Outdra", "Fugaku").
parent("Tajima", "Madara").
parent("Tajima", "Izuna").
parent("Tanara", "Madara").
parent("Tanara", "Izuna").
parent("Fugaku", "Itachi").
parent("Fugaku", "Sasuke").
parent("Mikoto", "Itachi").
parent("Mikoto", "Sasuke").
parent("Sasuke", "Sarada").
parent("Sakura", "Sarada").
parent("Asura", "Kushina").
parent("Bsura", "Kushina").
parent("Kushina", "Naruto").
parent("Minato", "Naruto").
parent("Naruto", "Boruto").
parent("Naruto", "Himawari").
parent("Hinata", "Boruto").
parent("Hinata", "Himawari").


married("Hagoromo", "Ozawa").
married("Ozawa", "Hagoromo").
married("Indra", "Outdra").
married("Outdra", "Indra").
married("Tajima", "Tanara").
married("Tanara", "Tajima").
married("Fugaku", "Mikoto").
married("Mikoto", "Fugaku").
married("Sasuke", "Sakura").
married("Sakura", "Sasuke").
married("Naruto", "Hinata").
married("Hinata", "Naruto").
married("Minato", "Kushina").
married("Kushina", "Minato").
married("Asura", "Bsura").
married("Bsura", "Asura").

hokage("Naruto").
hokage("Minato").

husband(Person, Wife) :-
    male(Person),
    female(Wife),
    married(Person, Wife).

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