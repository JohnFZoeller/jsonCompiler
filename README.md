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

    apples
	apples.size
    key2[0]

For more details on the syntax of JSON, see [JSON Language Specification](https://www.json.org/)
Note that my code does not yet strictly implement this language as I am still building. 

Also, a JSON must be listed BEFORE any Statement that references its keys. 

## Running the program
##### Without Token Co-occurrence
All files should be in the same directory. Example name: ~/Desktop/jsOnject/
In the simplest case...

    cd ~/Desktop/jsOnject/;
    chmod u+x Main.py
    ./Main.py input.txt
    
Where input.txt contains a series of JSONs and Commands. 
Given the above examples as input, the output should be. 

    
    

##### With Token Co-occurrence


## Token Co-occurrence


