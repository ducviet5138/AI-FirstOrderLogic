own("Nono", "M1").
missile("M1").
american("West").
enemy("Nono", america).

criminal(X) :- 
    american(X),
    weapon(Y), 
    sell(X, Y, Z),
    hostile(Z).

sell("West", X, "Nono") :- 
    missile(X),
    own("Nono", X).

weapon(X) :- missile(X).

hostile(X) :- enemy(X, america).