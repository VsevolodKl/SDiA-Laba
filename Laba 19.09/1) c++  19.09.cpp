#include <iostream>
#include <forward_list>
#include <locale>
using namespace std;

int main() {
    // Установка локали для русского языка
    setlocale(LC_ALL, "ru_RU.UTF-8");
    
    forward_list<int> list;
    
    // Добавление в начало
    list.push_front(3);
    list.push_front(2);
    list.push_front(1);
    
    cout << "Список: ";
    for (const auto& elem : list) {
        cout << elem << " -> ";
    }
    cout << "null" << endl;
    
    // Удаление первого элемента
    list.pop_front();
    cout << "После удаления первого: ";
    for (const auto& elem : list) {
        cout << elem << " -> ";
    }
    cout << "null" << endl;
    
    // Проверка пустоты
    cout << "Список пуст: " << (list.empty() ? "да" : "нет") << endl;
    
    return 0;
}
