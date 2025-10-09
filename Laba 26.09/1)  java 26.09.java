import java.util.PriorityQueue;

public class SimpleHeap {
    public static void main(String[] args) {
        // Min-heap (по умолчанию)
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        
        // Добавление элементов
        heap.add(3);
        heap.add(1);
        heap.add(4);
        heap.add(1);
        heap.add(5);
        
        // Извлечение в порядке приоритета
        System.out.print("Min-heap order: ");
        while (!heap.isEmpty()) {
            System.out.print(heap.poll() + " ");
        }
        System.out.println();
    }
}
