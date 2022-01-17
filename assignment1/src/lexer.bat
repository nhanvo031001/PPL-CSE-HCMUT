echo "Generating..."
python run.py gen

echo "Testing lexer..."
python run.py test LexerSuite

echo "Testing parser..."
python run.py test ParserSuite