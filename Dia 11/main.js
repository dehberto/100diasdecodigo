let box = document.querySelector('.box');
let input = document.querySelector('input');

input.addEventListener('input', () =>{
    box.computedStyleMap.borderRadius = input.value;
    box.computedStyleMap.background = input.value;
})