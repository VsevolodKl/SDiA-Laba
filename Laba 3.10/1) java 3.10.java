import java.util.*;

public class SimpleGraph {
    public static void main(String[] args) {
        // Создание графа как списка смежности
        int V = 5;
        List<Set<Integer>> graph = new ArrayList<>();
        
        // Инициализация
        for (int i = 0; i < V; i++) {
            graph.add(new HashSet<>());
        }
        
        // Добавление рёбер
        graph.get(0).add(1); graph.get(1).add(0);
        graph.get(0).add(2); graph.get(2).add(0);
        graph.get(1).add(2); graph.get(2).add(1);
        graph.get(1).add(3); graph.get(3).add(1);
        graph.get(2).add(4); graph.get(4).add(2);
        graph.get(3).add(4); graph.get(4).add(3);
        
        // Вывод графа
        System.out.println("Список смежности графа:");
        for (int i = 0; i < V; i++) {
            System.out.print("Вершина " + i + ": ");
            for (int neighbor : graph.get(i)) {
                System.out.print(neighbor + " ");
            }
            System.out.println();
        }
        
        // Проверка смежности
        int u = 1, v = 3;
        if (graph.get(u).contains(v)) {
            System.out.println("Вершины " + u + " и " + v + " смежны: Да");
        } else {
            System.out.println("Вершины " + u + " и " + v + " смежны: Нет");
        }
        
        // Степень вершины
        System.out.println("Степень вершины 2: " + graph.get(2).size());
    }
}
