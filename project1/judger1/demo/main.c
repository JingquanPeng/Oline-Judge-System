// #include <stdio.h>
// 
// int main(int argc, char *argv[]) {
//     char input[1000];
//     scanf("%s", input);
//     printf("Hello %s\n", input);
//     return 0;
// }

#include <stdio.h>

int main() {
    int N;
    scanf("%d\n", &N);

    for (int i = 0; i < N; i++) {
        int a, b;
        scanf("%d %d\n", &a, &b);
        printf("%d\n", a + b);
    }
}
