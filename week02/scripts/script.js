console.log("JavaScript is connected and running!");
alert("Welcome to my WDD 131 - BOM Example!");

const input = document.querySelector('#favchap');
const button = document.querySelector('button');
const list = document.querySelector('_______');

const li = document.createElement('li');

const deleteButton = document.createElement('button');

li.textContent = input.value;

deleteButton.textContent = '❌';

li.append(deleteButton);

list.append(li);



button.addEventListener('click', function() {
   if (input.value.trim() !== '') {
   }    
});
  
deleteButton.addEventListener('click', function() {
  list.removeChild(li);
  input.focus();

});

input.value = '';
input.focus();