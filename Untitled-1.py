"""Stack Overflow
Products
Search…
Home
PUBLIC
Questions
Tags
Users
Companies
COLLECTIVES
Explore Collectives
TEAMS
Stack Overflow for Teams – Start collaborating and sharing organizational knowledge. 
Building a parser (Part I)
Asked 10 years, 4 months ago
Modified 3 years ago
Viewed 40k times
33

25
I'm making my own javascript-based programming language (yeah, it is crazy, but it's for learn only... maybe?). Well, I'm reading about parsers and the first pass is to convert the code source to tokens, like:

if(x > 5)
  return true;
Tokenizer to:

T_IF          "if"
T_LPAREN      "("
T_IDENTIFIER  "x"
T_GT          ">"
T_NUMBER      "5"
T_RPAREN      ")"
T_IDENTIFIER  "return"
T_TRUE        "true"
T_TERMINATOR  ";"
I don't know if my logic is correct for that for while. On my parser it is even better (or not?) and translate to it (yeah, multidimensional array):

T_IF             "if"
  T_EXPRESSION     ...
    T_IDENTIFIER     "x"
    T_GT             ">"
    T_NUMBER         "5"
  T_CLOSURE        ...
    T_IDENTIFIER     "return"
    T_TRUE           "true"
I have some doubts:

Is my way better or worse that the original way? Note that my code will be read and compiled (translated to another language, like PHP), instead of interpreted all the time.
After I tokenizer, what I need do exactly? I'm really lost on this pass!
There are some good tutorial to learn how I can do it?
Well, is that. Bye!

parsing
programming-languages
translate
Share
Follow
asked Feb 26, 2012 at 11:11
user avatar
David Rodrigues
11.4k1414 gold badges5454 silver badges8787 bronze badges
16
Hey, making a programming language isn't crazy. Many people here are doing the same thing. – 
ApprenticeHacker
 Feb 26, 2012 at 11:19
3
Did you try the Dragon-Book? Basically what you call pass one is the lexer stage, followed by the actual syntactical parsing stage -> ideally outputting some kind of AST (Abstract Syntax Tree) which you can then semantically analyse (parse) or convert to your target language – 
stryba
 Feb 26, 2012 at 11:33
@IntermediateHacker Haha... Yeah, the crazy part is that is very much complex to one people do it. But to learn is a very good thing, really. For a professional use I guess that need a team, so is crazy do it alone. :p – 
David Rodrigues
 Feb 26, 2012 at 11:33 
Add a comment
4 Answers
Sorted by:
Introducing: Trending sort 
You can now choose to sort by Trending, which boosts votes that have happened recently, helping to surface more up-to-date answers.

Trending is based off of the highest score sort and falls back to it if no posts are trending.

 

Highest score (default)
28
Generally, you want to separate the functions of the tokeniser (also called a lexer) from other stages of your compiler or interpreter. The reason for this is basic modularity: each pass consumes one kind of thing (e.g., characters) and produces another one (e.g., tokens).

So you’ve converted your characters to tokens. Now you want to convert your flat list of tokens to meaningful nested expressions, and this is what is conventionally called parsing. For a JavaScript-like language, you should look into recursive descent parsing. For parsing expressions with infix operators of different precedence levels, Pratt parsing is very useful, and you can fall back on ordinary recursive descent parsing for special cases.

Just to give you a more concrete example based on your case, I’ll assume you can write two functions: accept(token) and expect(token), which test the next token in the stream you’ve created. You’ll make a function for each type of statement or expression in the grammar of your language. Here’s Pythonish pseudocode for a statement() function, for instance:

def statement():

  if accept("if"):
    x = expression()
    y = statement()
    return IfStatement(x, y)

  elif accept("return"):
    x = expression()
    return ReturnStatement(x)

  elif accept("{")
    xs = []
    while True:
      xs.append(statement())
      if not accept(";"):
        break
    expect("}")
    return Block(xs)

  else:
    error("Invalid statement!")
This gives you what’s called an abstract syntax tree (AST) of your program, which you can then manipulate (optimisation and analysis), output (compilation), or run (interpretation).

Share
Follow
answered Feb 26, 2012 at 11:35
user avatar
Jon Purdy
51.5k77 gold badges9393 silver badges161161 bronze badges
Add a comment
24
Most toolkits split the complete process into two separate parts

lexer (aka. tokenizer)
parser (aka. grammar)
The tokenizer will split the input data into tokens. The parser will only operate on the token "stream" and build the structure.

Your question seems to be focused on the tokenizer. But your second solution mixes the grammar parser and the tokenizer into one step. Theoretically this is also possible but for a beginner it is much easier to do it the same way as most other tools/framework: keep the steps separate.

To your first solution: I would tokenize your example like this:

T_KEYWORD_IF   "if"
T_LPAREN       "("
T_IDENTIFIER   "x"
T_GT           ">"
T_LITARAL      "5"
T_RPAREN       ")"
T_KEYWORD_RET  "return"
T_KEYWORD_TRUE "true"
T_TERMINATOR   ";"
In most languages keywords cannot be used as method names, variable names and so on. This is reflected already on the tokenizer level (T_KEYWORD_IF, T_KEYWORD_RET, T_KEYWORD_TRUE).

The next level would take this stream and - by applying a formal grammar - would build some datastructure (often called AST - Abstract Syntax Tree) which might look like this:

IfStatement:
    Expression:
        BinaryOperator:
            Operator:     T_GT
            LeftOperand: 
               IdentifierExpression:
                   "x"
            RightOperand:
                LiteralExpression
                    5
    IfBlock
        ReturnStatement
            ReturnExpression
                LiteralExpression
                    "true"
    ElseBlock (empty)
Implementing the parser by hand is usually done by some frameworks. Implementing something like that by hand and efficiently is usually done at a university in the better part of a semester. So you really should use some kind of framework.

The input for a grammar parser framework is usually a formal grammar in some kind of BNF. Your "if" part migh look like this:

IfStatement: T_KEYWORD_IF T_LPAREN Expression T_RPAREN Statement ;

Expression: LiteralExpression | BinaryExpression | IdentifierExpression | ... ;

BinaryExpression: LeftOperand BinaryOperator RightOperand;

....
That's only to get the idea. Parsing a realworld-language like Javascript correctly is not an easy task. But funny.

Share
Follow
answered Feb 26, 2012 at 11:57
user avatar
A.H.
61.1k1414 gold badges8686 silver badges116116 bronze badges
Add a comment
5
Is my way better or worse that the original way? Note that my code will be read and compiled (translated to another language, like PHP), instead of interpreted all the time.

What's the original way ? There are many different ways to implement languages. I think yours is fine actually, I once tried to build a language myself that translated to C#, the hack programming language. Many language compilers translate to an intermediate language, it's quite common.

After I tokenizer, what I need do exactly? I'm really lost on this pass!

After tokenizing, you need to parse it. Use some good lexer / parser framework, such as the Boost.Spirit, or Coco, or whatever. There are hundreds of them. Or you can implement your own lexer, but that takes time and resources. There are many ways to parse code, I generally rely on recursive descent parsing.

Next you need to do Code Generation. That's the most difficult part in my opinion. There are tools for that too, but you can do it manually if you want to, I tried to do it in my project, but it was pretty basic and buggy, there's some helpful code here and here.

There are some good tutorial to learn how I can do it?

As I suggested earlier, use tools to do it. There are a lot of pretty good well-documented parser frameworks. For further information, you can try asking some people who know about this stuff. @DeadMG , over at the Lounge C++ is building a programming language called "Wide". You may try consulting him.

Share
Follow
edited Jan 18, 2021 at 12:34
user avatar
CommunityBot
111 silver badge
answered Feb 26, 2012 at 11:30
user avatar
ApprenticeHacker
20.3k2626 gold badges100100 silver badges152152 bronze badges
Add a comment
2
Let's say I have this statement in a programming language:

if (0 < 1) then
   print("Hello")
The lexer will translate it into:

keyword: if
num: 0
op: <
num: 1
keyword: then
keyword: print
string: "Hello"
The parser will then take the information (aka "Token Stream") and make this:

if:
  expression:
    <:
      0, 1
then:
  print:
    "Hello"
I don't know if this will help or not, but I hope it does.

Share
Follow
answered Jun 30, 2019 at 15:27
user avatar
InfiniteDonuts
8777 bronze badges
Is this a new question or an attempt to rephrase one of the other answers? – 
RalfFriedl
 Jun 30, 2019 at 15:49
Add a comment
Your Answer
Sign up or log in
Post as a guest
Name
Email
Required, but never shown

By clicking “Post Your Answer”, you agree to our terms of service, privacy policy and cookie policy

Not the answer you're looking for? Browse other questions tagged parsing programming-languages translate or ask your own question.
The Overflow Blog
Exploring the interesting and strange results from our 2022 Developer Survey...
Seeing is believing: The Stack Overflow Podcast now available as video
Featured on Meta
Testing new traffic management tool
Duplicated votes are being cleaned up
Trending: A new answer sorting option
Ask Wizard Test Results and Next Steps
Updated button styling for vote arrows: currently in A/B testing
The [hyphen] tag is being burninated
Linked
0
How to create a search language?
0
Creating grammar for basic parser in scala
0
How to use Parse in java project Eclipse
Related
2
Is there a grammar parser (similar to yapps for python) for C++?
27
hand coding a parser
9
Parser vs. lexer and XML
3
Questions about grammar / parser theory
1
Python: parse commandline
15
How do I parse basic arithmetic (eg "5+5") using a simple recursive descent parser in C++?
2
Generating a JavaScript SQL parser for SQLite3 (with Lemon? ANTLR3?)
16
Differentiating between ">>" and ">" when parsing generic types
7
Can parser error recovery be guided automatically by the grammar?
Hot Network Questions
Lossless beam splitter relations
Can a US state opt to become a territory without leaving the nation as a whole?
How did this building's windows get like this?
Are density functionals distributive over densities?
Enumeration of sqrt signs
Bend straight object on corners 90 degrees
Could the right to "life" in the constitution be used by the supreme court to reject a federal law forbidding abortion bans?
What are the ethics of reviewing a paper, spotting issues, not raising them in the review, and then trying to publish a paper on the issues?
What did Putin do to ensure that he doesn't get overthrown by a military coup or to reduce the likelihood of it?
constexpr C++ error: destructor used before its definition
Pairs at every distance
How to respond politely to a client who is wrong about a small detail
Number of binary partitions
The FAA is asking for medical records that I don’t want to give can I refuse?
SQL Return Table with where clause and occurrences of value of total table
Why would giving birth to a boy child make the Boleyns "untouchable"?
Is white wire with grey stripes positive or negative wire?
Small examples of exceptional hyperbolic Dehn Filling of hyperbolic manifolds
Is it secure that Linux have default users?
Is it okay to plug 16A/250V appliances to a 10A/250V outlet?
How much safer would a spaceship clad in ice be?
What's complicated about regression to the mean?
Best way to smell-proof a revolver in 1998?
Print a list of license plate numbers of all cars that went over the speed limit, as well as the average speed of each of those cars
 Question feed

STACK OVERFLOW
Questions
Help
PRODUCTS
Teams
Cookie Settings
Cookie Policy
STACK EXCHANGE NETWORK
Technology
Culture & recreation
Life & arts
Science
Professional

Business
API
Data
Blog
Facebook
Twitter
LinkedIn
Instagram
Site design / logo © 2022 Stack Exchange Inc; user contributions licensed under cc by-sa. rev 2022.7.1.42502

Your privacy

By clicking “Accept all cookies”, you agree Stack Exchange can store cookies on your device and disclose information in accordance with our Cookie Policy."""