//Exercício linguagem C 2022 - 14/02/2022

//Exercício 1
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
    int numero,quadrado;
    scanf("%d",&numero);
    quadrado = pow(numero,2);
    printf("%d", quadrado);

    return 0;
}


//Exercício 2
#include <stdio.h>
#include <stdlib.h>

int main(){

    double a, b, c, resultado;

    scanf("%lf%lf%lf", &a, &b, &c);

    resultado = -b/(2*a);
    printf("%.4lf", resultado);
}

//Exercício 3
#include <stdio.h>
#include <stdlib.h>

int main() {
    int seg, h, m, s, resto;
    
    scanf("%d", &seg);
    
    h = seg / 3600;
    resto = seg % 3600;
    m = resto / 60;
    s = resto % 60;
    
    printf("%d:%d:%d\n", h, m, s);
    
    return 0;
}

//Exercício 4

//Exercício 5

//Exercício 6
