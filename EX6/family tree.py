==========FAMILY TREE=================
% --- Facts (Corrected for all children of John/Mary) ---
male(john). male(bob). male(jim). male(tom). male(steve).
male(fred). male(scott). male(jack). male(rich). male(mike). male(harry).

female(patty). female(mary). female(carol). female(alice). female(linda).
female(valerie). female(barbara). female(donna). female(rachel).
female(jane). female(cindy).

% Parents
father(john, tom). father(john, linda). father(john, carol). father(john, jim).
father(bob, jim).
father(tom, valerie). father(tom, barbara).
father(steve, jack). father(steve, rich).
father(fred, jane).
father(scott, cindy).
father(jack, mike).
father(rich, harry).

mother(mary, tom). mother(mary, linda). mother(mary, carol). mother(mary, jim).
mother(alice, valerie). mother(alice, barbara).
mother(linda, jack). mother(linda, rich).
mother(valerie, jane).
mother(barbara, cindy).
mother(donna, mike).
mother(rachel, harry).

% --- Rules ---
parent(X, Y) :- father(X, Y).
parent(X, Y) :- mother(X, Y).

% Use a helper to ensure X and Y are different to avoid instantiation errors
sibling(X, Y) :- father(Z, X), father(Z, Y), X \= Y.

brother(X, Y) :- male(X), sibling(X, Y).
sister(X, Y) :- female(X), sibling(X, Y).

grandfather(X, Z) :- male(X), parent(X, Y), parent(Y, Z).
grandmother(X, Z) :- female(X), parent(X, Y), parent(Y, Z).

grandchild(X, Z) :- parent(Z, Y), parent(Y, X).
grandson(X, Z) :- male(X), grandchild(X, Z).
granddaughter(X, Z) :- female(X), grandchild(X, Z).

uncle(X, Y) :- male(X), sibling(X, Z), parent(Z, Y).
aunt(X, Y) :- female(X), sibling(X, Z), parent(Z, Y).

cousin(X, Y) :- parent(A, X), parent(B, Y), sibling(A, B).
% Answer for Query 5: General relation check
related(X, Y, grandfather) :- grandfather(X, Y).
related(X, Y, grandmother) :- grandmother(X, Y).
related(X, Y, grandchild) :- grandchild(X, Y).
related(X, Y, parent) :- parent(X, Y).
related(X, Y, sibling) :- sibling(X, Y).
