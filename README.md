repo containing materials for minigames using sat solvers

The tentative plan is as follows 

Week 1: 

Reading up on propositional logic

1. Basic syntax and semantics
2. Satisfiability and Validity of Formulas
3. Normal Forms - CNF and DNF forms of formulas and complexity of checking satisfiability.
4. Encoding simple constraints as clauses

Week 2 -3:

1. Understanding DPLL algorithm 
2. Implementing a very basic DPLL based solver in python
3. Encoding sudoku into constraints and solving it using the SAT solver. ( Can try on your own but mostly will end up using Z3 python library)

Week 4

1. Encoding the Tsukoban game in clauses and using a SAT solver to find a solution for the same.

Resources

Note : There are a lot of given resources and some of them might seem very intimidating it is not necessary to study up all of these, simply use what seem most accesible and try to gain a solid understanding of the required parts.

1. Lecture slides on logic (CS 228 course)
Can skip lectures on proof systems completeness and soundness (Can be interesting side reading for those interested). Important thing is to understand week 1 requirements. 
refer to lectures 9 and 10 to understand what DPLL is

2. Huth and Ryan chapter 1 (Again can skip proof systems, completeness and soundness) (Important parts are propositional logic systems CNF and DNF)

3. Nice video explaining what SAT solvers are : https://www.youtube.com/watch?v=d76e4hV1iJY

4. Shawn Hedman Chapter 1 (Again can skip proof systems, completeness and soundness) (Important parts are propositional logic systems CNF and DNF)

5. Lectures 9 and 10 of CS 228 are essential for DPLL can also try referring to https://www.cs.ox.ac.uk/people/james.worrell/lecture06.pdf.

6. For DPLL can trying referring to first 3-4 lectures of : https://www.youtube.com/watch?v=qnEhZFH9gXw&list=PLbLuy9jaJwu07biHdKGHLmuCYClD-2iHj&index=1. The rest are not needed can watch if interested

7. A nice blog post on SAT solvers and SAT encoding https://rvprasad.medium.com/sat-encoding-an-introduction-44d23049ab2a 

You are free to look up and study other online resources if you find anything helpful, but the above are more than sufficient to finish the project.

(I made a small mistake as a result of which you can technically access week 3 week 4 materials early. )
