% Arithmetic Logic
calculate(add, A, B, R) :- R is A + B.
calculate(sub, A, B, R) :- R is A - B.
calculate(mul, A, B, R) :- R is A * B.
calculate(div, A, B, R) :- B \= 0, R is A / B.
calculate(div, _, 0, 'Error: Division by zero').
calculate(mod, A, B, R) :- B \= 0, R is A mod B. % Added Modulo Logic
calculate(mod, _, 0, 'Error: Modulo by zero').
main :-
    write('--- CALCULATOR ---'), nl,
    write('1. Addition'), nl,
    write('2. Subtraction'), nl,
    write('3. Multiplication'), nl,
    write('4. Division'), nl,
    write('5. Modulo'), nl,
    write('6. Exit'), nl,
    write('Choose an option (1-6): '),
    read(Choice),
    process(Choice).
process(1) :-
    write('1st number: '), read(A),
    write('2nd number: '), read(B),
    calculate(add, A, B, R),
    write('Res = '), write(R), nl, main.
process(2) :-
    write('1st number: '), read(A),
    write('2nd number: '), read(B),
    calculate(sub, A, B, R),
    write('Res = '), write(R), nl, main.
process(3) :-
    write('1st number: '), read(A),
    write('2nd number: '), read(B),
    calculate(mul, A, B, R),
    write('Res = '), write(R), nl, main.
process(4) :-
    write('1st number: '), read(A),
    write('2nd number: '), read(B),
    calculate(div, A, B, R),
    write('Res = '), write(R), nl, main.
process(5) :-
    write('1st number: '), read(A),
    write('2nd number: '), read(B),
    calculate(mod, A, B, R),
    write('Res = '), write(R), nl, main.
process(6) :-
    write('Exit!'), nl, !.
process(_) :-
    write('Invalid choice,enter again.'), nl,
    main.
