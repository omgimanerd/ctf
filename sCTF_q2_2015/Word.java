public class Word{
	public String[][] chart = new String[][]{
		{"e","e","c","a"},
		{"a","l","e","p"},
		{"h","n","b","o"},
		{"q","t","t","y"}
	};
	public String str;
	public boolean[][] val; //coords
	public int x;
	public int y;
	public Word[] wordTree = new Word[8];
	
	public Word(int j, int k){
		str = chart[j][k];
		val = new boolean[4][4];
		for (int i = 0; i < 4; i++){
			for (int a = 0; a < 4; a++){
				val[i][a] = true;
			}
		}
		val[j][k] = false;
		x = j;
		j = k;
	}
	public Word(int j, int k, Word w){
		//System.out.println("Branching from " + w.str);
		//System.out.println(j + "," + k);
		str = w.str + chart[j][k];
		//System.out.println(str);
		val = new boolean[4][4];
		//for (int i = 0; i < 8; i++){
			//wordTree[i] = null;
		//}
		for (int a = 0; a < 4; a++){
			for (int b = 0; b < 4; b++){
				val[a][b] = w.val[a][b];
			}
		}
		val[j][k] = false;
		x = j;
		y = k;
	}
}