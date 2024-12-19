# PLY-Easier (PLYE)
A tool to make your own programming language  
This tool is heavily based on PythonLexYacc, but easier to use.  
You need to download python to use this package.  

## Tokens.txt
-Is a list of all objects/functions to be recognised  
-Is in the form of a dictionary, but with many lines:  
--tokenName:[type, contents] * a few  
---The 'type' parameter is function or regEx.  
---this is because sometimes conversion might be needed.  

## Grammar
-Is a set of rules on how the parser should parse the tokens/groups of tokens  
-Is also in the form of a dictionary with many lines:  
--grammarRule:[tokenName, contents]  
---TokenName is the token the rule should return when finding a group  
---Contents is the rule for p[0], what it returns  
-  
### GRAMMAR_RULES:  
-----Grammar rules are in the form expression : some stuff  
-----stuff can be words, regEx or tokens.  
-----To put them together, use expression : some stuff | expression : more stuff  
-----Contents should contain what to do with p, the parameters.  
-----The first item is p[0], then p[1] so on.  
-----expression just denotes anything  

## Precedence.txt
-Decides what functions/tokens should be identified/initiated first.  
-The bottom ones go first, and the top last.  
--In the form of a tuple with tuples inside:  
---(direction, *stuff)  
----direction is left or right  
----Stuff is the tokens to be processed first.  

## Other.txt:  
-Has basically just got settings  
--Has many lines in form of:  
---ignore=[*charsOrRegExEs]  
---t_error=[functionWhenThereIsAnErrorInIdentifyingToken]  
---p_error=[functionWhenThereIsAnErrorInProccessingGrammar]  
---inputType=[lineByLine or editor]  
---printTokens=[trueOrFalse]  
---name=[thename]  
----DON'T INCLUDE 'identifier=[' AND ']'  
----ONLY ignore, t_error, p_error have been used.  

### Constructor.py  
-Run this program to construct your language. DO NOT EDIT THIS FILE  

### FOLDER: Name  
-There will be a folder with the name of your coding language.  
-Do not edit __pycache__, or parsetab.py, parser.out or LANGUAGE.py.  
--Only run runProgram.ps1 to run your program  

#### Calculator (Needs Python) (Built with PLY)  
To use the calculator, download calculator.zip and uncompress it.  
Then run the file. Enter expressions and it shows you how it parses it.  
