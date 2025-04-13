# Dexter

Proyecto fullstack compuesto por:

- **front**: Angular
- **back**: FastAPI

## Front

- Para el front es importante agregar es-lint: `ng add @angular-eslint/schematics`
- Comando para repara automaticamente: `pnpm lint --fix`
- Instalar Prettier: `pnpm add prettier -D`
- En el archivo `package.json` en la sesión scripts agregar el comando: `"format": "prettier --write ."`

```json
"scripts": {
  "format": "prettier --write ."
}
```

- Crear un archivo `.prettier.json` y agregar los siguiente:

```json
{
  "tabWidth": 2,
  "useTabs": false,
  "singleQuote": true,
  "semi": true,
  "bracketSpacing": true,
  "arrowParens": "avoid",
  "trailingComma": "es5",
  "bracketSameLine": true,
  "printWidth": 80
}
```

- Para que ESLint y Prettier trabajen en armonía, es necesario los siguientes paquetes adicionales: `pnpm add eslint-config-prettier eslint-plugin-prettier -D`
