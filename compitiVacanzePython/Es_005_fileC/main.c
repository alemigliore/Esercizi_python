#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#define DIM 3

//
//Usando la funzione dell'esercizio precedente, scrivere la funzione isIsoscele() che,
//dati 3 numeri, restituisce true/1 se possono essere le misure di un triangolo
//equilatero, false/0 altrimenti. Creare un main che testi questa funzione.
//

bool isTriangolo(float l1, float l2, float l3){

    return (l1 < l2+l3 && l2 < l1+l3 && l3 < l1+l2);

}

bool isIsoscele(int l1, int l2, int l3){

    return (isTriangolo(l1, l2, l3) && (l1 == l2) || (l2 == l3) || (l1 == l3));

}

int nonNegativo(char frase[]){
    int n;

    do{
        printf("%s", frase);
        fflush(stdin);
        scanf("%d", &n);
    }while(n < 0);

    return n;
}


int main()
{
    int l1;
    int l2;
    int l3;

    l1 = nonNegativo("Inserisci un lato: ");
    l2 = nonNegativo("inserisci il secondo lato: ");
    l3 = nonNegativo("Inserisci il terzo lato: ");
    printf("\n");

   if(isTriangolo(l1, l2, l3) == true){
        if(isIsoscele(l1, l2, l3) == true){
        printf("puo' essere un triangolo isoscele\n");
    }else{
        printf("non puo' essere un triangolo isoscele\n");
    }
    }else{
        printf("non puo' essere un triangolo\n");
    }

    return 0;
}
