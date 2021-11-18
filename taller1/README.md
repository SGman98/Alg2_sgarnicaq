# Encontrar substring en una cadena usando fuerza bruta

El codigo usado para resolver este problema es el siguiente:

```python
def fuerza_bruta(target, sequence): # O(n)==???
    target_len = len(target) # O(1)
    sequence_len = len(sequence) # O(1)

    result = [] # O(1)
    for i in range(sequence_len - target_len + 1): # O(n)
        for j, _ in enumerate(target): # O(m)
            if (target[j] == sequence[i + j]): # O(1)
                if (j < target_len - 1): # O(1)
                    continue # O(1)
                result.append((i, i + target_len - 1)) # O(1)
                break # O(1)
            break # O(1)

    return result # O(1)
```

### Funcionamiento del Codigo

1. Se itera sobre `sequence`
2. Por cada iteracion de la secuencia se itera sobre `target`
3. Mientras el elemento en `target` sea igual al elemento en `sequence` sigue iterando `target`
4. Si en la ultima iteracion de `target` se evidencia que existe la cadena en `sequence` se adjunta el resultado
a `result`
5. En caso contrario se rompe el bucle de `target` y se sigue iterando sobre `sequence`
6. Al final de los bucles se retorna la lista de `result`

### Reduccion problema complejidad O(n)=
```
fuerza_bruta
 ├── asignacion                             O(1)
 ├── asignacion                             O(1)
 ├── asignacion                             O(1)
 ├── bucle                                  O(n)
 │   └── bucle                              O(m)
 │       ├── condicion                      O(1)
 │       │   │F     │T
 │       │          ├── condicion           O(1)
 │       │          │   │F     │T
 │       │          │          └── continue O(1)
 │       │          ├── append              O(1)
 │       │          └── break               O(1)
 │       └── break                          O(1)
 └── retorno                                O(1)
```
> Como en la condicion no hay ningun bucle interno, el tiempo de ejecucion de la condicion externa es O(1)
```
fuerza_bruta
 ├── asignacion                             O(1)
 ├── asignacion                             O(1)
 ├── asignacion                             O(1)
 ├── bucle                                  O(n)
 │   └── bucle                              O(m)
 │       ├── condicion                      O(1)
 |       └── break                          O(1)
 └── retorno                                O(1)
```
> Para los bucles se multiplica el O de la condicion por el O de la iteracion interna teniendo en cuenta que aquellos O en la misma linea se suman
```md
fuerza_bruta
 ├── asignacion                             O(1)
 ├── asignacion                             O(1)
 ├── asignacion                             O(1)
 ├── bucle    O(n) * O(m) * [O(1) + O(1)] = O(n*m)
 └── retorno                                O(1)
```
> ya no quedan mas bucles ni condiciones por lo que se suma el O de la iteracion interna
```
fuerza_bruta  O(n) * O(m) * [O(1) + O(1)] = O(n*m)
```
> Teniendo en cuenta que `n` es el la longitud de la secuencia `sequence`
y `m` es la longitud de la cadena objetivo `target`
