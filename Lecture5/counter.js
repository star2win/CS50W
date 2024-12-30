document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('button').onclick = count; });

let counter = 0;

function count() {
    counter++;
    document.querySelector('#counter').innerHTML = counter;

    if (counter % 10 == 0) {
        alert(`Counter is at ${counter}!`);
    }
} 

/*
Variable types:
* const (a constant / not changeable later on in the code)
* let (a variable that exists only in the innermost curly braces)
* var (a variable exists in whole function, even if it was in curly braces within
*/
