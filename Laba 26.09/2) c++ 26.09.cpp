#include <iostream>
#include <queue>
using namespace std;

int main() {
    // Max-heap (по умолчанию)
    priority_queue<int> pq;
    
    // Добавление элементов
    pq.push(3);
    pq.push(1);
    pq.push(4);
    pq.push(1);
    pq.push(5);
    
    // Извлечение в порядке приоритета
    cout << "Priority order: ";
    while (!pq.empty()) {
        cout << pq.top() << " ";
        pq.pop();
    }
    cout << endl;
    
    return 0;
}
