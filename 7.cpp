/*
The ticket booking system of Cinemax theater has to be implemented
using C++ program. There are 10 rows and 7 seats in each row.
Doubly circular linked list has to be maintained to keep track of free
seats at rows. Assume some random booking to start with. Use array to
store pointers (Head pointer) to each row On demand
The list of available seats is to be displayed
*/

#include <iostream>
using namespace std;

class node
{
public:
    node *next;
    node *prev;
    int seat;
    string id;
    int status;
};
// define class cinemax
class cinemax
{
public:
    node *head, *tail, *temp;
    cinemax()
    {
        head == NULL;
    }
    void create_list();
    void display();
    void book();
    void cancel();
    void avail();
};
// defining every function in class cinemax.
void cinemax::create_list()
{
    int i = 1;
    temp = new node;
    temp->seat = 1;
    temp->status = 0;
    temp->id = "null";
    tail = head = temp;
    for (i = 2; i <= 70; i++)
    {
        node *p;
        p = new node;
        p->seat = i;
        p->status = 0;
        p->id = "null";
        tail->next = p;
        tail = p;
        tail->next = head;
        head->prev = tail;
    }
}
void cinemax::display()
{
    {
        int r = 1;
        node *temp;
        temp = head;
        int count = 0;
        cout << "\n----------------------------------------------\n";
        cout << "Screenthis way\n";
        cout << "----------------------------------------------\n";
        cout<<endl;
        while (temp->next != head)
        {
            if (temp->seat / 10 == 0)
            {
                cout << "S0" << temp->seat << " :";
            }
            else
            {
                cout << "S" << temp->seat << " :";
            }
            if (temp->status == 0)
            {
                cout << "|___|";
            }
            else
            {
                cout << "|_B_|";
                count++;
            }
            if (count % 7 == 0)
            {
                cout << endl;
                r++;
            }
            temp = temp->next;
        }
        cout << "S" << temp->seat << " :";
        if (temp->status == 0)
        {
            cout << "|___|";
        }
        else
        {
            cout << "|_B_|";
        }
    }
}

void cinemax::book()
{
    int x;
    string y;
label:
    cout << "\nEnter the seat number to be booked:\n";
    cin >> x;
    cout << "Enter your id";
    cin >> y;
    if (x < 1 || x > 70)
    {
        cout << "Enter correct seat number to book (1-70)\n";
        goto label;
    }
    node *temp;
    temp = new node;
    temp = head;
    while (temp->seat != x)
    {
        temp = temp->next;
    }
    if (temp->status == 1)
    {
        cout << "\nSeat is already booked";
    }
    else
    {
        temp->status = 1;
        temp->id = y;
        cout << "Seat " << x << " booked!\n";
    }   
}
void cinemax::cancel()
{
    int x;
    string y;
label1:
    cout << "Enter the number to cancel booking:\n";
    cin >> x;
    cout << "Enter your id:\n";
    cin >> y;
    if (x < 1 || x > 70)
    {
        cout << "Enter correct seat number to cancel:";
        goto label1;
    }
    node *temp;
    temp = new node;
    temp = head;
    while (temp->seat != x)
    {
        temp = temp->next;
    }
    if (temp->status == 0)
    {
        cout << "Seat not booked yet!!\n";
    }
    else
    {
        if (temp->id == y)
        {
            temp->status = 0;
            cout << "Seat Cancelled!\n";
        }
        else
        {
            cout << "Wrong ID !!! Seat number cannot be cancelled!!\n";
        }
    }
}
void cinemax::avail()
{
    int r = 1;
    temp = head;
    int count = 0;
    cout << "\n\n\n\n";
    cout << "Screen this way\n";
    cout << "---------------------------------------------------\n";
    while (temp->next != head)
    {
        {
            if (temp->seat / 10 == 0)
            {
                cout << " S0" << temp->seat << " :";
            }
            else
            {
                cout << " S" << temp->seat << " :";
            }
            if (temp->status == 0)
            {
                cout << "|___| ";
            }
            else if (temp->seat == 0)
            {
                cout << " ";
            }
            count++;
            if (count % 7 == 0)
            {
                cout << endl;
            }
        }
        temp = temp->next;
    }
    if (temp->status == 0)
    {
        cout << "S" << temp->seat << " :";
        if (temp->status == 0)
        {
            cout << "|___|";
        }
    }
}

int main()
{
    cinemax obj;
    obj.create_list();
    int ch;
    char c = 'y';
    while (c == 'y')
    {
        obj.display();
        cout << "\n*********************************************\n";
        cout << " CINEMAX MOVIE THEATRE\n";
        cout << "   *********************************************\n";
        cout << "\nEnter Choice\n1.Current SeatStatus\n2.Book Seat \n3.Available Seat\n4.CancelSeat\n";
        cin >> ch;
        switch (ch)
        {
        case 1:
            obj.display();
            break;
        case 2:
            obj.book();
            break;
        case 3:
            obj.avail();
            break;
        case 4:
            obj.cancel();
            break;
        default:
            cout << "Wrong choice input\n";
        }
        cout << "\nDo you want to perform any other operation : (y/n)\n";
        cin >> c;
    }
    return 0;
}