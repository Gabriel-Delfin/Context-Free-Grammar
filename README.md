# Context-Free-Grammar

## Description

The language I chose was german. Since it is a really huge language with too many options of grammar I decided to divided into small sentences with the following order:
1.  Article
2. Noun
3. Adjective (optional)
4. Verb

This grammar consists defining how sentences (S), noun phrases (NP), articles (ART), adjectives (ADJ), nouns (N), and verbs (V) can be constructed.

## Models
This is the model we are using to define our sentences (S). 

- S -> NP V '.'
- NP -> ART ADJ N | ART N
- ART -> 'Der' | 'Die' | 'Ein' | 'Eine'
- ADJ -> 'großer' | 'kleiner' | 'schöner' | 'große' | 'kleine' | 'schöne'
- N -> 'Mann' | 'Frau' | 'Hund' | 'Katze'
- V -> 'geht' | 'singt' | 'läuft'

We are not using left recursion and the vocabulary is restricted. If we wish to add more words to this, we would need to add them manually to the code.

## Code
If you wish to download the code, I will leave a document called "german_grammar_analysis" explaining how to run the code and explaining every part of the program.
