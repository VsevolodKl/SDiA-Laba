#include <iostream>
#include <vector>

using namespace std;

int main() {
    // Создание графа как матрицы смежности
    int V = 5; // Количество вершин
    vector<vector<bool>> matrix(V, vector<bool>(V, false));
    
    // Функция для добавления ребра
    auto addEdge = [&](int u, int v) {
        matrix[u][v] = true;
        matrix[v][u] = true;
    };
    
    // Добавление рёбер
    addEdge(0, 1);
    addEdge(0, 2);
    addEdge(1, 2);
    addEdge(1, 3);
    addEdge(2, 4);
    addEdge(3, 4);
    
    // Вывод матрицы смежности
    cout << "Матрица смежности:" << endl;
    cout << "  ";
    for (int i = 0; i < V; i++) {
        cout << i << " ";
    }
    cout << endl;
    
    for (int i = 0; i < V; i++) {
        cout << i << " ";
        for (int j = 0; j < V; j++) {
            cout << (matrix[i][j] ? "1 " : "0 ");
        }
        cout << endl;
    }
    
    // Проверка смежности
    int u = 1, v = 3;
    cout << "Вершины " << u << " и " << v << " смежны: " 
         << (matrix[u][v] ? "Да" : "Нет") << endl;
    
    // Подсчёт степени вершины
    int vertex = 2;
    int degree = 0;
    for (int i = 0; i < V; i++) {
        if (matrix[vertex][i]) degree++;
    }
    cout << "Степень вершины " << vertex << ": " << degree << endl;
    
    return 0;
}
