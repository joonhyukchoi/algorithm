#include <iostream>

class Node {
    public:
        int data;
        Node* left;
        Node* right;
    Node(int num) {
        data = num;
        left = NULL;
        right = NULL;
    }
};

class Tree{
    public:
        void inorder(Node* currentNode) {
            inorder(currentNode->left);
            std::cout << currentNode->data;
            inorder(currentNode->right);
        }

        void insertNode(int num) {
            Node* new_node = new Node(num);
            if (root = NULL) {
                root = new_node;
            } else {
                Node* now = root;
                while (now != NULL) {
                    Node* temp = now;
                    if (now->data > num) {
                        now = now->left;
                    } else {
                        now = now->right;
                    }
                    if (temp->data > num) {
                        temp->left = new_node;
                    } else {
                        temp->right = new_node;
                    }
                }
            }
        }
    private:
        Node* root;
};