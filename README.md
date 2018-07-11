# jsonParser-ML
A basic JavaScript Object Notation Parser with a co-occurence algorithm. 

## Input language
This parser requires that the input be in the following 2 formats:

- A JSON or a collection of JSONs.  These can be flat, like so:
		{"key":"value","key2":[1, 2]}
- Or they can be formatted:
		{
			"john":"zoeller",
			"apples" {
				"size":0,
				"color":"red"
			}
		}

- There can be many JSONs listed in a row:
	{"first":"value"}
	{"second":"value"}

- The program will generate output via commands in the input
  the format of these commands is:

	__keyName__ **opt**( *Dot Operator* __KeyName__ )

- example:

	apples.size


## Running the program
