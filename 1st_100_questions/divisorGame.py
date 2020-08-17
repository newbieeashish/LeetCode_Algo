'''
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn,
 that player makes a move consisting of:

Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.
Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play 
optimally.


Example 1:

Input: 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.
Example 2:

Input: 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves
'''

def DivisorGame(N):
    return N%2 ==0 

print(DivisorGame(2))

'''Proof:  If Alice starts with an even number she will always win.

If Alice has an even number, she can always subtract 1, giving Bob an odd number. 
 numbers are not divisible by 2. They are only divisible by odd numbers. 
Hence Bob must subtract an odd number. Since odd minus odd is even, 
Bob will always return an even number to Alice. Alice will thus get a 
smaller even number after each round of play and Bob will get a smaller 
odd number after each round of play. Eventually Bob will have to play the 
number 1 and will lose the game since he will have no options.'''