import os
path = r"E:\text folder"
os.chdir(path)



class Solution:
  def read_text_file(self,file_path):
    
    with open(file_path, 'r') as f:
      words = f.read().split()
    self.findAllConcatenatedWordsInADict(words)
    



  def findAllConcatenatedWordsInADict(self, words):
    s1 = []
    words_dict = set(words)
    for word in words:
      words_dict.remove(word)
      if self.check(word, words_dict) is True:
        s1.append(word)
      words_dict.add(word)
    s1 = sorted(s1, key=lambda u: (-len(u), u))
    print("Longest Compound Word :" , s1[0])
    print("Second Longest Compound Word :" ,s1[1])
    
  def check(self, word, d):
    if word in d:
      return True
    for i in range(len(word),0, -1):
      if word[:i] in d and self.check(word[i:], d):
        return True
    return False


s = Solution()


for file in os.listdir():

	if file.endswith(".txt"):
		file_path = f"{path}\{file}"

		
		s.read_text_file(file_path)
   
