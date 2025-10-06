#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> heap = {3, 1, 4, 1, 5, 9};
    
    // Создание max-heap
    make_heap(heap.begin(), heap.end());
    cout << "Max-heap: ";
    for (int x : heap) cout << x << " ";
    cout << endl;
    
    // Добавление элемента
    heap.push_back(7);
    push_heap(heap.begin(), heap.end());
    cout << "After push 7: ";
    for (int x : heap) cout << x << " ";
    cout << endl;
    
    // Извлечение максимального
    pop_heap(heap.begin(), heap.end());
    int max_val = heap.back();
    heap.pop_back();
    cout << "Popped: " << max_val << endl;
    cout << "Heap now: ";
    for (int x : heap) cout << x << " ";
    cout << endl;
    
    return 0;
}
