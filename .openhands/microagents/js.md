---
triggers:
- js
---

# JavaScript Knowledge

This microagent provides information about JavaScript when triggered.

## What is JavaScript?

JavaScript is a high-level, interpreted programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS. It enables interactive web pages and is an essential part of web applications.

## Key Features

- **Dynamic Typing**: Variables don't need explicit type declarations
- **First-Class Functions**: Functions can be assigned to variables, passed as arguments, and returned from other functions
- **Prototype-Based Object Orientation**: Objects can inherit directly from other objects
- **Event-Driven Programming**: Responds to user interactions and system events
- **Asynchronous Programming**: Supports callbacks, promises, and async/await

## Common Use Cases

1. **Web Development**: Interactive websites, single-page applications (SPAs)
2. **Server-Side Development**: Node.js for backend applications
3. **Mobile App Development**: React Native, Ionic
4. **Desktop Applications**: Electron framework
5. **Game Development**: Browser-based games
6. **IoT and Embedded Systems**: JavaScript on microcontrollers

## Popular Frameworks and Libraries

- **Frontend**: React, Vue.js, Angular, Svelte
- **Backend**: Node.js, Express.js, Nest.js
- **Testing**: Jest, Mocha, Cypress
- **Build Tools**: Webpack, Vite, Parcel

## Basic Syntax Examples

```javascript
// Variables
let name = "JavaScript";
const year = 1995;

// Functions
function greet(name) {
    return `Hello, ${name}!`;
}

// Arrow functions
const add = (a, b) => a + b;

// Objects
const person = {
    name: "John",
    age: 30,
    greet() {
        return `Hi, I'm ${this.name}`;
    }
};

// Arrays
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(n => n * 2);

// Promises
fetch('/api/data')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));

// Async/Await
async function fetchData() {
    try {
        const response = await fetch('/api/data');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error:', error);
    }
}
```

## Learning Resources

- **MDN Web Docs**: Comprehensive JavaScript documentation
- **JavaScript.info**: Modern JavaScript tutorial
- **Eloquent JavaScript**: Free online book
- **FreeCodeCamp**: Interactive coding lessons
- **You Don't Know JS**: Book series on JavaScript fundamentals

JavaScript continues to evolve with new features added regularly through ECMAScript specifications, making it a versatile and powerful language for modern development.