""" Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test" """

# My Solution 
def spin_words(sentence):
    words = sentence.split()
    string = ""
    iterator = 0;
    for i in words:
      if(len(i)>4):
        for j in i:
          string = j + string
        words[iterator] = string
        string = ""
        print(words[iterator])
        iterator+=1
      else:
        iterator+=1  
    return " ".join(words)

# Solution 1
function spinWords(words){
  return words.split(' ').map(function (word) {
    return (word.length > 4) ? word.split('').reverse().join('') : word;
  }).join(' ');
}

# Solution 2
function spinWords(string){
  return string.replace(/\w{5,}/g, function(w) { return w.split('').reverse().join('') })
}

# Solution 3 
function spinWords(str){
  return str.split(' ').map( w => w.length<5 ? w : w.split('').reverse().join('') ).join(' ');
}

# Solution 4
function spinWords(str){
  return str.split(' ').map(spinSingleWord).join(' ');
}

function spinSingleWord(word){
  return word.length>4 ? word.split('').reverse().join('') : word;
}