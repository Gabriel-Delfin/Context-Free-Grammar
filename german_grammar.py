import nltk

# Define the grammar
grammar = nltk.CFG.fromstring("""
    S -> NP V '.'
    NP -> DET ADJ N | DET N
    DET -> 'Der' | 'Die' | 'Ein' | 'Eine'
    ADJ -> 'großer' | 'kleiner' | 'schöner' | 'große' | 'kleine' | 'schöne'
    N -> 'Mann' | 'Frau' | 'Hund' | 'Katze'
    V -> 'geht' | 'singt' | 'läuft'
""")

# Create a chart parser based on the grammar
parser = nltk.ChartParser(grammar)

def test_german_grammar(sentence):
    # Separate the sentence with tokens
    tokens = sentence.split()
    
    # Check if parsing succeeds
    parsed_trees = parser.parse(tokens)
    parsing_successful = False
    for tree in parsed_trees:
        parsing_successful = True
        print("Parsing SUCCESSFUL for:", sentence)
        break
    
    # Check if parsing fails
    if not parsing_successful:
        print("Parsing FAILED for:", sentence)
    
    return parsing_successful

# Test cases
test_cases = [
    "Die Frau singt .",
    "Ein Hund läuft .",
    "Der große Mann geht .", # Example with adjective
    "Die kleine Katze läuft .", # Example with adjective
    "Mann Der geht .", # Should fail due to incorrect word order
    "Der Hund Katze .", # Should fail due to lack of verb
    "Ein läuft .", # Should fail due to lack of noun
]

# Execute test cases
print("Starting test cases...\n")
for sentence in test_cases:
    test_german_grammar(sentence)
    print()