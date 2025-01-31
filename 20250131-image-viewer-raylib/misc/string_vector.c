#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STRINGS 100
#define MAX_STRING_LENGTH 100

typedef struct {
    char** data;
    int size;
    int capacity;
} sv_vector;

// Function to initialize the vector
void sv_init(sv_vector* vector) {
    vector->data = (char**)malloc(MAX_STRINGS * sizeof(char*));
    for (int i = 0; i < MAX_STRINGS; i++) {
        vector->data[i] = (char*)malloc(MAX_STRING_LENGTH * sizeof(char));
    }
    vector->size = 0;
    vector->capacity = MAX_STRINGS;
}

// Function to add a string to the vector
void sv_add(sv_vector* vector, const char* str) {
    if (vector->size < vector->capacity) {
        strncpy(vector->data[vector->size], str, MAX_STRING_LENGTH - 1);
        vector->data[vector->size][MAX_STRING_LENGTH - 1] = '\0'; // Ensure null termination
        vector->size++;
    }
}

// Function to free the memory allocated for the vector
void sv_free(sv_vector* vector) {
    for (int i = 0; i < vector->capacity; i++) {
        free(vector->data[i]);
    }
    free(vector->data);
}

int main() {
    sv_vector vector;
    sv_init(&vector);

    sv_add(&vector, "hello world");
    sv_add(&vector, "c programming");
    sv_add(&vector, "vector of strings");

    // Printing strings
    for (int i = 0; i < vector.size; i++) {
        printf("%s\n", vector.data[i]);
    }

    sv_free(&vector);
    return 0;
}
