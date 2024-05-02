/*

Implement C++ program for expression conversion as infix to
postfix and its evaluation using stack based on given conditions:
1. Operands and operator, both must be single character.
2. Input Postfix expression must be in a desired format.
 Only '+', '-', '*' and '/ ' operators are expected.

*/
#include<iostream>
#include<cctype>
#include<cstring>
#include<stack>
using namespace std;

// returns the value when a specific operator
// operates on two operands
int eval(int op1, int op2, char operate) {
   switch (operate) {
      case '*': return op2 * op1;
      case '/': return op2 / op1;
      case '+': return op2 + op1;
      case '-': return op2 - op1;
      default : return 0;
   }
}
int getWeight(char ch) {
   switch (ch) {
      case '/':
      case '*': return 2;
      case '+':
      case '-': return 1;
      default : return 0;
   }
}
// evaluates the postfix operation
// this module neither supports multiple digit integers
// nor looks for valid expression
// However it can be easily modified and some additional
// code can be added to overcome the above mentioned limitations
// it's a simple function which implements the basic logic to
// evaluate postfix operations using stack
int evalPostfix(char postfix[], int size) {
   stack<int> s;
   int i = 0;
   char ch;
   int val;
   while (i < size) {
      ch = postfix[i];
      if (isdigit(ch)) {
         // we saw an operand
         // push the digit onto stack
         s.push(ch-'0');
      }
      else {
         // we saw an operator
         // pop off the top two operands from the
         // stack and evalute them using the current
         // operator
         int op1 = s.top();
         s.pop();
         int op2 = s.top();
         s.pop();
         val = eval(op1, op2, ch);
         // push the value obtained after evaluating
         // onto the stack
         s.push(val);
      }
      i++;
   }
   return val;
}
int getWeight(char ch) {
	switch (ch) {
	case '/':
	case '*': return 2;
	case '+':
	case '-': return 1;
	default : return 0;
	}
}

// convert infix expression to postfix using a stack
void infix2postfix(char infix[], char postfix[], int size) {
	stack<char> s;
	int weight;
	int i = 0;
	int k = 0;
	char ch;
	// iterate over the infix expression
	while (i < size) {
		ch = infix[i];
		if (ch == '(') {
			// simply push the opening parenthesis
			s.push(ch);
			i++;
			continue;
		}
		if (ch == ')') {
			// if we see a closing parenthesis,
			// pop of all the elements and append it to
			// the postfix expression till we encounter
			// a opening parenthesis
			while (!s.empty() && s.top() != '(') {
				postfix[k++] = s.top();
				s.pop();

			}
			// pop off the opening parenthesis also
			if (!s.empty()) {
				s.pop();
			}
			i++;
			continue;
		}
		weight = getWeight(ch);
		if (weight == 0) {
			// we saw an operand
			// simply append it to postfix expression
			postfix[k++] = ch;

		}
		else {
			// we saw an operator
			if (s.empty()) {
				// simply push the operator onto stack if
				// stack is empty
				s.push(ch);
			}
			else {
				// pop of all the operators from the stack and
				// append it to the postfix expression till we
				// see an operator with a lower precedence that
				// the current operator
				while (!s.empty() && s.top() != '(' &&
						weight <= getWeight(s.top())) {
					postfix[k++] = s.top();
					s.pop();

				}
				// push the current operator onto stack
				s.push(ch);
			}
		}
		i++;
	}
	// pop of the remaining operators present in the stack
	// and append it to postfix expression
	while (!s.empty()) {
		postfix[k++] = s.top();
		s.pop();
	}
	postfix[k] = 0; // null terminate the postfix expression
}

// main
int main() {
   char postfix[] = {'a','b','c','+','*','d','/'};
   int i=0;
  // cout<<"Postfix 0"<<postfix[i];
   while(postfix[i]!='\0')
   {
   	if(getWeight(postfix[i])==0)
   	{
   		cout<<" Enter value for "<<postfix[i]<<" = ";
   		cin>>postfix[i];
	   }
	   i++;
   }
   int size = sizeof(postfix);
   int val = evalPostfix(postfix, size);
   cout<<"\nExpression evaluates to "<<val;
   cout<<endl;
   char infix[100];//"A*(B+C)/D";
	cout<<"\nENter Infix Operation:";
	cin>>infix;
	int size = strlen(infix);
	char postfix[size];
	infix2postfix(infix,postfix,size);
	cout<<"\nInfix Expression :: "<<infix;
	cout<<"\nPostfix Expression :: "<<postfix;
	cout<<endl;
   return 0;
}

