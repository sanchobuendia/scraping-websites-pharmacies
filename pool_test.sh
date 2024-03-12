export TESTING=True # Set the testing flag to true

# Run the tests using coverage
coverage run -m pytest tests
coverage report -m --omit=tests/*

# sh pool_test.sh
# pystest tests