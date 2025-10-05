#include <iostream>
#include <forward_list>
#include <locale>
using namespace std;

int main() {
    // Установка локали для русского языка
    setlocale(LC_ALL, "ru_RU.UTF-8");
    
    forward_list<int> list = {1, 2, 4, 5};
    //Отображение исходного списка
    cout << "Исходный список: ";
    for (const auto& elem : list) {
        cout << elem << " ";
    }
    cout << endl;
    
    // Вставка после первого элемента
    auto it = list.begin();
    list.insert_after(it, 3);
    
    cout << "После вставки 3: ";
    for (const auto& elem : list) {
        cout << elem << " ";
    }
    cout << endl;
    
    // Удаление элемента после первого
    it = list.begin();
    list.erase_after(it);
    
    cout << "После удаления: ";
    for (const auto& elem : list) {
        cout << elem << " ";
    }
    cout << endl;
    
    // Размер списка
    int size = 0;
    for (auto it = list.begin(); it != list.end(); ++it) {
        size++;
    }
    cout << "Размер списка: " << size << endl;
    
    return 0;
}