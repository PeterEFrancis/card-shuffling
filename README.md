# card-shuffling


Deck with $n$ cards.

**Random-to-Random Shuffle**:
 1. Remove a card u.a.r. from the deck
 1. Insert it u.a.r.

One shuffle acts on the deck by one of the following elements of $S_n$:
$$S=\{(1)\}\cup\{(a\ a+1)\ :\ a\in [n-1]\}\cup\{(a\ a+1\ \cdots b)^\pm\ :\ a, b\in [n], |a-b| > 1\} \subset S_n.$$

Note: $|S|=1+(n-1)+2n(n-3)$ ?

For any $x\in S_n$, and $s\in S$, $\mathbb{P}(x, xs)=\begin{cases}\frac{1}{n} & s=(1)\\ \frac{2}{n^2} & s= (a\ a+1)\\ \frac{1}{n^2}&s=(a\ a+1\ \cdots\ b)\end{cases}$
<!-- 
**Modified Random-to-Random Shuffle**
 1. Remove a card u.a.r. from the deck
 1. Insert it u.a.r. *among all positions, excluding the one below it or the top position if the bottom card is selected*
 
For any $x\in S_n$, $\mathbb{P}(x, xs)=\begin{cases}\frac{1}{n} & s=(1)\\ \frac{1-\frac{1}{n}}{|S|-1} & s\in S\setminus\{(1)\}\end{cases}$
 -->
**Goal**

Let $T$ be the first time that all cards have been picked ($T\geq n$).

We want to compute $\mathbb{P}(X_t=\sigma\mid T\leq t)$ for all $\sigma\in S_n$ and $t$.
