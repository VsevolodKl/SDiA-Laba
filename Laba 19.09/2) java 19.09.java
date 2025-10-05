import java.util.LinkedList;
import java.util.Iterator;
import java.io.PrintStream;
import java.io.UnsupportedEncodingException;

public class Main {
    public static void main(String[] args) {
        try {
            System.setOut(new PrintStream(System.out, true, "UTF-8"));
        } catch (UnsupportedEncodingException e) {
            System.out.println("Ошибка кодировки");
        }
        //Объявляем список
        LinkedList<String> list = new LinkedList<>();
        //Добавляем элементы
        list.addFirst("яблоко");
        list.addFirst("банан");
        list.addFirst("апельсин");
        
        System.out.println("Список: " + list);
        
        // Поиск
        System.out.println("Содержит 'банан': " + list.contains("банан"));
        System.out.println("Индекс 'апельсин': " + list.indexOf("апельсин"));
        
        // Обход итератором
        System.out.print("Обход итератором: ");
        Iterator<String> it = list.iterator();
        while (it.hasNext()) {
            System.out.print(it.next() + " ");
        }
        System.out.println();
        
        // Удаление по значению
        list.remove("банан");
        System.out.println("После удаления: " + list);
        
        // Очистка списка
        list.clear();
        System.out.println("После очистки: " + list);
        System.out.println("Пустой: " + list.isEmpty());
    }
}