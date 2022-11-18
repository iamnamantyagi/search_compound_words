In this problem we have to find the maximum number of compounded words in a word with maximum length.
Firstly we use the os module to read both the text files from the folder.
Here i use the recursive approach where we use two functions
first function

def findAllConcatenatedWordsInADict(self, words)
function to append those words with maximum composition.

second function

(def check(self, word, d))
for checking whether the word is present in the input file or not.

Through the first function we call the second function and in the second function self.check(word[i:],d) recursively calls the check function
and breaks the word to check the presence in the input file.
Lastly i have print the output in lexicographical order and with max length.
