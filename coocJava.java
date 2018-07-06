import java.util.Scanner;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.Map;
import java.util.HashMap;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Queue;
import java.util.LinkedList;

//Artschool
//warm neon
private class WordData {
	public String title;
	public int count;
	public boolean paired;

	public WordData(String title) {
		this.title = title;
		this.count = 1;
		this.paired = false;
	}
}

public class cooc {

	public static void main(String[] args) {
		Map<String, Integer> wordCountMap = new HashMap<String, Integer>();

		HashMap<String, HashMap<String, Integer>> coOcMap = 
			new HashMap<String, HashMap<String, Integer>>();

		HashMap<String, HashSet<WordData>> wordDataMap = 
			new HashMap<String, HashSet<WordData>>();
		
		String inputFile = args[0];
		int k = Integer.parseInt(args[1]);
		int maxWindow = k + 1;
		Queue<String> queue = new LinkedList<String>();

		try { 
			Scanner scanner = new Scanner(new File(inputFile));

			while(scanner.hasNext()) {
				String nextLine = scanner.next();
				String[] processedLine = nextLine.replaceAll("[^a-zA-Z ]", "")
											.toLowerCase().split("\\s+");
				String currentWord = processedLine[0];

				//build occurences map
				int occurences;

				if(!wordCountMap.containsKey(currentWord)) 
					occurences = 0;
				else occurences = wordCountMap.get(currentWord); 

				wordCountMap.put(currentWord, ++occurences);


				//build coOcMap
				queue.add(currentWord);
				int queueSize = queue.size();
				int j = 0;

				if(queueSize > maxWindow) 
					queue.poll();

				if(!coOcMap.containsKey(currentWord)) {
				   coOcMap.put(currentWord, new HashMap<String, Integer>());
				}

				if(!wordDataMap.containsKey(currentWord))
					wordDataMap.put(currentWord, new HashSet<WordData>());


				for(String i : queue) {

					if(!i.equals(currentWord)) {
						WordData currWord, iWord;

						if(wordDataMap.get(i).contains(currentWord)) {
							currWord = wordDataMap.get(i).get(currentWord);
						}

						if(coOcMap.get(i).containsKey(currentWord)) {
							currVal = coOcMap.get(i).get(currentWord);
						}

						if(coOcMap.get(currentWord).containsKey(i)) {
							iVal = coOcMap.get(currentWord).get(i);
						}

						if(wordCountMap.get(i) >= occurences) {
							coOcMap.get(i).put(currentWord, ++currVal);
							coOcMap.get(currentWord).put(i, ++iVal);
						}
					}
				}
				//System.out.println(coOcMap.toString());
			}

			scanner.close();
		} catch (FileNotFoundException e) 
			{ System.out.println("No Such file"); }

		//System.out.println(wordCountMap.toString() + "\n");
		//System.out.println(coOcMap.toString());
		//System.out.println(queue.toString());

		InputStreamReader isReader = new InputStreamReader(System.in);
		BufferedReader bufReader = new BufferedReader(isReader);
		
		while(true){ 
			try {
	        	String line = null;
	        
		        if((line = bufReader.readLine()) != null) {
		        	String[] pair = line.split("\\s+");
		        	System.out.printf(pair[0] + " : " + pair[1] + " -> ");
		        	int occured = 0, coOc = 0;

		        	try {
			        	occured = wordCountMap.get(pair[0]);
			        	coOc = coOcMap.get(pair[0]).get(pair[1]);
		        	} catch (NullPointerException n) { }


		        	System.out.printf("%.2f", 
		        		(float)((float)coOc / (float)occured));
		        	System.out.println('\n');
		        }
		        else break;
		    } catch (IndexOutOfBoundsException | IOException e) { 
		    	System.out.println(e); 
		    }
		}
	}
}









