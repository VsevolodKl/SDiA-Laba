import java.util.LinkedList;
import java.io.PrintStream;
import java.io.UnsupportedEncodingException;

public class Main {
    public static void main(String[] args) {
        System.setOut(new PrintStream(System.out, true, "UTF-8"));
        //Объявляем список
        LinkedList<Integer> list = new LinkedList<>();
        
        // Добавление элементов
        list.addFirst(3);
        list.addFirst(2);
        list.addFirst(1);
        
        System.out.println("Список: " + list);
        System.out.println("Первый элемент: " + list.getFirst());
        
        // Удаление из начала
        list.removeFirst();
        System.out.println("После удаления первого: " + list);
        
        // Размер списка
        System.out.println("Размер: " + list.size());
        System.out.println("Пустой: " + list.isEmpty());
    }
}