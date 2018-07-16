# JSONParser-ML
A basic JavaScript Object Notation Parser with a co-occurence algorithm. 

## Input language
This parser requires that the input be one of the following:
##### JSONs
A JSON or a collection of JSONs.  These can be flat, like so.

    {"key":"value","key2":[1, 2]}
Or, they can be formatted.

		{
			"john":"zoeller",
			"apples" {
				"size":0,
				"color":"red"
			}
		}

There can also be many JSONs listed in a row.

	{"first":"value"}
	{"second":"value"}

##### Statements
The program will generate output via command statements in the input, the format of these commands is:
    
    Statement := 
        Command 
        Nested_Command
    Command := keyName opt([ArraySubscript])
	Nested_Command := Command opt(<DotOperator> Command)

examples:

    second
	apples.size
    key2[0]

For more details on the syntax of JSON, see [JSON Language Specification](https://www.json.org/)
Note that my code does not yet strictly implement this language as I am still building. 

Also, a JSON must be listed BEFORE any Statement that references its keys. 

If a Key is present in multiple JSONs, all of the values associated with that key
will be printed in order of most recently created JSON.

## Running the program
##### Without Token Co-occurrence
All files should be in the same directory. Example name: ~/Desktop/jsOnject/
In the simplest case...

    cd ~/Desktop/jsOnject/;
    chmod u+x Main.py
    ./Main.py input.txt
    
Where input.txt contains a series of JSONs and Commands. 
Given the above examples as input, the output should be:  

    No Co-Occurrence input
    Result: value
    Result: 0
    Result: 1

##### With Token Co-occurrence
By providing a second input file via that command line, token co-occurrence will
be calculated.  For a full description of Token Co-occurrence, see the next Section. 

    ./Main input.txt tokenList.txt

The second input file (tokenList.txt above) must be in the following form.

    Token \s Token \n
    Token \s Token \n etc...
    
Standard JSON operators such as a ":", or a ",", can be simply typed as they are,
while Strings will be represented as "" (two consecutive quotes). Ints, booleans,
nulls should be typed out with arbitrary values.  An example of all this would
be:

    , :
    : ""
    { 45
    ] null
    null true

## Token Co-occurrence

Token Co-occurrence is the likelihood that a token (A) will appear within
K tokens of another token (B) in the inputted JSON. For the immediate future,
my program will predetermine K to be 3, although an arbitrary K will be 
implemented soon.  Therefore, an example of the Token co-occurrence would be:

    placeholder
    





