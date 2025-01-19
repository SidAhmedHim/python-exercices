unique_words= set()
while True:
   
  sensitive=input("would u like the programme to be case sensitive? 1 for yes 0 for no: ")
  if sensitive in ["1","0"]:
     break
  else:
     print("enter the right value 1 or 0")
     
while True:      
      word=input("enter a word: ").strip() #eliminate the spaces in the edges

      list_word=word.split()
      if len(list_word)==1:      #verifying the input confirm if its a word
          if sensitive=="1":        
            if word in unique_words:  #verifiying duplicate 
              print(f"You typed in {len(unique_words)} unique words and {len(unique_words)+1} Total words.")
              break
          else:
             if word.lower() in [words.lower() for words in unique_words]: #verifiying duplicate
               print(f"You typed in {len(unique_words)} unique words and {len(unique_words)+1} Total words.")
               break
          unique_words.add(word)  #adding the unique new word   
      else:
         print("you entered a phrase enter a word")
  
         
print(sorted(unique_words,reverse=False))       #sorting alphabeticaly 
try:
        with open("unique_words.txt", "w") as file:  #saving the set to a file named unique_words.txt
            for word in unique_words:
                file.write(word + "\n") 
        print(f"Unique words saved to unique_words.txt as: {unique_words}.")
except Exception as e:
        print(f"An error occurred while saving: {e}")




