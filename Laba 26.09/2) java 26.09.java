import java.util.PriorityQueue;
import java.util.Collections;

public class SimpleMaxHeap {
    public static void main(String[] args) {
        // Max-heap
        PriorityQueue<Integer> heap = new PriorityQueue<>(Collections.reverseOrder());
        
        // Добавление элементов
        heap.add(3);
        heap.add(1);
        heap.add(4);
        heap.add(1);
        heap.add(5);
        
        // Извлечение в порядке приоритета
        System.out.print("Max-heap order: ");
        while (!heap.isEmpty()) {
            System.out.print(heap.poll() + " ");
        }
        System.out.println();
    }
}
