import java.util.*;

public class LexicalAnalyser {
    private static final List<String> KEYWORD_DICTIONARY = new ArrayList<>(Arrays.asList("if", "else", "java", "while", "elseif", "else if", "do", "return", "public", "private", "static", "main", "final", "int", "INTEGER", "double", "boolean", "char", "float", "void", "protected", "break", "abstract", "class", "for", "each", "switch", "this", "throw", "ex", "catch", "break", "case", "const", "continue", "enum", "set", "import", "interface", "extends", "implements", "long", "short", "byte", "String", "super", "try", "new", "default", "System", "print", "println", "printf", "out", "in", "Array", "List", "Hashset"));

    private static final List<Character> OPERATORS = new ArrayList<>(Arrays.asList('+', '-', '/', '*', '%', '=', '>', '<', '!', '&', '|'));

    private static final List<Character> DELIMITERS = new ArrayList<>(Arrays.asList(';', ':', ',', '{', '}', '(', ')', '[', ']'));



    public static List<Token> analyser(String inputCode){
        List<Token> tokens = new ArrayList<>();
        String currentLexeme = "";
        boolean containsDigit = false;
        int state = 0;

        for (int i=0; i<=inputCode.length(); i++){
            char currentChar = (i < inputCode.length()) ? inputCode.charAt(i) : ' ';

            switch (state) {
                case 0: 
                    if (Character.isLetter(currentChar)){ // Automatically detects possible keyword or identifier
                        currentLexeme += currentChar;
                        containsDigit = false;
                        state = 1;
                    } else if (Character.isDigit(currentChar)){ // Automatically detects possible integer or double
                        currentLexeme += currentChar;
                        state = 2;
                    } else if (OPERATORS.contains(currentChar)){ //
                        currentLexeme += currentChar;
                        state = 3;
                    } else if (DELIMITERS.contains(currentChar)){
                        tokens.add(new Token(String.valueOf(currentChar), "delimiter"));
                    }
                    
                    break;

                case 1: // Distinguishing between keyword and identifier
                if (Character.isLetter(currentChar)){
                    currentLexeme += currentChar;
                } else if (Character.isDigit(currentChar)){
                    currentLexeme += currentChar;
                    containsDigit = true; // Used to identify an identifier
                } else {
                    tokens.add(new Token(currentLexeme, containsDigit ? "identifier" : (KEYWORD_DICTIONARY.contains(currentLexeme) ? "keyword" : "identifier")));
                    currentLexeme = "";
                    containsDigit = false;
                    state = 0; // return to start state of FA to analyse next lexeme
                    i--; // Allows for reprocessing of current character to cater for spaces or no spaces between lexemes
                }
                break;

                case 2: // Distinguishing between integer and double
                if(Character.isDigit(currentChar)){
                    currentLexeme += currentChar;
                } else if (Character.isLetter(currentChar)){
                    throw new IllegalArgumentException("Invalid syntax: digit followed by letter");
                }
                else if (currentChar == '.'){
                    currentLexeme += currentChar;
                    state = 4; // Number is a double
                } else {
                    tokens.add(new Token(currentLexeme, "integer"));
                    currentLexeme = "";
                    state = 0; // return to start state of FA to analyse next lexeme
                    i--; // Allows for reprocessing of current character to cater for spaces or no spaces between lexemes
                }
                break;

                case 3: // Operators
                if(OPERATORS.contains(currentChar)){
                    currentLexeme += currentChar;
                } else {
                    tokens.add(new Token(currentLexeme, "operator"));
                    currentLexeme = "";
                    state = 0; // return to start state of FA to analyse next lexeme
                    i--; // Allows for reprocessing of current character to cater for spaces or no spaces between lexemes    
                }
                break;

                case 4: // Doubles
                if (Character.isDigit(currentChar)) {
                    currentLexeme += currentChar;            
                } else if (Character.isLetter(currentChar) || currentChar == '.'){
                    throw new IllegalArgumentException("Invalid syntax: double directly followed by invalid character");
                }else {
                    tokens.add(new Token(currentLexeme, "double"));
                    currentLexeme = "";
                    state = 0; // return to start state of FA to analyse next lexeme
                    i--; // Allows for reprocessing of current character to cater for spaces or no spaces between lexemes
                }
                break;
                
            }
        }
        return tokens;

    }
    
    public static void main(String[] args) {
        String input = "private int count1 = 4; 1count = count1 + 1; if (count >= 10){return 0.523*2 + count}";

        List<Token> tokens = analyser(input);
        System.out.println("Output: Lexeme | Token");
        for (Token token : tokens){
            System.out.println(token.lexeme + " | " + token.tokenLabel);
        }
    }
    
}

class Token{
    String lexeme;
    String tokenLabel;

    public Token(String lexeme, String tokenLabel){
        this.lexeme = lexeme;
        this.tokenLabel = tokenLabel;
    }
}