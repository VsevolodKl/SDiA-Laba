#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main() {
    // Создание графа как списка смежности
    int V = 5; // Количество вершин
    vector<set<int>> graph(V);
    
    // Добавление рёбер
    graph[0].insert(1);
    graph[0].insert(2);
    graph[1].insert(0);
    graph[1].insert(2);
    graph[1].insert(3);
    graph[2].insert(0);
    graph[2].insert(1);
    graph[2].insert(4);
    graph[3].insert(1);
    graph[3].insert(4);
    graph[4].insert(2);
    graph[4].insert(3);
    
    // Вывод графа
    cout << "Список смежности графа:" << endl;
    for (int i = 0; i < V; i++) {
        cout << "Вершина " << i << ": ";
        for (int neighbor : graph[i]) {
            cout << neighbor << " ";
        }
        cout << endl;
    }
    
    // Проверка смежности
    int u = 1, v = 3;
    cout << "Вершины " << u << " и " << v << " смежны: " 
         << (graph[u].count(v) ? "Да" : "Нет") << endl;
    
    // Степень вершины
    cout << "Степень вершины 2: " << graph[2].size() << endl;
    
    return 0;
}
