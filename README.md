# MarkovChainTextGeneration
Text generation using Markov Chains.
This little project was made for university Information Theory course.<br>
I was doing it with my colleague Kacper Kuźnik (https://github.com/KacperKuznik)
___

Algorithm needs a text corpus in normalized form, (only english lowercase letters a-z , spaces ' ' and digits 0-9)<br>
It reads the entire text and creates a probability tree. Each node has a value, which indicates probability that this specific letter appears after previous letters (ancestors). <br><br>
Algorithm also needs order, which indicates how many letters we consider before choosing next letter.<br>
With all this information algorithm generates text of given length using conditional probabilities of letters. The higher order the text should look more like the original text corpus.
___
### Brief explanation
Order: 1 (we consider one previous letter when choosing to generate another one)<br>
Text corpus: "abac"<br>
Simplified tree:<br>
<pre>
  a(2/4)      b(1/4)      c(1/4)
  /     \        |
b(1/2) c(1/2)  a(1)
</pre>
<br>
If we want to generate first letter then we use probabilities from first level of the tree</br>
Let's say that 'a' was chosen, then we look at the children of node a on the first level and we choose another letter with these probabilities.<br>
Let's say now we have generated text 'ac', node 'c' doesn't have any children so we choose letter with probabilities from first level.<br><br>
<b>Disclaimer</b>
This is a big simplification, with bigger order it works the same way, but it is difficult to describe.
