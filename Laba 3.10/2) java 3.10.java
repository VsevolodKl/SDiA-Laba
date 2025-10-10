import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Создание графа как матрицы смежности
        int V = 5;
        boolean[][] matrix = new boolean[V][V];
        
        // Добавление рёбер
        matrix[0][1] = true; matrix[1][0] = true;
        matrix[0][2] = true; matrix[2][0] = true;
        matrix[1][2] = true; matrix[2][1] = true;
        matrix[1][3] = true; matrix[3][1] = true;
        matrix[2][4] = true; matrix[4][2] = true;
        matrix[3][4] = true; matrix[4][3] = true;
        
        // Вывод матрицы
        System.out.println("Матрица смежности:");
        System.out.print("  ");
        for (int i = 0; i < V; i++) {
            System.out.print(i + " ");
        }
        System.out.println();
        
        for (int i = 0; i < V; i++) {
            System.out.print(i + " ");
            for (int j = 0; j < V; j++) {
                if (matrix[i][j]) {
                    System.out.print("1 ");
                } else {
                    System.out.print("0 ");
                }
            }
            System.out.println();
        }
        
        // Проверка смежности
        int u = 1, v = 3;
        if (matrix[u][v]) {
            System.out.println("Вершины " + u + " и " + v + " смежны: Да");
        } else {
            System.out.println("Вершины " + u + " и " + v + " смежны: Нет");
        }
        
        // Подсчёт степени вершины
        int vertex = 2;
        int degree = 0;
        for (int i = 0; i < V; i++) {
            if (matrix[vertex][i]) {
                degree++;
            }
        }
        System.out.println("Степень вершины " + vertex + ": " + degree);
        
        // Создание графа как списка смежности через массивы
        int[][] adjList = new int[V][];
        adjList[0] = new int[]{1, 2};
        adjList[1] = new int[]{0, 2, 3};
        adjList[2] = new int[]{0, 1, 4};
        adjList[3] = new int[]{1, 4};
        adjList[4] = new int[]{2, 3};
        
        // Вывод списка смежности
        System.out.println("\nСписок смежности через массивы:");
        for (int i = 0; i < V; i++) {
            System.out.print("Вершина " + i + ": ");
            for (int j = 0; j < adjList[i].length; j++) {
                System.out.print(adjList[i][j] + " ");
            }
            System.out.println();
        }
    }
}
