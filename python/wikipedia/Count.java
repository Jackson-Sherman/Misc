import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

import java.util.ArrayList;
import java.util.HashMap;

public class Count {
	
	public final String content;
	public final String regex;
	
	public static void main (String[] args) {
		Count c = new Count(new File("cropped_article.html"), "[&][^&;]*[;]");
		
		HashMap<String,Integer> map = c.run();
		Count.soutln(map.size());
		ArrayList<String> strs = new ArrayList<>();
		int maxWidth = 0;
		for (String k : map.keySet()) {
			
			maxWidth = Math.max(maxWidth, k.length());
			int i = 0;
			while (i < strs.size() && k.compareTo(strs.get(i)) < 0)
				i++;
			
			strs.add(i, k);
		}
		for (String str : strs) {
			String output = str;
			while (output.length() < maxWidth)
				output = ' ' + output;
			
			Count.sout(output + ' ');
			if (str.equals("&amp;"))
				Count.sout('&' + " ");
			
			else {
				String inte = str.substring(2, str.length()-1);
				Count.sout((char)Integer.parseInt(inte) + " ");
			}
			Count.soutln(map.get(str));
		}
	}
	
	private Count (File file, String regex) {
		String s = "";
		try {
			Scanner sc = new Scanner(file);
			while (sc.hasNextLine()) {
				s += sc.nextLine();
			}
			sc.close();
		} catch (FileNotFoundException e) {
			Count.soutln(e);
			s = "";
		}
		this.content = s;
		this.regex = regex;
	}
	
	private HashMap<String,Integer> run () {
		return this.runAux(this.content, new HashMap<String,Integer>());
	}
	
	private HashMap<String,Integer> runAux (String string, HashMap<String,Integer> map) {
		String[] splitUp = string.split(this.regex, 2);
		
		if (splitUp.length < 2)
			return map;
		
		String key_at_top = string.substring(splitUp[0].length());
		String rest = splitUp[1];
		int key_len = key_at_top.length() - rest.length();

		String key = key_at_top.substring(0, key_len);
		
		if (!map.containsKey(key))
			map.put(key, 0);
		
		map.put(key, map.get(key) + 1);
		
		return this.runAux(rest, map);
	}
	
	private static void sout (Object o) {
		System.out.print(o);
	}
	
	private static void soutln (Object o) {
		System.out.println(o);
	}
}
