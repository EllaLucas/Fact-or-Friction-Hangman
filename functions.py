"""A collection of the functions that exist to execute my project's code."""

#Will be used to grab random fact from list.
import random 

#List of 21 obscure facts. List serves as database that program will import from. 
facts = ['space smells like a combination of diesel fuel and barbecue', 'cornell university scientists have created a functioning guitar the size of a human blood cell', 'many oranges are green when they’re ripe', 'The average person walks the equivalent of five laps around the world', 'women constitute seventy percent of Iranian university science and engineering students', 'globally only two percent of the population has green eyes', 'nothing rhymes with woman', 'honey is a better cough suppressant than over-the-counter cough suppressants', 'sarcasm makes you more creative', 'people are more likely to agree with a statement written in baskerville than any other font', 'talking to yourself makes your brain work more efficiently', 'due to a genetic defect cats cant taste sweet things', 'a single elephant tooth can weigh up to nine lbs', 'odontophobia is the fear of teeth', 'the most common name in the world is Mohammed', 'when you die your hair still grows for a couple of months', 'the neanderthals brain was bigger than yours', 'elephants are the only mammals that cant jump', 'american car horns beep in the tone of f', 'a lions roar can be heard from five miles away', 'every human spent about half an hour as a single cell']

#Variable designating how many total attempts user has to guess correctly.
lives_remaining = 5 

#guessed_letters will be filled in to display and update user's progress.
guessed_letters = ' ' 

def grab_fact(): 
    """Selects a fact from list of facts at random. 
    
    Returns
    -------
    facts[fact_position] : indexed list
        The result provides a print out of a random fact from list.  
    """
    
    #Variable returns a random integer to represent a position in facts. 
    fact_position = random.randint(0, len(facts) - 1)
    
    #Takes that integer and indexes it to facts, giving a random fact to play!
    return facts[fact_position]

def play_hangman():
    """Function that enables gameplay."""
    
    fact = grab_fact()
    
    #Loop instructs program how to handle guesses that lead to the game's conclusion.
    while True: 
        
        guess = get_guess(fact)
        
        #Instructs program how to communicate victory to user!
        if process_guess(guess, fact):
            print('You got it! Enjoy the knowledge.')
            print('The fact is: ' + fact)
            break 
        
        #Instructs program how to communicate failure to user when lives expire.
        if lives_remaining == 0: 
            print('Game over!')
            print('The fact was: ' + fact) 
            break 

def get_guess(fact):
    """Informs user progress throughout gameplay by updating fact, remaining lives.
    
    Parameters
    ----------
    fact : string 
        Randomly selected fact from list of facts. 
        
    Returns
    -------
    guess : string 
        Letter or word that user guessed.
    """
    
    #Calls function, documented below. 
    print_fact_with_blanks(fact)
    
    #Prints remaining lives for user reference. 
    print('Lives Remaining: ' + str(lives_remaining))
    
    #Displays instructions to user. 
    guess = input(' Guess a single letter or a whole word. Previous guess: ')
    
    return guess             
            
def print_fact_with_blanks(fact): 
    """Updates user on facts structure and informs what letters have been guessed. 
    
    Parameters
    ----------
    fact : string
        Randomly selected fact from list of facts. 
    """
    
    display_fact = '' 
    
    #Loop compares letter user guessed with every letter of the random fact.
    for letter in fact: 
        if guessed_letters.find(letter) > -1: 
            # letter found in random fact - provides position of letter in string. 
            display_fact = display_fact + letter 
        else: 
            # letter not found in random fact - adds hyphen. 
            display_fact = display_fact + '-'
    
    print(display_fact)
    
def process_guess(guess, fact): 
    """What to return after user enters guess(single character or the whole fact).
    
    Parameters
    ----------
    guess : string
        Letter or word that user guessed. 
    fact : string
        Randomly selected fact from list of facts.
        
    Returns
    -------
    whole_fact_guess(guess, fact) : function
        Returned when user attempts to guess entire fact at once. 
    single_letter_guess(guess, fact) : function
        Returned when user guesses a letter, judges whether letter is in the fact.    
    """
    
    #If guess is length of the fact, sends to check validity of whole phrase. 
    if len(guess) > 1 and len(guess) == len(fact): 
        return whole_fact_guess(guess, fact)
    
   #If guess is not the length of the fact, sends to check validity of single letter.
    else: 
        return single_letter_guess(guess, fact)    

def whole_fact_guess(guess, fact):
    """Instructs program on what to do after user attempts to guess the entire fact.
    
    Parameters
    ----------
    guess : string
        Letter or word that user guessed. 
    fact : string 
        Randomly selected fact from list of facts. 
        
    Returns 
    -------
    True : boolean 
        User guessed correctly.
    False : boolean 
        User guessed incorrectly. 
    """
    
    #Allows modification of variable lives_remaining inside of function. 
    global lives_remaining 
    
    if guess.lower() == word.lower(): 
        return True  
    else: 
        lives_remaining = lives_remaining - 1
        return False   
    
def single_letter_guess(guess, fact):
    """Instructs program on what to do after user guesses a letter.
    
    Parameters
    ----------
    guess : string 
        Letter or word that user guessed. 
    fact : string 
        Randomly seleced fact from list of facts 
        
    Returns 
    -------
    True : boolean 
        User guessed correctly. 
    False : boolean
        User guessed incorrectly. 
    """
    
    #Allows variables to be modified inside of function.
    global guessed_letters 
    global lives_remaining 
    
    #If user's guess does not exist inside of the random fact, user loses a life. 
    if fact.find(guess) == -1: 
        lives_remaining = lives_remaining - 1 
    
    #Adds the guess to variable storing previously guessed letters.
    guessed_letters = guessed_letters + guess.lower() 
    
    if all_letters_guessed(fact): 
        return True
    
    return False   

def all_letters_guessed(fact):
    """Instructs program what to do if user guesses all the letters in random fact.
    
    Parameters
    ----------
    fact : string
        Randomly selected fact from list of facts.
        
    Returns 
    -------
    False : boolean 
        User guessed incorrectly.
    True : boolean 
        User guessed correctly. 
    """
    
    #If guess doesn't exist in the random fact, user's guess registered as incorrect.
    for letter in fact: 
        if guessed_letters.find(letter.lower()) == -1:
            return False 
    
    return True 