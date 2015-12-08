import java.io.*;

public class run2{
	
	public static String[] gen = new String[9150606];
	public static int z = 0; //ctr
	public static boolean branch(Word w){
		//System.out.println("Branching now, printing branches...");
		/*for (int i = 0; i < 8; i++){
			if (w.wordTree[i] == null){
				//System.out.println("It's null, sir! @" + i);
			}
			else
				System.out.println("It's " + w.wordTree[i].str + " @" + i);
		}*/
		//start at 6 o' clock, going ccw
		boolean anyMore = false;
		if (inBounds(w.x+1,w.y,w)){anyMore = true;
		w.wordTree[0] = new Word(w.x+1,w.y,w);}
		if (inBounds(w.x+1,w.y+1,w)){anyMore = true;
		w.wordTree[1] = new Word(w.x+1,w.y+1,w);}
		if (inBounds(w.x,w.y+1,w)){anyMore = true;
		w.wordTree[2] = new Word(w.x,w.y+1,w);}
		if (inBounds(w.x-1,w.y+1,w)){anyMore = true;
		w.wordTree[3] = new Word(w.x-1,w.y+1,w);}
		if (inBounds(w.x-1,w.y,w)){anyMore = true;
		w.wordTree[4] = new Word(w.x-1,w.y,w);}
		if (inBounds(w.x-1,w.y-1,w)){anyMore = true;
		w.wordTree[5] = new Word(w.x-1,w.y-1,w);}
		if (inBounds(w.x,w.y-1,w)){anyMore = true;
		w.wordTree[6] = new Word(w.x,w.y-1,w);}
		if (inBounds(w.x+1,w.y-1,w)){anyMore = true;
		w.wordTree[7] = new Word(w.x+1,w.y-1,w);}
		//System.out.println("Branch terminated, printing branches");
    /*
		for (int i = 0; i < 8; i++){
			if (w.wordTree[i] == null){
				System.out.println("It's null, sir! @" + i);
			}
			else
				System.out.println("It's " + w.wordTree[i].str + " @" + i);
		}*/
		return anyMore;
	}
	
	public static boolean inBounds(int j, int k, Word w){
		return (j >= 0 && j < 4 && k >= 0 && k < 4 && w.val[j][k]);	//if j,k is forbidden pair
	}
	//x,y are starting locations.
	public static void wordGen(int x, int y){
		Word w = new Word(x,y);
		
		if (isIn(w.str, gen)){gen[z] = w.str;
		z++;}
		branch(w);
		for (Word w1: w.wordTree){
			if (w1 != null)
        wordGrow(w1);
		}
		return;
	}
	
	public static void wordGrow(Word w){
		if (isIn(w.str, gen)){gen[z] = w.str;
		z++;}
		if (!branch(w)){
			return;
		};
		for (Word w1: w.wordTree){
			if (w1 != null && w1.str != null)
				wordGrow(w1);
		}
		return;
	}
	
	public static boolean isIn(String s, String[] a){
		for (String s1:a)
			if (s.equals(s1))
				return true;
		return false;
	}
	public static void main(String [] args) {

        // The name of the file to open.
        String fileName = "words.txt";

        // This will reference one line at a time
        String line = null;
        String[] words = new String[235900];
        int i = 0;

        try {
            // FileReader reads text files in the default encoding.
            FileReader fileReader = 
                new FileReader(fileName);

            // Always wrap FileReader in BufferedReader.
            BufferedReader bufferedReader = 
                new BufferedReader(fileReader);

            while((line = bufferedReader.readLine()) != null) {
                words[i] = line.toLowerCase();
				i += 1;
            }   

            // Always close files.
            bufferedReader.close();         
        }
        catch(FileNotFoundException ex) {
            System.out.println(
                "Unable to open file '" + 
                fileName + "'");                
        }
        catch(IOException ex) {
            System.out.println(
                "Error reading file '" 
                + fileName + "'");                  
            // Or we could just do this: 
            // ex.printStackTrace();
        }
		//Load thing
		for (i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
        System.out.println("ayy lmao");
				wordGen(i,j);
			}
		}
		
    int ctr = 0;
    for (String g: gen)
      if (g == null)
        break;
      else
        ctr++;
    System.out.println(ctr);/*
    
		int ctr = 0;
		for (String w: words){
			for (String g: gen) {
				if (w.equals(g)){
					System.out.println(w);
					ctr++;
          break;
        }
      }
		}
		
		System.out.println(ctr);*/
	}
	
	
	
	
}