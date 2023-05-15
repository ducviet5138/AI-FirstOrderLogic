buffalo("Bob").
pig("Pat").
slug("Steve").

faster(B, P) :-
    buffalo(B),
    pig(P).
faster(P, S) :-
    pig(P),
    slug(S).
faster(B, S) :-
    faster(B, P),
    faster(P, S).