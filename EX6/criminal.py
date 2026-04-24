========criminal===================
% FACTS
american(west).
enemy(nono, america).
owns(nono, m1).
missile(m1).

% RULES
criminal(X) :-
    american(X),
    weapon(Y),
    sells(X, Y, Z),
    hostile(Z).

sells(west, X, nono) :-
    missile(X),
    owns(nono, X).

weapon(X) :-
    missile(X).

hostile(X) :-
    enemy(X, america).
