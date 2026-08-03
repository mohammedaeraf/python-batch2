# Python comparison with other programs

```python
n = 7
rem = n % 2

if rem == 0:
    print(n, "is even")
else:
    print(n, "is odd")
```

---

# Java

```java
public class EvenOdd {
    public static void main(String[] args) {

        int n = 7;
        int rem = n % 2;

        if (rem == 0) {
            System.out.println(n + " is even");
        } else {
            System.out.println(n + " is odd");
        }

    }
}
```

### Things to Notice

- Requires a class.
- Requires the `main()` method.
- Variables must have a data type (`int`).
- Uses `System.out.println()` for output.
- Curly braces `{}` define code blocks.

---

# C

```c
#include <stdio.h>

int main() {

    int n = 7;
    int rem = n % 2;

    if (rem == 0) {
        printf("%d is even\n", n);
    } else {
        printf("%d is odd\n", n);
    }

    return 0;
}
```

### Things to Notice

- Includes the `stdio.h` library.
- Requires the `main()` function.
- Variables must have data types.
- Uses `printf()` instead of `print()`.
- Format specifier `%d` is used for integers.

---

# JavaScript

```javascript
let n = 7;
let rem = n % 2;

if (rem == 0) {
  console.log(n + " is even");
} else {
  console.log(n + " is odd");
}
```

### Things to Notice

- Uses `let` to declare variables.
- No need to specify the data type.
- Uses `console.log()` for output.
- Curly braces `{}` define code blocks.

---

# Comparison Table

| Feature                   | Python    | Java                   | C          | JavaScript           |
| ------------------------- | --------- | ---------------------- | ---------- | -------------------- |
| Variable Type Required    | ❌ No     | ✅ Yes                 | ✅ Yes     | ❌ No (`let`)        |
| Curly Braces `{}`         | ❌ No     | ✅ Yes                 | ✅ Yes     | ✅ Yes               |
| Semicolon `;`             | ❌ No     | ✅ Yes                 | ✅ Yes     | ✅ Yes (recommended) |
| Main Function Required    | ❌ No     | ✅ Yes                 | ✅ Yes     | ❌ No                |
| Output Statement          | `print()` | `System.out.println()` | `printf()` | `console.log()`      |
| Indentation Defines Block | ✅ Yes    | ❌ No                  | ❌ No      | ❌ No                |

---

## Important Point

> **"Which language is easiest to read?"**

Advantages of Python:

- Uses fewer lines of code.
- Doesn't require a `main()` method.
- Doesn't require data type declarations.
- Doesn't use curly braces `{}`.
- Doesn't require semicolons (`;`).

This makes Python an excellent first programming language while still being powerful enough for web development, automation, AI, data science, and many other applications.

---

# Program 2 - Area of a Rectangle

```python
input1 = input("Enter the length: ")
length = int(input1)

input2 = input("Enter the breadth: ")
breadth = int(input2)

area = length * breadth

print("Area =", area)
```

---

# C

```c
#include <stdio.h>

int main() {

    int length, breadth, area;

    printf("Enter the length: ");
    scanf("%d", &length);

    printf("Enter the breadth: ");
    scanf("%d", &breadth);

    area = length * breadth;

    printf("Area = %d\n", area);

    return 0;
}
```

### Things to Notice

- Variables must be declared with a data type (`int`).
- Uses `scanf()` to accept user input.
- `&` is used to pass the memory address to `scanf()`.
- Uses `printf()` to display the output.

---

# Java

```java
import java.util.Scanner;

public class RectangleArea {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the length: ");
        int length = sc.nextInt();

        System.out.print("Enter the breadth: ");
        int breadth = sc.nextInt();

        int area = length * breadth;

        System.out.println("Area = " + area);

        sc.close();
    }
}
```

### Things to Notice

- Requires the `Scanner` class for user input.
- Variables must have a data type (`int`).
- Requires a class and the `main()` method.
- Uses `nextInt()` to read integers.
- It is good practice to close the `Scanner` using `sc.close()`.

---

# Comparison

| Feature                      | Python        | C                            | Java                       |
| ---------------------------- | ------------- | ---------------------------- | -------------------------- |
| Input Function               | `input()`     | `scanf()`                    | `Scanner.nextInt()`        |
| Type Conversion              | `int()`       | Not required (`scanf("%d")`) | Not required (`nextInt()`) |
| Variable Declaration         | `length = 10` | `int length;`                | `int length;`              |
| Output                       | `print()`     | `printf()`                   | `System.out.println()`     |
| Main Function Required       | ❌ No         | ✅ Yes                       | ✅ Yes                     |
| Additional Library for Input | ❌ No         | `stdio.h`                    | `java.util.Scanner`        |

### Tip

This example clearly demonstrates why Python is popular among beginners:

- **Python:** 7 simple lines with straightforward syntax.
- **C:** Requires `#include`, `main()`, `printf()`, `scanf()`, format specifiers (`%d`), and memory address operator (`&`).
- **Java:** Requires `Scanner`, `import`, a class, the `main()` method, `nextInt()`, and object creation.

Students usually appreciate how much less boilerplate code Python requires, allowing them to focus on programming logic rather than language syntax.
