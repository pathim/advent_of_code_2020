#include <iostream>
#include <vector>
#include <fstream>
#include <string>

struct Node{
	Node(int val):value(val){}
	Node* prev=nullptr;
	Node* next=nullptr;
	int value;
	void insert_after(Node* n){
		auto nx=this->next;
		this->next=n;
		n->prev=this;
		while (n->next){
			n=n->next;
		}
		n->next=nx;
		nx->prev=n;
	}
	void remove_range(Node* last){
		auto pr=this->prev;
		auto nx=last->next;
		pr->next=nx;
		nx->prev=pr;
		this->prev=nullptr;
		last->next=nullptr;
	}
	static Node* init(int max){
		auto cur=new Node(max);
		auto prev=cur;
		for(int i=1;i<max;i++){
			auto n=new Node(i);
			prev->next=n;
			n->prev=prev;
			prev=n;
		}
		cur->prev=prev;
		prev->next=cur;
		return cur->next;
	}
};

template<typename T>
void set_start_values(Node* start,T values){
	auto cur=start;
	for(const auto v:values){
		cur->value=v;
		cur=cur->next;
	}
}

void do_turn(Node* &current,Node* lookup[],int max_val){
	int invalid[3];
	Node* pickup_start=current->next;
	invalid[0]=pickup_start->value;
	Node* pickup_end=pickup_start->next;
	invalid[1]=pickup_end->value;
	pickup_end=pickup_end->next;
	invalid[2]=pickup_end->value;
	auto dest_val=current->value;
	do{
		dest_val--;
		if (dest_val==0){
			dest_val=max_val;
		}
	} while(dest_val==invalid[0] || dest_val==invalid[1] || dest_val==invalid[2]);
	auto dest=lookup[dest_val];
	pickup_start->remove_range(pickup_end);
	dest->insert_after(pickup_start);
	current=current->next;
}

int main(){
	std::string s;
	std::getline(std::ifstream{"input"},s);
	std::vector<int> start_values;
	for(const auto c:s){
		start_values.push_back(c-'0');
	}

	const int endval=1000000;
	auto cups=Node::init(endval);
	Node* lookup[endval+1];
	set_start_values(cups,start_values);

	Node *cur=cups;
	do{
		lookup[cur->value]=cur;
		cur=cur->next;
	} while(cur!=cups);

	for(int i=0;i<10000000;i++){
		do_turn(cups,lookup,endval);
	}
	unsigned long v1=lookup[1]->next->value;
	unsigned long v2=lookup[1]->next->next->value;
	std::cout<<"Second solution: "<<v1*v2<<std::endl;
}